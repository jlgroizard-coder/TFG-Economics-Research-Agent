import tempfile
import unittest
from pathlib import Path
from expediente import (init_case, add_artifact, add_evidence, add_decision,
                        add_evaluation, revoke_evaluation, audit, open_case, migrate_legacy_reports)

class ExpedienteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "case"
        init_case(self.root, "SINTETICO")

    def file(self, rel, content="texto"):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def validated(self, criterion, rel, version="v2"):
        self.file(rel)
        add_artifact(self.root, rel, "literatura", version)
        add_evidence(self.root, criterion, "vigente_verificada", rel, version, "Comprobado")

    def test_init_no_overwrite(self):
        with self.assertRaises(ValueError):
            init_case(self.root, "OTHER")

    def test_continuity(self):
        self.validated("B", "02_literatura/revision.md")
        self.file("06_resultados/v3.csv", "x\n1\n")
        add_artifact(self.root, "06_resultados/v3.csv", "resultados", "v3")
        items = audit(self.root)["effective_evidence"]
        self.assertEqual(items[0]["status"], "vigente_verificada")

    def test_missing_file_blocks_complete_evaluation(self):
        for criterion in "ABCDEFGH":
            self.validated(criterion, "01_propuesta/"+criterion+".md")
        report = self.file("evaluaciones/v3.md")
        (self.root/"01_propuesta/B.md").rename(self.root/"01_propuesta/B-quarantine.md")
        with self.assertRaisesRegex(ValueError, "inaccesible"):
            add_evaluation(self.root, "v3", "E09", "expediente_completo",
                           "evaluaciones/v3.md", 3.8, 3.8)
        self.assertEqual(len(open_case(self.root)["evaluations"]), 0)
        self.assertEqual(
            [r for r in audit(self.root)["effective_evidence"] if r["criterion"]=="B"][0]["status"],
            "no_aportada_ahora")

    def test_modified_file_needs_revalidation(self):
        self.validated("B", "02_literatura/lit.md")
        self.file("02_literatura/lit.md", "modificado")
        self.assertEqual(audit(self.root)["effective_evidence"][0]["status"], "desactualizada")

    def test_new_decision_invalidates_dependent_items(self):
        self.validated("B", "02_literatura/lit.md")
        self.validated("D", "01_propuesta/met.md")
        res = add_decision(self.root, "metodo", "Cambio a panel")
        statuses = {x["criterion"]: x["status"] for x in audit(self.root)["effective_evidence"]}
        self.assertEqual(statuses["B"], "vigente_verificada")
        self.assertEqual(statuses["D"], "desactualizada")
        self.assertIn("D", res["decision"]["affected_criteria"])

    def test_question_invalidates_old_evidence(self):
        self.validated("A", "01_propuesta/question.md")
        add_decision(self.root, "pregunta", "Nuevas regiones", "Pregunta nueva")
        self.assertEqual(open_case(self.root)["research_question"], "Pregunta nueva")
        self.assertEqual(audit(self.root)["effective_evidence"][0]["status"], "desactualizada")

    def test_latest_status_not_historical_count(self):
        self.validated("B", "02_literatura/lit.md")
        add_evidence(self.root, "B", "pendiente", "02_literatura/lit.md", "v3", "Por revisar")
        counts = audit(self.root)["effective_status_counts"]
        self.assertEqual(counts["vigente_verificada"],0)
        self.assertEqual(counts["pendiente"],1)

    def test_report_integrity_and_revocation(self):
        for criterion in "ABCDEFGH":
            self.validated(criterion, "01_propuesta/"+criterion+".md")
        report = self.file("evaluaciones/v3.md")
        add_evaluation(self.root, "v3", "E09", "expediente_completo",
                       "evaluaciones/v3.md", 3.8,3.8)
        report.write_text("informe manipulado",encoding="utf-8")
        self.assertFalse(audit(self.root)["evaluation_reports"][0]["intact"])
        revoke_evaluation(self.root, "v3", "evaluaciones/v3.md", "Informe corregido")
        self.assertTrue(audit(self.root)["evaluation_reports"][0]["revoked"])

    def test_partial_cannot_record_global_score(self):
        self.file("evaluaciones/v3.md")
        with self.assertRaises(ValueError):
            add_evaluation(self.root, "v3", "E09", "parcial",
                           "evaluaciones/v3.md", complete=3.8)
        entry = add_evaluation(self.root, "v3", "E09", "parcial",
                               "evaluaciones/v3.md",technical=7.5, consistency=2.0)
        self.assertIsNone(entry["complete_score"])

    def test_empty_evidence_blocks_global_grade(self):
        self.file("evaluaciones/v3.md")
        with self.assertRaisesRegex(ValueError, "sin evidencia"):
            add_evaluation(self.root,"v3","E09","expediente_completo",
                           "evaluaciones/v3.md",3.8,3.8)

    def test_path_escape(self):
        with self.assertRaises(ValueError):
            add_evidence(self.root, "A", "pendiente", "../outside", "v1", "x")
        with self.assertRaises(ValueError):
            add_evidence(self.root, "A", "pendiente", "/tmp/outside", "v1", "x")


    def test_status_overwrite_cannot_hide_missing_verified_file(self):
        for c in "ABCDEFGH":
            self.validated(c, "01_propuesta/"+c+".md")
        self.file("evaluaciones/test.md")
        (self.root/"01_propuesta/B.md").unlink()
        for status in ("pendiente","vigente_no_verificada"):
            add_evidence(self.root,"B",status,"01_propuesta/B.md","v3","Intento de elusión")
            with self.assertRaises(ValueError):
                add_evaluation(self.root,"v3","E09","expediente_completo",
                               "evaluaciones/test.md",3.8,3.8)
        self.assertEqual(len(open_case(self.root)["evaluations"]),0)

    def test_status_overwrite_cannot_hide_modified_verified_file(self):
        for c in "ABCDEFGH":
            self.validated(c, "01_propuesta/"+c+".md")
        self.file("evaluaciones/test.md")
        self.file("01_propuesta/C.md","modificado")
        add_evidence(self.root,"C","pendiente","01_propuesta/C.md","v3","Intento de elusión")
        self.assertEqual([x for x in audit(self.root)["effective_evidence"]
                          if x["criterion"]=="C"][0]["status"],"desactualizada")
        with self.assertRaises(ValueError):
            add_evaluation(self.root,"v3","E09","expediente_completo",
                           "evaluaciones/test.md",3.8,3.8)

    def test_stale_global_score_on_decision_and_evidence_change(self):
        for c in "ABCDEFGH":
            self.validated(c, "01_propuesta/"+c+".md")
        self.file("evaluaciones/test.md")
        add_evaluation(self.root,"v3","E09","expediente_completo",
                       "evaluaciones/test.md",3.8,3.8)
        add_decision(self.root,"pregunta","Nueva pregunta","Nueva")
        self.assertTrue(audit(self.root)["evaluation_reports"][0]["obsolete"])

    def test_legacy_migration_does_not_claim_historical_integrity(self):
        for c in "ABCDEFGH":
            self.validated(c, "01_propuesta/"+c+".md")
        self.file("evaluaciones/test.md")
        add_evaluation(self.root,"v3","E09","expediente_completo",
                       "evaluaciones/test.md",3.8,3.8)
        obj=open_case(self.root)
        del obj["evaluations"][0]["report_sha256"]
        from expediente import save_case
        save_case(self.root,obj)
        self.assertFalse(audit(self.root)["evaluation_reports"][0]["intact"])
        result=migrate_legacy_reports(self.root,"Acepto línea de base actual")
        self.assertEqual(len(result["baselines_created"]),1)
        self.assertTrue(audit(self.root)["evaluation_reports"][0]["legacy_baseline_only"])

    def test_nan_scores_rejected(self):
        self.file("evaluaciones/v3.md")
        with self.assertRaises(ValueError):
            add_evaluation(self.root,"v3","E09","parcial",
                           "evaluaciones/v3.md",technical=float("nan"))

if __name__=="__main__":
    unittest.main()
