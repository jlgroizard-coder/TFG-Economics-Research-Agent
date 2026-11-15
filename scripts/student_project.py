#!/usr/bin/env python3
"""Proyecto local sencillo TFG UIB: crear, capturar entrega y mostrar estado.

La conversación con el tutor activa estos comandos, nunca se exigen al estudiante.
Solo Python estándar; los archivos y sus copias permanecen en la carpeta local.
"""
import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

FOLDERS = ("01_propuesta", "02_literatura", "03_datos", "04_analisis",
           "05_manuscrito", "06_evaluaciones", "07_entrega")
HIDDEN = ".tfg"
GUIDE = """# Mi TFG de Economía · UIB

**Esta es tu carpeta de trabajo.** Puedes editar tus archivos con Word, LibreOffice,
un editor de texto o el programa con el que estés familiarizado.

## Cómo empezar

Escribe al Tutor IA: **«Quiero empezar mi TFG de Economía; ayúdame con E01»**.
Para entregar un borrador: **«He actualizado este documento; evalúalo»**.
Para continuar: **«¿Qué tengo pendiente en mi TFG?»**.

El tutor puede orientarte y darte **calificaciones formativas** cuando se lo pidas;
**no son notas oficiales ni sustituyen las del profesor o tribunal de la UIB**.
Las propuestas deben ser aprobadas académicamente por tu profesor.

## Buenas prácticas

- Formula una pregunta económica clara y viable; avanza por entregas.
- Lee y comprueba los originales de los artículos; no cites referencias inventadas.
- Entiende y justifica los mecanismos y resultados que presentas.
- Usa la IA como apoyo, nunca para sustituir tu trabajo intelectual.
- Conserva las fuentes de datos y los pasos para reproducir tablas y gráficos.
- Distingue asociación de causalidad, y describe las limitaciones.
- Pide evaluaciones después de mejoras verificables; una nota no es un objetivo en sí.
- Mantén copia de seguridad y no compartas datos personales o restringidos.

## Carpetas

- 01_propuesta: preguntas, objetivos y propuesta
- 02_literatura: bibliografía y fichas
- 03_datos: fuentes y documentación
- 04_analisis: cálculos, programas, tablas y gráficos
- 05_manuscrito: borradores
- 06_evaluaciones: informes que podrás volver a leer
- 07_entrega: documentos finales

La carpeta oculta .tfg contiene versiones entregadas, instrucciones del tutor
y registros técnicos; **no hace falta modificarla**.

## Próximo paso

**E01:** prepara *dos preguntas de investigación* candidatas. Para cada una explica
por qué es económica, cuál es el mecanismo que te interesa y qué evidencia
podrías utilizar (1–2 páginas en total). Pide al tutor que te ayude a acotarlas.
La guía docente y la dirección académica de la UIB prevalecen siempre.
"""

ROOT_CLAUDE = """# Tutor IA del TFG Economía — Proyecto local del estudiante

Lee antes de actuar:
- .tfg/agent/instructions-portable.md
- .tfg/agent/references/rubrica.md
- .tfg/agent/references/protocolo-evaluacion.md
- .tfg/agent/references/guia-tfg-uib-2026-27.md
- LEEME_PRIMERO.md

Eres tutor conversacional, no un gestor de terminal para el estudiante.
Responde de forma breve, rigurosa y pedagógica. Nadie necesita comandos.
El estudiante puede autoevaluarse cuando quiera: todas las notas son
informativas, nunca oficiales, sin exigir aprobación previa del profesor.
Guarda los informes en 06_evaluaciones/ con nombres nuevos.
Si tienes permiso local para leer archivos, antes de evaluar un borrador
captúralo con: python3 .tfg/tools/student_project.py submit . RUTA_RELATIVA
(la ejecución la haces tú; no pidas al alumno escribirla).
No edites el documento original al capturarlo ni lo sobrescribas sin permiso.
Si no hay acceso local, di que no se puede guardar automáticamente.
No uses begin-revision ni scripts/expediente.py para las entregas sencillas.
No presupongas que una entrega fue verificada científicamente solo porque
su copia se guardó con hash. Lee la evidencia real y explica límites.
"""

ROOT_AGENTS = ROOT_CLAUDE

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def utcnow():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def safe_file(root, name):
    rel = Path(name)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("Selecciona un archivo dentro de la carpeta del TFG")
    target = (root / rel).resolve()
    if (not target.is_relative_to(root.resolve()) or
        (rel.parts and rel.parts[0] in (HIDDEN, "06_evaluaciones"))):
        raise ValueError("No se permiten archivos internos ni fuera del TFG")
    if not target.is_file():
        raise ValueError("No se encuentra el archivo de trabajo")
    return target, str(rel)

def find_sources():
    # En el repositorio de desarrollo, los textos de referencia son locales.
    parent = Path(__file__).resolve().parents[1]
    if (parent / "references" / "rubrica.md").is_file():
        return parent
    return None

