# Publicación, pruebas y mantenimiento

Repositorio: https://github.com/jlgroizard-coder/TFG-Economics-Research-Agent

1. Confirmar que el repositorio es público y que no contiene expedientes ni datos de estudiantes.
2. Probar con Claude Code (`CLAUDE.md` + `.claude/skills/`) y Codex (`AGENTS.md` + `.agents/skills/`).
3. Ejecutar pruebas: `python -m unittest discover -s scripts -p 'test_*.py'`.
4. Probar tres expedientes ficticios: propuesta deficiente, propuesta correcta y trabajo empírico con fallos de reproducción.
5. Comparar puntuaciones entre modelos y revisar divergencias académicamente.
6. Registrar cambios en rúbrica y crear una release `v0.1.0` tras la validación docente.
7. No publicar trabajos personales ni documentos oficiales con derechos de redistribución no aclarados.

Esta versión no ofrece una web de conversación: distribuye habilidades para asistentes compatibles.
