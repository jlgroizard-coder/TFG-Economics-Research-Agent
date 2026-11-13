#!/usr/bin/env python3
"""Auditoría estática de archivos, NO ejecución ni reproducibilidad científica."""
import argparse
import json
from pathlib import Path

def audit(root, mode):
    files=[p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    lower=lambda p: str(p.relative_to(root)).lower()
    checks={
        "readme":any(p.name.lower().startswith("readme") for p in files),
        "manuscrito":any(p.suffix.lower() in (".pdf",".docx",".tex",".md") and any(k in lower(p) for k in ("manuscrito","tesis","tfg","thesis")) for p in files),
        "fuentes_documentadas":any(any(k in lower(p) for k in ("fuente","data","readme")) for p in files),
        "codigo":any(p.suffix.lower() in (".py",".r",".do",".ipynb",".jl",".m") for p in files),
        "resultados":any(any(k in lower(p) for k in ("resultado","output","figure","table")) for p in files)
    }
    if mode!="empirico":
        checks["codigo"]="no_aplica_si_no_hay_programas"
    return {
        "tipo":"auditoria_estructural_no_reproduccion",
        "ruta":str(root),
        "modalidad":mode,
        "numero_archivos":len(files),
        "comprobaciones":checks,
        "advertencias":[k for k,v in checks.items() if v is False],
        "reproduccion_ejecutada":False
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("ruta")
    parser.add_argument("--modalidad",choices=["empirico","teorico","revision"],default="empirico")
    args=parser.parse_args()
    root=Path(args.ruta).expanduser().resolve()
    if not root.is_dir(): parser.error("Directorio inexistente")
    result=audit(root,args.modalidad)
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 2 if result["advertencias"] else 0

if __name__=="__main__":
    raise SystemExit(main())
