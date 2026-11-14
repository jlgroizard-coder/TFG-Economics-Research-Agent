#!/usr/bin/env python3
"""Herramienta local de expedientes TFG. No puntúa investigaciones ni sube datos."""
import argparse
import hashlib
import json
from pathlib import Path

STATES = {"vigente_verificada","vigente_no_verificada","no_aportada_ahora",
          "desactualizada","refutada","pendiente"}
CRITERIA = "ABCDEFGH"

def inside(base, rel):
    path = (base / rel).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError("Ruta fuera del expediente privado")
    return path

def open_case(base):
    path = inside(base, "expediente.json")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("schema_version") != "0.2":
        raise ValueError("Versión del esquema incorrecta")
    return obj

def save_case(base, obj):
    path = inside(base, "expediente.json")
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

def init_case(base, student_id):
    base = base.expanduser().resolve()
    if base.exists() and any(base.iterdir()):
        raise ValueError("El directorio ya existe y no está vacío: no se sobrescribe")
    base.mkdir(parents=True, exist_ok=True)
    for name in ("00_admin","01_propuesta","02_literatura","03_datos_raw",
                 "04_datos_work","05_codigo","06_resultados","07_texto",
                 "08_presentacion","09_entrega","evaluaciones"):
        (base / name).mkdir(exist_ok=True)
    obj = {"schema_version":"0.2","student_id":student_id,
           "course":"2026-2027","modality":"empirico","stage":"E01",
           "research_question":"","artifacts":[],"evidence":[],"evaluations":[]}
    save_case(base,obj)
    (base/"decisiones.md").write_text("# Registro privado de decisiones\n",encoding="utf-8")
    return base

def add_artifact(base, rel, kind, version):
    obj=open_case(base)
    path=inside(base,rel)
    if not path.is_file():
        raise ValueError("Archivo no encontrado")
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    entry={"path":rel,"kind":kind,"version":version,"sha256":sha}
    obj["artifacts"].append(entry)
    save_case(base,obj)
    return entry

def evidence(base, criterion, status, rel, version, note):
    if criterion not in CRITERIA or status not in STATES:
        raise ValueError("Criterio o estado inválido")
    obj=open_case(base)
    inside(base,rel)
    row={"criterion":criterion,"status":status,
         "artifact_path":rel,"version":version,"note":note}
    obj["evidence"].append(row)
    save_case(base,obj)
    return row

def add_evaluation(base, version, stage, scope, report_path, complete=None, stage_score=None, technical=None, consistency=None):
    if scope not in ("expediente_completo", "parcial", "provisional"):
        raise ValueError("Alcance desconocido")
    if stage not in {f"E{i:02d}" for i in range(1,15)}:
        raise ValueError("Etapa E01–E14 inválida")
    if scope != "expediente_completo" and (complete is not None or stage_score is not None):
        raise ValueError("Una evaluación parcial/provisional no puede registrar notas científicas globales")
    scores=(complete,stage_score,technical,consistency)
    if any(x is not None and not 0 <= x <= 10 for x in scores):
        raise ValueError("Notas fuera del intervalo 0–10")
    path=inside(base,report_path)
    if not path.is_file():
        raise ValueError("Informe de evaluación no encontrado")
    obj=open_case(base)
    if any(x["version"]==version and x["report_path"]==report_path for x in obj["evaluations"]):
        raise ValueError("Evaluación ya registrada")
    row={"version":version,"stage":stage,"scope":scope,"report_path":report_path,
         "complete_score":complete,"stage_score":stage_score,
         "technical_score":technical,"consistency_score":consistency}
    obj["evaluations"].append(row)
    save_case(base,obj)
    return row

def audit(base):
    obj=open_case(base)
    found=[]
    for x in obj["artifacts"]:
        path=inside(base,x["path"])
        exists=path.is_file()
        same=exists and hashlib.sha256(path.read_bytes()).hexdigest()==x.get("sha256")
        found.append({"path":x["path"],"version":x["version"],
                      "exists":exists,"unchanged":same})
    return {"student_id":obj["student_id"],"artifacts":found,
            "evidence_status_counts":{s:sum(x["status"]==s for x in obj["evidence"]) for s in sorted(STATES)},
            "warning":"Solo archivos y hashes; NO demuestra vigencia científica ni reproducción."}

def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest="action",required=True)
    p=sub.add_parser("init"); p.add_argument("folder");p.add_argument("--id",default="SEUDONIMO_LOCAL")
    p=sub.add_parser("add-artifact");p.add_argument("folder");p.add_argument("path");p.add_argument("--kind",required=True,
        choices=["propuesta","literatura","teoria","datos","codigo","resultados","manuscrito","reproduccion","otros"]);p.add_argument("--version",required=True)
    p=sub.add_parser("add-evidence");p.add_argument("folder");p.add_argument("--criterion",required=True,choices=list(CRITERIA))
    p.add_argument("--status",required=True,choices=sorted(STATES));p.add_argument("--path",required=True)
    p.add_argument("--version",required=True);p.add_argument("--note",required=True)
    p=sub.add_parser("add-evaluation")
    p.add_argument("folder");p.add_argument("--version",required=True)
    p.add_argument("--stage",required=True)
    p.add_argument("--scope",required=True,choices=["expediente_completo","parcial","provisional"])
    p.add_argument("--report",required=True)
    p.add_argument("--complete",type=float);p.add_argument("--stage-score",type=float)
    p.add_argument("--technical",type=float);p.add_argument("--consistency",type=float)
    p=sub.add_parser("audit");p.add_argument("folder")
    args=ap.parse_args()
    base=Path(args.folder).expanduser()
    if args.action=="init":res={"created":str(init_case(base,args.id))}
    elif args.action=="add-artifact":res=add_artifact(base,args.path,args.kind,args.version)
    elif args.action=="add-evidence":res=evidence(base,args.criterion,args.status,args.path,args.version,args.note)
    elif args.action=="add-evaluation":res=add_evaluation(base,args.version,args.stage,args.scope,args.report,args.complete,args.stage_score,args.technical,args.consistency)
    else:res=audit(base)
    print(json.dumps(res,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
