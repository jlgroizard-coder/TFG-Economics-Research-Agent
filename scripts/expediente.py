#!/usr/bin/env python3
"""Expedientes privados TFG: registro, integridad y revisión. NO asigna notas."""
import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

STATES = {"vigente_verificada", "vigente_no_verificada", "no_aportada_ahora",
          "desactualizada", "refutada", "pendiente"}
CRITERIA = "ABCDEFGH"
KINDS = ("propuesta", "literatura", "teoria", "datos", "codigo", "resultados",
         "manuscrito", "reproduccion", "otros")
STAGES = {f"E{i:02d}" for i in range(1, 15)}
# Heurística conservadora: el agente/docente decide vigencia definitiva.
DEPENDENCIES = {
    "pregunta": set(CRITERIA), "ambito": set("ABCDEFGH"),
    "periodo": set("DEFGH"), "datos": set("DEFGH"),
    "variables": set("CDEFGH"), "metodo": set("CDFGH"),
    "hipotesis": set("BCDFH")
}

def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def inside(base, rel):
    rel = Path(rel)
    if rel.is_absolute():
        raise ValueError("No se permiten rutas absolutas")
    path = (base / rel).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError("Ruta fuera del expediente privado")
    return path

def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def open_case(base):
    obj = json.loads(inside(base, "expediente.json").read_text(encoding="utf-8"))
    if obj.get("schema_version") != "0.2":
        raise ValueError("Esquema desconocido")
    obj.setdefault("decisions", [])
    return obj

def mark_scores_stale(obj, reason):
    for row in obj["evaluations"]:
        if row.get("scope") == "expediente_completo" and not row.get("revoked_at") and not row.get("stale_at"):
            row["stale_at"] = now()
            row["stale_reason"] = reason

def artifact_health(base, a):
    path = inside(base, a["path"])
    if not path.is_file():
        return "no_aportada_ahora"
    if not a.get("sha256") or hash_file(path) != a["sha256"]:
        return "desactualizada"
    return "intacta"

def historic_integrity_problems(base, obj):
    """New labels may not hide missing/modified previously verified evidence."""
    index = {(a["path"], a["version"]): a for a in obj["artifacts"]}
    verified = {(r["criterion"], r["artifact_path"], r["version"])
                for r in obj["evidence"] if r["status"] == "vigente_verificada"}
    problems = []
    for criterion, path, version in sorted(verified):
        a = index.get((path, version))
        state = artifact_health(base, a) if a else "sin_registro"
        if state != "intacta":
            problems.append(f"{criterion}: {path} ({version}) {state}")
    return problems

def confirmed_status(base, obj, row):
    a = next((a for a in reversed(obj["artifacts"])
              if a["path"] == row["artifact_path"] and a["version"] == row["version"]), None)
    if a:
        health = artifact_health(base, a)
        if health != "intacta":
            return health
    else:
        historical = [r for r in obj["evidence"]
                      if r["criterion"] == row["criterion"]
                      and r["artifact_path"] == row["artifact_path"]
                      and r["status"] == "vigente_verificada"]
        for record in historical:
            prior = next((a for a in obj["artifacts"]
                          if a["path"] == record["artifact_path"]
                          and a["version"] == record["version"]), None)
            if prior:
                health = artifact_health(base, prior)
                if health != "intacta":
                    return health
        if row["status"] in ("vigente_verificada", "vigente_no_verificada"):
            path = inside(base, row["artifact_path"])
            return "no_aportada_ahora" if not path.is_file() else "desactualizada"
    return row["status"]

