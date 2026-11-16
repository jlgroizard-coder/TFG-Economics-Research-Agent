import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

spec = importlib.util.spec_from_file_location("repro_package", Path(__file__).with_name("repro_package.py"))
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

class ReproducibilityZipTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "student"
        self.root.mkdir()
        for dir in ("07_entrega", "03_datos", "04_analisis", ".tfg"):
            (self.root / dir).mkdir()
        (self.root / "07_entrega" / "TFG_final.pdf").write_bytes(b"%PDF-1.4 test only")
        (self.root / "07_entrega" / "README_REPRODUCCION.md").write_text("Pasos de reproducción", encoding="utf-8")
        (self.root / "03_datos" / "datos.csv").write_text("a,b\n1,2\n", encoding="utf-8")
        (self.root / ".tfg" / "registro.json").write_text("privado")
        self.manifest = self.root / p.MANIFEST
        self.manifest.write_text("07_entrega/TFG_final.pdf\n07_entrega/README_REPRODUCCION.md\n03_datos/datos.csv\n")

    def test_zip_contains_only_chosen_inputs(self):
        output = Path(self.tmp.name) / "TFG_entrega.zip"
        info = p.build(self.root, output)
        self.assertEqual(info["included_files"],3)
        with zipfile.ZipFile(output) as z:
            names = set(z.namelist())
            self.assertIn("MANIFIESTO_SHA256.json",names)
            self.assertEqual(len(names),4)
            self.assertNotIn(".tfg/registro.json",names)
            hashes = json.loads(z.read("MANIFIESTO_SHA256.json"))
            self.assertEqual(hashes["total_files"],3)

    def test_reject_traversal_and_private_and_missing(self):
        for name in ("../privado.txt", ".tfg/registro.json", "06_evaluaciones/eval.md",
                     "03_datos/no_existe.csv"):
            self.manifest.write_text("07_entrega/TFG_final.pdf\n07_entrega/README_REPRODUCCION.md\n"+name+"\n")
            with self.assertRaises(ValueError):
                p.check(self.root)

    def test_requires_pdf_and_readme(self):
        self.manifest.write_text("03_datos/datos.csv\n07_entrega/README_REPRODUCCION.md\n")
        with self.assertRaisesRegex(ValueError,"PDF"):
            p.check(self.root)
        self.manifest.write_text("07_entrega/TFG_final.pdf\n")
        with self.assertRaisesRegex(ValueError,"README"):
            p.check(self.root)

    def test_originals_untouched_and_no_overwrite(self):
        out=Path(self.tmp.name)/"result.zip"
        p.build(self.root,out)
        self.assertTrue((self.root/"03_datos/datos.csv").is_file())
        with self.assertRaises(ValueError):
            p.build(self.root,out)

    def test_sensitive_and_discarded_filenames_rejected(self):
        names=("03_datos/datos_restringidos.csv","03_datos/exploratorio_descartado.csv",
               "04_analisis/api_key.txt","07_entrega/credenciales.txt","03_datos/clave.pem")
        for name in names:
            pth=self.root/name
            pth.parent.mkdir(parents=True,exist_ok=True)
            pth.write_text("contenido de prueba")
            self.manifest.write_text("07_entrega/TFG_final.pdf\n"
                                     "07_entrega/README_REPRODUCCION.md\n"+name+"\n")
            with self.assertRaisesRegex(ValueError,"privados"):
                p.check(self.root)

    def test_excluded_candidates_are_visible(self):
        (self.root/"03_datos"/"exploratorio_descartado.csv").write_text("x")
        result=p.check(self.root)
        self.assertIn("03_datos/exploratorio_descartado.csv",result["excluded_candidates"])
        self.assertIn("no asegura",result["warning"])

    def test_symlink_rejected(self):
        outside=Path(self.tmp.name)/"private.txt"
        outside.write_text("secret")
        link=self.root/"03_datos"/"linked.csv"
        try:
            link.symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        self.manifest.write_text("07_entrega/TFG_final.pdf\n07_entrega/README_REPRODUCCION.md\n03_datos/linked.csv\n")
        with self.assertRaises(ValueError):
            p.check(self.root)

if __name__ == "__main__":
    unittest.main()
