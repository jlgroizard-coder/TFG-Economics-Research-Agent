# Tutor IA del TFG en Economía — UIB

**Agente académico abierto · prototipo de usabilidad v0.3 (MVP) · noviembre de 2026**

Este proyecto ayuda a estudiantes del Grado en Economía de la Universitat de les Illes Balears a preparar investigaciones científicas rigurosas, comprender la literatura, mejorar propuestas y manuscritos y producir un paquete reproducible. Ofrece una **evaluación formativa**, nunca una nota oficial de la UIB.

## Próximo rediseño: v0.3 centrada en el estudiante

Estamos diseñando una experiencia conversacional basada en **un proyecto local privado**, sin exigir Git, terminal o comandos de versionado. El estudiante podrá solicitar por sí mismo evaluaciones formativas; la evaluación institucional corresponde exclusivamente al profesorado de la UIB. **Ya existe un primer prototipo local de creación de proyectos y captura de entregas.** La experiencia conversacional aún requiere validación independiente; no se ha implementado una aplicación web propia.

- [Recorrido y organización del proyecto local](design/v0.3-recorrido-estudiante.md)
- [Guía rápida y pautas de uso eficiente para estudiantes](guides/GUIA_RAPIDA_ESTUDIANTE.md)
- [Pruebas previstas con diferentes perfiles tecnológicos](design/v0.3-pruebas-usabilidad.md)

## Instalación rápida

**Claude Code:** clona o descarga el repositorio y abre su carpeta en Claude Code. Se leerá `CLAUDE.md` y estarán disponibles las skills de `.claude/skills/`.

**Codex:** abre la carpeta del repositorio en Codex CLI o IDE. Sigue `AGENTS.md` y las skills de `.agents/skills/`. Usa `$tfg-tutor`, `$literature-review`, `$research-design`, `$tfg-evaluator` y `$reproducibility-audit` según la tarea.

**ChatGPT web, Claude web, Gemini:** copia `instructions-portable.md`, `references/rubrica.md`, `references/protocolo-evaluacion.md` y `references/guia-tfg-uib-2026-27.md` a un proyecto con instrucciones personalizadas. No se garantiza que puedan ejecutar scripts.

## Flujo del estudiante

1. En Claude Code o Codex, con acceso autorizado a archivos, pide: **«Quiero empezar mi TFG; crea mi proyecto local privado»**. El agente puede usar internamente `scripts/student_project.py` para crear carpetas, instrucciones y tarea E01, sin exigir terminal al alumno.
2. Pide ayuda para precisar dos preguntas económicas e identificar literatura.
3. Completa los entregables E01–E14 de la guía, con propuesta aprobada antes de Navidad.
4. Solicita `Evalúa mi TFG con rigor` y aporta los archivos pertinentes.
5. Guarda cada informe y aplica sus tres mejoras prioritarias. En el **flujo sencillo v0.3**, el agente captura cada entrega y el estudiante puede editar y volver a entregar sin comandos previos. El registro técnico anterior v0.2 continúa disponible para necesidades de auditoría avanzada.
6. Para entregar, prepara manuscrito, datos o instrucciones de acceso, programas, figuras, tablas y README de reproducción.

El informe distingue **calidad científica** (total y por etapa), **reproducibilidad técnica** y **correspondencia manuscrito–resultados**: son tres indicadores independientes, no una media. Una nota de un criterio no desciende automáticamente porque su capítulo no venga en el último archivo: debe consultarse el expediente y comprobar su vigencia. **Sin acceso a evidencia esencial, la nota es provisional o no evaluable, no cero por defecto.**

## Estructura

- `instructions-portable.md`: instrucciones comunes e independientes de proveedor.
- `references/`: rúbrica, protocolo, ética y guía UIB.
- `.agents/skills/` y `.claude/skills/`: cinco habilidades especializadas.
- `templates/`: ficha de artículo, propuesta, informe y documentación.
- `references/expediente-y-continuidad.md`: expediente privado y reglas de continuidad.
- `references/indicadores-tecnicos.md`: dos escalas técnicas independientes.
- `schemas/expediente.schema.json`: formato del expediente.
- `scripts/student_project.py`: inicio de un proyecto autónomo con instrucciones locales, tarea E01 y copias de entregas al solicitarlas.
- `scripts/expediente.py`: motor avanzado v0.2 de auditoría histórica (no exigido al estudiante en la ruta sencilla).
- `scripts/test_student_project.py`: pruebas de inicio y captura conversacional respaldada por archivos.
- `scripts/test_expediente.py`: pruebas del motor avanzado.
- `scripts/audit_package.py`: comprobación estructural estática.
- `scripts/test_audit.py`: pruebas del auditor.

## Privacidad y límites

No subas datos personales, trabajos privados, código secreto ni datos de acceso restringido al repositorio público. La verificación estructural de archivos **no implica** reproducción de resultados. El agente no sustituye a docentes, tribunales ni normas vigentes de la UIB. Contrasta siempre plazos y procedimientos con la Facultad.

Licencia: MIT para contenido propio. Los enlaces a la normativa universitaria no implican permiso para republicar documentos de terceros.
