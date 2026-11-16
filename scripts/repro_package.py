#!/usr/bin/env python3
"""Comprueba y empaqueta solo los archivos declarados relevantes para el TFG.

No ejecuta código ni certifica reproducción. La prueba sustantiva la hace el
estudiante en una carpeta independiente, siguiendo README_REPRODUCCION.md.
"""
import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
import re
from pathlib import Path

MANIFEST = "07_entrega/ARCHIVOS_INCLUIDOS.txt"
README = "07_entrega/README_REPRODUCCION.md"
DISALLOWED = {".tfg", "06_evaluaciones", "__pycache__", ".git"}
# Patrón prudente, orientado a nombres; no sustituye revisión manual del contenido.
SENSITIVE_PARTS = {"credenciales", "credentials", "secret", "secrets", "password",
                   "passwords", "token", "tokens", "api_key", "apikey",
                   "private", "privado", "confidential", "confidencial",
                   "restringido", "restricted", "descartado", "discarded",
                   "backup", "backups", "borrador", "draft", "old", "restringidos", "restringidas", "descartados", "descartadas", "confidenciales", "privados", "privadas"}
SECRET_EXTENSIONS = {".pem", ".key", ".p12", ".pfx"}
MAX_FILES = 2000
MAX_BYTES = 2_000_000_000

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def entries(root):
    root = root.resolve()
    manifest = root / MANIFEST
    if not manifest.is_file() or manifest.is_symlink():
        raise ValueError(f"Falta {MANIFEST}")
    names = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        name = line.strip()
        if not name or name.startswith("#"):
            continue
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or not relative.parts:
            raise ValueError(f"Ruta no permitida: {name}")
        if any(part in DISALLOWED or part.startswith(".") for part in relative.parts):
            raise ValueError(f"No incluir carpetas privadas, ocultas o históricas: {name}")
        fragments = [part.lower() for part in relative.parts]
        lexical = set()
        for part in fragments:
            lexical.update(x for x in re.split(r"[^a-z0-9áéíóúñ]+", part) if x)
        if (lexical & SENSITIVE_PARTS or {"api", "key"}.issubset(lexical)
                or relative.suffix.lower() in SECRET_EXTENSIONS):
            raise ValueError(f"Posibles datos privados, descartados o credenciales: {name}")
        path = root / relative
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"Enlace o salida de la carpeta: {name}")
        if not path.is_file():
            raise ValueError(f"No existe el archivo declarado: {name}")
        names.append(relative.as_posix())
    if not names or len(names) > MAX_FILES:
        raise ValueError("La lista debe contener entre 1 y 2000 archivos")
    if len(names) != len(set(names)):
        raise ValueError("Hay archivos repetidos en la lista")
    if README not in names:
        raise ValueError(f"Debe incluirse {README}")
    if not any(Path(n).parts[0] == "07_entrega" and n.lower().endswith(".pdf") for n in names):
        raise ValueError("Falta incluir un manuscrito final PDF en 07_entrega/")
    if sum((root / n).stat().st_size for n in names) > MAX_BYTES:
        raise ValueError("El paquete supera 2 GB")
    return names

def check(root):
    paths = entries(root)
    files = [{"path": name, "sha256": sha256(root / name),
              "size_bytes": (root / name).stat().st_size} for name in paths]
    excluded = []
    for directory in ("03_datos", "04_analisis", "05_manuscrito", "07_entrega"):
        folder = root / directory
        if folder.is_dir():
            excluded.extend(str(p.relative_to(root)) for p in folder.rglob("*")
                            if p.is_file() and not p.is_symlink()
                            and str(p.relative_to(root)) not in paths)
    return {"files": files, "total_files": len(files),
            "excluded_candidates": sorted(excluded)[:100],
            "excluded_candidates_truncated": len(excluded) > 100,
            "warning": "Revise manualmente datos restringidos, credenciales y dependencias omitidas. "
                       "Esta lista no asegura que todos los archivos necesarios estén incluidos.",
            "message": "Validación estructural; NO se han reproducido resultados."}

def build(root, output):
    root = root.resolve()
    output = output.resolve()
    if output.exists():
        raise ValueError("El ZIP de salida ya existe; no se sobrescribe")
    data = check(root)
    if output.is_relative_to(root):
        raise ValueError("Guardar el ZIP fuera del proyecto, para evitar confusiones")
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as z:
            for item in data["files"]:
                z.write(root / item["path"], item["path"])
            z.writestr("MANIFIESTO_SHA256.json",
                       json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        # Confirmar que la extracción de un paquete nuevo conserva los bytes.
        with tempfile.TemporaryDirectory(prefix="tfg_zip_check_") as tmp:
            with zipfile.ZipFile(output) as z:
                z.extractall(tmp)
            for item in data["files"]:
                target = Path(tmp) / item["path"]
                if sha256(target) != item["sha256"]:
                    raise ValueError("El ZIP no conserva los archivos originales")
    except Exception:
        output.unlink(missing_ok=True)
        raise
    return {"zip": str(output), "included_files": data["total_files"],
            "message": "Integridad de archivos comprobada. El estudiante debe ejecutar la reproducción por separado."}

def main():
    p = argparse.ArgumentParser(description="Paquete final reproducible de TFG")
    sub = p.add_subparsers(dest="action", required=True)
    a = sub.add_parser("check"); a.add_argument("project")
    a = sub.add_parser("build"); a.add_argument("project"); a.add_argument("output")
    args = p.parse_args()
    try:
        result = check(Path(args.project)) if args.action == "check" else build(Path(args.project), Path(args.output))
    except (ValueError, OSError, zipfile.BadZipFile) as ex:
        p.exit(2, f"Error: {ex}\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
