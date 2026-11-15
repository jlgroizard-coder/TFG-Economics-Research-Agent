"""Prueba sintética de paquete ZIP desde una copia limpia.

Simula un estudiante operando el ZIP; NO acredita aprendizaje ni reproducción
autónoma de un estudiante real. No accede a datos de usuarios.
"""
import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("repro_package", HERE / "repro_package.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)

CALCULATE = """import csv
from pathlib import Path
rows=list(csv.DictReader(Path('03_datos/variables.csv').open(encoding='utf-8')))
mean=sum(float(r['salario']) for r in rows)/len(rows)
Path('resultado.json').write_text(__import__('json').dumps({'n':len(rows),'media':mean}))
"""

class StudentReproductionUsabilityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="tfg_ux_repro_")
        self.addCleanup(temp.cleanup)
        self.base=Path(temp.name)
        self.project=self.base/"proyecto_ficticio"
        for folder in ("03_datos","04_analisis","07_entrega",".tfg","06_evaluaciones"):
            (self.project/folder).mkdir(parents=True,exist_ok=True)
        (self.project/"03_datos/variables.csv").write_text(
            "salario\n10\n20\n30\n40\n",encoding="utf-8")
        (self.project/"03_datos/exploratorio_descartado.csv").write_text(
            "no_usar\n999\n",encoding="utf-8")
        (self.project/"04_analisis/calcular.py").write_text(CALCULATE,encoding="utf-8")
        (self.project/".tfg/registro.json").write_text('{"private":true}')
        (self.project/"06_evaluaciones/borrador.md").write_text("nota orientativa")
        (self.project/"07_entrega/TFG_final.pdf").write_bytes(b"%PDF-1.4 synthetic test")
        (self.project/"07_entrega/README_REPRODUCCION.md").write_text(
            "# Reproducción\n\nDesde la carpeta EXTRAÍDA:\n"
            "python3 04_analisis/calcular.py\n\n"
            "Comprueba resultado.json: n=4, media=25.\n"
            "Software: Python 3, biblioteca estándar.\n",encoding="utf-8")
        (self.project/"07_entrega/ARCHIVOS_INCLUIDOS.txt").write_text(
            "07_entrega/TFG_final.pdf\n"
            "07_entrega/README_REPRODUCCION.md\n"
            "03_datos/variables.csv\n"
            "04_analisis/calcular.py\n",encoding="utf-8")

    def extract(self):
        archive=self.base/"entrega_final.zip"
        package.build(self.project,archive)
        clean=self.base/"solo_zip"
        clean.mkdir()
        with zipfile.ZipFile(archive) as z:
            z.extractall(clean)
            names=z.namelist()
        return clean,names

    def run_clean(self,root):
        return subprocess.run(
            [sys.executable,"04_analisis/calcular.py"],
            cwd=root,text=True,capture_output=True,check=False)

    def test_extract_run_and_compare_with_claim(self):
        clean,names=self.extract()
        self.assertNotIn("03_datos/exploratorio_descartado.csv",names)
        self.assertNotIn(".tfg/registro.json",names)
        self.assertNotIn("06_evaluaciones/borrador.md",names)
        process=self.run_clean(clean)
        self.assertEqual(process.returncode,0,process.stderr)
        result=json.loads((clean/"resultado.json").read_text())
        self.assertEqual(result["n"],4)
        self.assertEqual(result["media"],25)

    def test_detect_deliberately_incorrect_manuscript_claim(self):
        clean,_=self.extract()
        self.assertEqual(self.run_clean(clean).returncode,0)
        actual=json.loads((clean/"resultado.json").read_text())["media"]
        manuscript_claim=26 # discrepancy intentionally introduced by evaluator
        self.assertNotEqual(actual,manuscript_claim)

    def test_missing_essential_script_blocks_reproduction(self):
        self.project.joinpath("04_analisis/calcular.py").unlink()
        with self.assertRaisesRegex(ValueError,"No existe"):
            package.check(self.project)

    def test_missing_input_from_manifest_breaks_clean_run(self):
        # Structural ZIP integrity is not scientific reproducibility:
        # script is present but the input data are omitted.
        manifest=self.project/"07_entrega/ARCHIVOS_INCLUIDOS.txt"
        manifest.write_text("07_entrega/TFG_final.pdf\n"
                            "07_entrega/README_REPRODUCCION.md\n"
                            "04_analisis/calcular.py\n",encoding="utf-8")
        clean,_=self.extract()
        result=self.run_clean(clean)
        self.assertNotEqual(result.returncode,0)
        self.assertFalse((clean/"03_datos/variables.csv").exists())

if __name__=="__main__":
    unittest.main()
