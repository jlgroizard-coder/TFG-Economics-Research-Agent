import tempfile
import unittest
from pathlib import Path
from audit_package import audit

class AuditTests(unittest.TestCase):
    def test_empty(self):
        with tempfile.TemporaryDirectory() as d:
            result=audit(Path(d),"empirico")
            self.assertFalse(result["comprobaciones"]["readme"])
            self.assertFalse(result["reproduccion_ejecutada"])

    def test_minimal_project(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for f in ("README.md","manuscrito/tfg.pdf","codigo/run.py","resultados/table.csv","datos/data.csv"):
                p=root/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_text("test")
            result=audit(root,"empirico")
            self.assertFalse(result["advertencias"])

if __name__=="__main__":
    unittest.main()