def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def init(root):
    root = root.expanduser().resolve()
    if root.exists() and any(root.iterdir()):
        raise ValueError("La carpeta no está vacía. Selecciona una carpeta nueva y privada.")
    source = find_sources()
    if not source:
        raise ValueError("Necesito el repositorio del agente para crear el proyecto.")
    root.mkdir(parents=True, exist_ok=True)
    for folder in FOLDERS:
        (root / folder).mkdir(exist_ok=True)
    private = root / HIDDEN
    (private / "entregas").mkdir(parents=True, exist_ok=True)
    (private / "agent" / "references").mkdir(parents=True, exist_ok=True)
    (private / "tools").mkdir(exist_ok=True)
    shutil.copy2(Path(__file__).resolve(), private / "tools" / "student_project.py")
    for name in ("instructions-portable.md",):
        shutil.copy2(source / name, private / "agent" / name)
    for name in ("rubrica.md", "protocolo-evaluacion.md", "guia-tfg-uib-2026-27.md",
                 "indicadores-tecnicos.md", "expediente-y-continuidad.md"):
        shutil.copy2(source / "references" / name,
                     private / "agent" / "references" / name)
    (private / "agent" / "templates").mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / "templates" / "informe-evaluacion.md",
                 private / "agent" / "templates" / "informe-evaluacion.md")
    write_text(root / "LEEME_PRIMERO.md", GUIDE)
    write_text(root / "CLAUDE.md", ROOT_CLAUDE)
    write_text(root / "AGENTS.md", ROOT_AGENTS)
    write_text(root / "01_propuesta" / "E01_dos_preguntas.md",
               "# E01 — Mis dos preguntas de investigación\n\n"
               "## Pregunta 1\n\n- Pregunta:\n- Relevancia económica:\n"
               "- Mecanismo esperado:\n- Datos o fuentes posibles:\n\n"
               "## Pregunta 2\n\n- Pregunta:\n- Relevancia económica:\n"
               "- Mecanismo esperado:\n- Datos o fuentes posibles:\n\n"
               "## Pregunta que prefiero y por qué\n\n")
    write_text(private / "registro.json",
               json.dumps({"version": "0.3-mvp", "created_at": utcnow(),
                           "submissions": []}, ensure_ascii=False, indent=2) + "\n")
    return {"project": str(root), "next_step": "Completar E01_dos_preguntas.md",
            "hint": "Abre esta carpeta en tu asistente con acceso a archivos; no requiere Git."}

def submit(root, relative_path):
    root = root.expanduser().resolve()
    state_file = root / HIDDEN / "registro.json"
    if not state_file.is_file():
        raise ValueError("No es un proyecto de TFG inicializado")
    src, rel = safe_file(root, relative_path)
    state = json.loads(state_file.read_text(encoding="utf-8"))
    old = state["submissions"]
    sha = digest(src)
    if old and old[-1]["source_path"] == rel and old[-1]["sha256"] == sha:
        return {"status": "sin_cambios", "submission": old[-1],
                "note": "No ha cambiado desde la última entrega de ese documento."}
    matches = [e for e in old if e["source_path"] == rel]
    if matches and matches[-1]["sha256"] == sha:
        return {"status": "sin_cambios", "submission": matches[-1],
                "note": "Esta versión del documento ya estaba guardada."}
    number = len(old) + 1
    snapshot = (root / HIDDEN / "entregas" / f"{number:04d}_{sha[:10]}" / src.name)
    snapshot.parent.mkdir(parents=True, exist_ok=False)
    shutil.copy2(src, snapshot)
    if digest(snapshot) != sha:
        snapshot.unlink(missing_ok=True)
        raise ValueError("Error al verificar la copia; no se registra la entrega")
    entry = {"number": number, "source_path": rel,
             "snapshot": str(snapshot.relative_to(root)),
             "sha256": sha, "saved_at": utcnow()}
    old.append(entry)
    state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    return {"status": "guardado", "submission": entry,
            "note": "Copia guardada. No implica revisión académica ni evaluación automática."}

def status(root):
    root = root.expanduser().resolve()
    file = root / HIDDEN / "registro.json"
    if not file.is_file():
        raise ValueError("No se encuentra un proyecto inicializado")
    state = json.loads(file.read_text(encoding="utf-8"))
    recent = state["submissions"][-3:]
    # Indicar modificaciones sin convertir la ausencia en juicio científico.
    for entry in recent:
        path = root / entry["source_path"]
        entry = entry
        entry["working_file_changed"] = not path.is_file() or digest(path) != entry["sha256"]
    return {"project": str(root), "submissions": len(state["submissions"]),
            "last_submissions": recent,
            "next_step": "Consulta LEEME_PRIMERO.md y la última evaluación formativa."}

def main():
    parser = argparse.ArgumentParser(description="Gestión interna de proyecto local TFG")
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("init"); p.add_argument("project")
    p = sub.add_parser("submit"); p.add_argument("project"); p.add_argument("file")
    p = sub.add_parser("status"); p.add_argument("project")
    a = parser.parse_args()
    try:
        result = (init(Path(a.project)) if a.action == "init" else
                  submit(Path(a.project), a.file) if a.action == "submit" else
                  status(Path(a.project)))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
