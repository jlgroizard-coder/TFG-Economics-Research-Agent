import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "student_project.py"
spec = importlib.util.spec_from_file_location("student_project", SCRIPT)
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

class StudentProjectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "TFG_ficticio"

    def test_initialize_folders_and_onboarding(self):
        r = student.init(self.root)
        self.assertTrue((self.root / "LEEME_PRIMERO.md").is_file())
        self.assertTrue((self.root / "CLAUDE.md").is_file())
        self.assertTrue((self.root / "AGENTS.md").is_file())
        self.assertTrue((self.root / "01_propuesta" / "E01_dos_preguntas.md").is_file())
        self.assertIn("E01", r["next_step"])
        self.assertTrue((self.root / ".tfg/agent/references/rubrica.md").is_file())
        self.assertTrue((self.root / ".tfg/tools/student_project.py").is_file())
        with self.assertRaises(ValueError):
            student.init(self.root)

    def test_submit_edit_and_resubmit_without_pre_command(self):
        student.init(self.root)
        p = self.root / "01_propuesta/E01_dos_preguntas.md"
        p.write_text("borrador original", encoding="utf-8")
        a = student.submit(self.root, "01_propuesta/E01_dos_preguntas.md")
        self.assertEqual(a["status"], "guardado")
        self.assertEqual(student.submit(self.root, "01_propuesta/E01_dos_preguntas.md")["status"], "sin_cambios")
        p.write_text("borrador corregido", encoding="utf-8")
        b = student.submit(self.root, "01_propuesta/E01_dos_preguntas.md")
        self.assertEqual(b["status"], "guardado")
        self.assertNotEqual(a["submission"]["sha256"], b["submission"]["sha256"])
        original = self.root / a["submission"]["snapshot"]
        self.assertEqual(original.read_text(), "borrador original")
        self.assertEqual(student.status(self.root)["submissions"],2)

    def test_skip_outside_and_internal_files(self):
        student.init(self.root)
        with self.assertRaises(ValueError):
            student.submit(self.root, "../secrets.txt")
        with self.assertRaises(ValueError):
            student.submit(self.root, ".tfg/registro.json")
        with self.assertRaises(ValueError):
            student.submit(self.root, "06_evaluaciones/eval.md")

    def test_cli_from_student_project_folder(self):
        student.init(self.root)
        result = subprocess.run([sys.executable, str(self.root / ".tfg/tools/student_project.py"),
                                 "submit", str(self.root), "01_propuesta/E01_dos_preguntas.md"],
                                text=True, capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"],"guardado")

if __name__ == "__main__":
    unittest.main()
