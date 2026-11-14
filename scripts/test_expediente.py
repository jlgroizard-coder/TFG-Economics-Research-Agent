import json
import tempfile
import unittest
from pathlib import Path
from expediente import init_case, add_artifact, evidence, audit, open_case, add_evaluation

class ExpedienteTests(unittest.TestCase):
    def test_init_is_private_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"private"
            init_case(root,"SINTETICO")
            self.assertEqual(open_case(root)["schema_version"],"0.2")
            self.assertTrue((root/"evaluaciones").is_dir())
            with self.assertRaises(ValueError):
                init_case(root,"OTHER")

    def test_versioned_evidence_not_discarded(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"case"
            init_case(root,"SINTETICO")
            path=root/"02_literatura"/"revision.md"
            path.write_text("Texto original de literatura.",encoding="utf-8")
            add_artifact(root,"02_literatura/revision.md","literatura","v2")
            evidence(root,"B","vigente_verificada","02_literatura/revision.md","v2","Leído")
            # Nueva versión del capítulo de resultados: literatura sigue existiendo y no desaparece.
            (root/"06_resultados"/"tabla.csv").write_text("col\n1\n",encoding="utf-8")
            add_artifact(root,"06_resultados/tabla.csv","resultados","v3")
            self.assertEqual(len(open_case(root)["evidence"]),1)
            self.assertTrue(all(x["unchanged"] for x in audit(root)["artifacts"]))

    def test_modification_is_detected_but_not_automatically_graded(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"case"
            init_case(root,"SINTETICO")
            path=root/"01_propuesta"/"v1.md"
            path.write_text("a",encoding="utf-8")
            add_artifact(root,"01_propuesta/v1.md","propuesta","v1")
            path.write_text("b",encoding="utf-8")
            self.assertFalse(audit(root)["artifacts"][0]["unchanged"])
            self.assertIn("NO demuestra",audit(root)["warning"])

    def test_provisional_evaluation_does_not_invent_global_score(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"case"
            init_case(root,"SINTETICO")
            report=root/"evaluaciones"/"v3.md"
            report.write_text("Evaluación de capítulo",encoding="utf-8")
            with self.assertRaises(ValueError):
                add_evaluation(root,"v3","E09","parcial","evaluaciones/v3.md",complete=3.5)
            row=add_evaluation(root,"v3","E09","parcial","evaluaciones/v3.md",
                               technical=9.0,consistency=2.0)
            self.assertIsNone(row["complete_score"])
            self.assertEqual(len(open_case(root)["evaluations"]),1)

    def test_block_path_traversal(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"case"
            init_case(root,"SINTETICO")
            with self.assertRaises(ValueError):
                evidence(root,"A","pendiente","../../secret.txt","v1","no")

if __name__=="__main__":
    unittest.main()