def migrate_legacy_reports(base, reason):
    """Establish CURRENT integrity baseline; cannot attest old history."""
    obj = open_case(base)
    changed = []
    for row in obj["evaluations"]:
        if row.get("report_sha256"):
            continue
        path = inside(base, row["report_path"])
        if not path.is_file():
            continue
        row["report_sha256"] = hash_file(path)
        row["legacy_baseline_at"] = now()
        row["legacy_baseline_note"] = reason
        changed.append(row["report_path"])
    if changed:
        save_case(base, obj)
    return {"baselines_created": changed,
            "warning": "La huella acredita solo el contenido actual; NO demuestra integridad histórica."}


    inside(base, "expediente.json").write_text(
        json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def save_case(base, obj):
    inside(base, "expediente.json").write_text(
        json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def init_case(base, student_id):
    base = base.expanduser().resolve()
    if base.exists() and any(base.iterdir()):
        raise ValueError("El directorio no está vacío; no se sobrescribe")
    base.mkdir(parents=True, exist_ok=True)
    for name in ("00_admin", "01_propuesta", "02_literatura", "03_datos_raw",
                 "04_datos_work", "05_codigo", "06_resultados", "07_texto",
                 "08_presentacion", "09_entrega", "evaluaciones"):
        (base / name).mkdir(exist_ok=True)
    save_case(base, {"schema_version": "0.2", "student_id": student_id,
                     "course": "2026-2027", "modality": "empirico", "stage": "E01",
                     "research_question": "", "artifacts": [], "evidence": [],
                     "evaluations": [], "decisions": []})
    (base / "decisiones.md").write_text("# Registro privado de decisiones\n", encoding="utf-8")
    return base

def add_artifact(base, rel, kind, version):
    if kind not in KINDS:
        raise ValueError("Tipo de artefacto desconocido")
    obj = open_case(base)
    path = inside(base, rel)
    if not path.is_file():
        raise ValueError("Archivo no encontrado")
    row = {"path": rel, "kind": kind, "version": version,
           "sha256": hash_file(path), "checked_at": now()}
    if any(x["path"] == rel and x["version"] == version for x in obj["artifacts"]):
        raise ValueError("La misma versión de artefacto ya está registrada; crea otra versión")
    obj["artifacts"].append(row)
    mark_scores_stale(obj, "Se registró un nuevo artefacto")
    save_case(base, obj)
    return row

def add_evidence(base, criterion, status, rel, version, note):
    if criterion not in CRITERIA or status not in STATES:
        raise ValueError("Criterio o estado inválido")
    obj = open_case(base)
    path = inside(base, rel)
    row = {"criterion": criterion, "status": status, "artifact_path": rel,
           "version": version, "note": note, "checked_at": now()}
    if status == "vigente_verificada":
        linked = [a for a in obj["artifacts"] if a["path"] == rel and a["version"] == version]
        if not linked or not path.is_file() or hash_file(path) != linked[-1].get("sha256"):
            raise ValueError("Para validar evidencia hay que registrar y conservar el archivo exacto")
    obj["evidence"].append(row)
    mark_scores_stale(obj, "Cambió el registro de evidencia")
    save_case(base, obj)
    return row

def effective_evidence(base, obj):
    # Última entrada para cada pareja criterio+artefacto, NO recuentos históricos acumulados.
    latest = {}
    for row in obj["evidence"]:
        latest[(row["criterion"], row["artifact_path"])] = dict(row)
    for row in latest.values():
        status = confirmed_status(base, obj, row)
        if status != row["status"]:
            row["alert"] = "Estado comprobado por integridad de archivo, no por su etiqueta"
            row["status"] = status
    return list(latest.values())

def add_decision(base, change, detail, value=None):
    if change not in DEPENDENCIES:
        raise ValueError("Cambio no reconocido")
    obj = open_case(base)
    affected = sorted(DEPENDENCIES[change])
    # Se invalida conservadoramente la evidencia previa; requiere revisión docente.
    current = effective_evidence(base, obj)
    affected_rows = []
    for row in current:
        if row["criterion"] in affected and row["status"] in ("vigente_verificada", "vigente_no_verificada"):
            obj["evidence"].append({
                "criterion": row["criterion"], "status": "desactualizada",
                "artifact_path": row["artifact_path"], "version": row["version"],
                "note": "Revalidación requerida por cambio de "+change+": "+detail,
                "checked_at": now()})
            affected_rows.append(row["criterion"] + ":" + row["artifact_path"])
    decision = {"change": change, "detail": detail, "affected_criteria": affected,
                "time": now()}
    if change == "pregunta" and value is not None:
        obj["research_question"] = value
    obj["decisions"].append(decision)
    mark_scores_stale(obj, "Nueva decisión sobre "+change)
    save_case(base, obj)
    with inside(base, "decisiones.md").open("a", encoding="utf-8") as f:
        f.write("\n- "+decision["time"]+" | "+change+" | "+detail+"\n")
    return {"decision": decision, "invalidated_evidence": affected_rows}

def add_evaluation(base, version, stage, scope, report_path,
                   complete=None, stage_score=None, technical=None, consistency=None):
    if scope not in ("expediente_completo", "parcial", "provisional"):
        raise ValueError("Alcance desconocido")
    if stage not in STAGES:
        raise ValueError("Etapa E01–E14 inválida")
    scores = (complete, stage_score, technical, consistency)
    if any(x is not None and (not math.isfinite(x) or x < 0 or x > 10) for x in scores):
        raise ValueError("Puntuación fuera de intervalo o no finita")
    if scope != "expediente_completo" and (complete is not None or stage_score is not None):
        raise ValueError("No asignar notas globales en evaluaciones provisionales o parciales")
    path = inside(base, report_path)
    if not path.is_file():
        raise ValueError("Informe no encontrado")
    obj = open_case(base)
    if scope == "expediente_completo":
        if complete is None or stage_score is None:
            raise ValueError("Evaluación global requiere ambas notas científicas")
        current = effective_evidence(base, obj)
        by_criterion = {c: [x for x in current if x["criterion"] == c] for c in CRITERIA}
        # Se admiten criterios con 0 puntos, solo si están documentados explícitamente
        # como ausencia acreditada y no como archivo perdido.
        problems = []
        for criterion, rows in by_criterion.items():
            if not rows:
                problems.append(criterion + " sin evidencia documentada")
            if any(x["status"] in ("no_aportada_ahora", "desactualizada") for x in rows):
                problems.append(criterion + " con evidencia inaccesible/desactualizada")
        problems.extend(historic_integrity_problems(base, obj))
        if problems:
            raise ValueError("No se puede emitir nota global: " + "; ".join(problems))
    if any(x["version"] == version and x["report_path"] == report_path
           and not x.get("revoked_at") for x in obj["evaluations"]):
        raise ValueError("Evaluación activa duplicada")
    row = {"version": version, "stage": stage, "scope": scope,
           "report_path": report_path, "report_sha256": hash_file(path),
           "recorded_at": now(), "complete_score": complete,
           "stage_score": stage_score, "technical_score": technical,
           "consistency_score": consistency}
    obj["evaluations"].append(row)
    save_case(base, obj)
    return row

def revoke_evaluation(base, version, report_path, reason):
    obj = open_case(base)
    matches = [x for x in obj["evaluations"] if x["version"] == version
               and x["report_path"] == report_path and not x.get("revoked_at")]
    if len(matches) != 1:
        raise ValueError("No hay una evaluación activa única que anular")
    matches[0]["revoked_at"] = now()
    matches[0]["revoke_reason"] = reason
    save_case(base, obj)
    return {"revoked": version, "report": report_path, "reason": reason}

def audit(base):
    obj = open_case(base)
    artifacts = []
    for a in obj["artifacts"]:
        path = inside(base, a["path"])
        exists = path.is_file()
        unchanged = exists and hash_file(path) == a.get("sha256")
        artifacts.append({"path": a["path"], "version": a["version"],
                          "exists": exists, "unchanged": unchanged,
                          "suggested_status": "vigente_verificada" if unchanged else
                              "no_aportada_ahora" if not exists else "desactualizada"})
    effective = effective_evidence(base, obj)
    reports = []
    integrity_alert = bool(historic_integrity_problems(base, obj))
    for x in obj["evaluations"]:
        path = inside(base, x["report_path"])
        reports.append({"version": x["version"], "report_path": x["report_path"],
                        "intact": path.is_file() and hash_file(path) == x.get("report_sha256"),
                        "revoked": bool(x.get("revoked_at")),
                        "obsolete": bool(x.get("stale_at")) or
                                    (integrity_alert and x.get("scope") == "expediente_completo"),
                        "legacy_baseline_only": bool(x.get("legacy_baseline_at"))})
    return {"student_id": obj["student_id"], "artifacts": artifacts,
            "historic_integrity_problems": historic_integrity_problems(base, obj),
            "effective_evidence": effective,
            "effective_status_counts": {s: sum(x["status"] == s for x in effective)
                                        for s in sorted(STATES)},
            "evaluation_reports": reports,
            "warning": "Auditoría de archivos/estados; NO verifica la vigencia científica por sí sola."}

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="action", required=True)
    p = sub.add_parser("init"); p.add_argument("folder"); p.add_argument("--id", default="SEUDONIMO_LOCAL")
    p = sub.add_parser("add-artifact"); p.add_argument("folder"); p.add_argument("path")
    p.add_argument("--kind", required=True, choices=KINDS); p.add_argument("--version", required=True)
    p = sub.add_parser("add-evidence"); p.add_argument("folder")
    p.add_argument("--criterion", required=True, choices=list(CRITERIA))
    p.add_argument("--status", required=True, choices=sorted(STATES))
    p.add_argument("--path", required=True); p.add_argument("--version", required=True)
    p.add_argument("--note", required=True)
    p = sub.add_parser("add-decision"); p.add_argument("folder")
    p.add_argument("--change", required=True, choices=sorted(DEPENDENCIES))
    p.add_argument("--detail", required=True); p.add_argument("--value")
    p = sub.add_parser("set-question"); p.add_argument("folder")
    p.add_argument("--question", required=True); p.add_argument("--reason", required=True)
    p = sub.add_parser("add-evaluation"); p.add_argument("folder")
    p.add_argument("--version", required=True); p.add_argument("--stage", required=True)
    p.add_argument("--scope", required=True, choices=["expediente_completo", "parcial", "provisional"])
    p.add_argument("--report", required=True); p.add_argument("--complete", type=float)
    p.add_argument("--stage-score", type=float); p.add_argument("--technical", type=float)
    p.add_argument("--consistency", type=float)
    p = sub.add_parser("revoke-evaluation"); p.add_argument("folder")
    p.add_argument("--version", required=True); p.add_argument("--report", required=True)
    p.add_argument("--reason", required=True)
    p = sub.add_parser("migrate-legacy"); p.add_argument("folder")
    p.add_argument("--reason", required=True)
    p = sub.add_parser("audit"); p.add_argument("folder")
    args = ap.parse_args()
    base = Path(args.folder).expanduser()
    if args.action == "init":
        result = {"created": str(init_case(base, args.id))}
    elif args.action == "add-artifact":
        result = add_artifact(base, args.path, args.kind, args.version)
    elif args.action == "add-evidence":
        result = add_evidence(base, args.criterion, args.status, args.path, args.version, args.note)
    elif args.action == "add-decision":
        result = add_decision(base, args.change, args.detail, args.value)
    elif args.action == "set-question":
        result = add_decision(base, "pregunta", args.reason, args.question)
    elif args.action == "add-evaluation":
        result = add_evaluation(base, args.version, args.stage, args.scope, args.report,
                                args.complete, args.stage_score, args.technical, args.consistency)
    elif args.action == "revoke-evaluation":
        result = revoke_evaluation(base, args.version, args.report, args.reason)
    elif args.action == "migrate-legacy":
        result = migrate_legacy_reports(base, args.reason)
    else:
        result = audit(base)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
