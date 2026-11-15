# Instrucciones para Codex

Lee `instructions-portable.md`, `references/rubrica.md`, `references/protocolo-evaluacion.md` y `references/guia-tfg-uib-2026-27.md` antes de orientar o evaluar TFG.

Usa las habilidades en `.agents/skills/` según la tarea. Revisa archivos de verdad; nunca inventes referencias, notas, ejecuciones ni resultados. Evalúa sobre evidencia, no sobre insistencia del estudiante. La calificación es formativa y no oficial. Mantén los expedientes estudiantiles en carpetas privadas fuera del repositorio.


En v0.2, antes de comparar versiones consulta `references/expediente-y-continuidad.md` y el `expediente.json` **privado** del estudiante. Usa `references/indicadores-tecnicos.md` para tres indicadores separados. Si un capítulo previo no está disponible, declara evaluación provisional, no le asignes 0 por ausencia de reenvío.

## Inicio sencillo v0.3 (prototipo)

Para peticiones como «Quiero empezar mi TFG», consulta `design/v0.3-recorrido-estudiante.md` y, con autorización, crea una carpeta **privada y nueva** usando internamente `python3 scripts/student_project.py init RUTA_PRIVADA_NUEVA`. No solicites Git, terminal ni comandos al estudiante. Lee el `LEEME_PRIMERO.md` generado y acompaña la tarea E01.

Cuando el estudiante entregue un archivo para evaluar, captura su versión con `python3 .tfg/tools/student_project.py submit . RUTA_RELATIVA` desde el proyecto privado. La copia se realiza al **entregar**; no requiere `begin-revision` antes de editar. El análisis científico, la rúbrica y las limitaciones de las notas formativas siguen siendo obligatorios. Si careces de acceso a archivos, declara el límite y enseña a guardar manualmente los informes.
