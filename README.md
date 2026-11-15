# Tutor IA del TFG en Economía — UIB

**Agente académico abierto · v0.2.2 · noviembre de 2026**

Este proyecto ayuda a estudiantes del Grado en Economía de la Universitat de les Illes Balears a preparar investigaciones científicas rigurosas, comprender la literatura, mejorar propuestas y manuscritos y producir un paquete reproducible. Ofrece una **evaluación formativa**, nunca una nota oficial de la UIB.

## Instalación rápida

**Claude Code:** clona o descarga el repositorio y abre su carpeta en Claude Code. Se leerá `CLAUDE.md` y estarán disponibles las skills de `.claude/skills/`.

**Codex:** abre la carpeta del repositorio en Codex CLI o IDE. Sigue `AGENTS.md` y las skills de `.agents/skills/`. Usa `$tfg-tutor`, `$literature-review`, `$research-design`, `$tfg-evaluator` y `$reproducibility-audit` según la tarea.

**ChatGPT web, Claude web, Gemini:** copia `instructions-portable.md`, `references/rubrica.md`, `references/protocolo-evaluacion.md` y `references/guia-tfg-uib-2026-27.md` a un proyecto con instrucciones personalizadas. No se garantiza que puedan ejecutar scripts.

## Flujo del estudiante

1. Crea un **proyecto privado** fuera de este repositorio y copia `templates/estudiante/` como punto de partida.
2. Pide ayuda para precisar dos preguntas económicas e identificar literatura.
3. Completa los entregables E01–E14 de la guía, con propuesta aprobada antes de Navidad.
4. Solicita `Evalúa mi TFG con rigor` y aporta los archivos pertinentes.
5. Guarda cada informe y aplica sus tres mejoras prioritarias.
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
- `scripts/expediente.py`: registro privado con estados efectivos por criterio, invalidación conservadora por cambios de investigación, hashes de informes y anulación de evaluaciones.
- `scripts/test_expediente.py`: pruebas de regresión de continuidad y protección contra notas globales con archivos ausentes.
- `scripts/audit_package.py`: comprobación estructural estática.
- `scripts/test_audit.py`: pruebas del auditor.

## Privacidad y límites

No subas datos personales, trabajos privados, código secreto ni datos de acceso restringido al repositorio público. La verificación estructural de archivos **no implica** reproducción de resultados. El agente no sustituye a docentes, tribunales ni normas vigentes de la UIB. Contrasta siempre plazos y procedimientos con la Facultad.

Licencia: MIT para contenido propio. Los enlaces a la normativa universitaria no implican permiso para republicar documentos de terceros.
