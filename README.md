# Tutor IA del TFG en Economía — UIB

**Agente académico abierto · prototipo de usabilidad v0.3 (MVP) · noviembre de 2026**

Este proyecto ayuda a estudiantes del Grado en Economía de la Universitat de les Illes Balears a preparar investigaciones científicas rigurosas, comprender la literatura, mejorar propuestas y manuscritos y producir un paquete reproducible. Ofrece una **evaluación formativa**, nunca una nota oficial de la UIB.

## Próximo rediseño: v0.3 centrada en el estudiante

Estamos diseñando una experiencia conversacional basada en **un proyecto local privado**, sin exigir Git, terminal o comandos de versionado. El estudiante podrá solicitar por sí mismo evaluaciones formativas; la evaluación institucional corresponde exclusivamente al profesorado de la UIB. **Ya existe un primer prototipo local de creación de proyectos y captura de entregas.** La experiencia conversacional aún requiere validación independiente; no se ha implementado una aplicación web propia.

- [Recorrido y organización del proyecto local](design/v0.3-recorrido-estudiante.md)
- [Guía rápida y pautas de uso eficiente para estudiantes](guides/GUIA_RAPIDA_ESTUDIANTE.md)
- [Pruebas previstas con diferentes perfiles tecnológicos](design/v0.3-pruebas-usabilidad.md)
- [Prueba independiente de reproducción y ZIP para tres perfiles](tests/PRUEBA_USABILIDAD_REPRODUCCION_V03.md)
- `scripts/test_ux_reproduction.py`: cuatro simulaciones técnicas con ZIP extraído y cálculo reproducido desde una carpeta independiente (**no** es una prueba real con estudiantes).

## Estructura común y entrega final reproducible

**Todos los estudiantes**, también quienes usan solo chat con archivos adjuntos, mantienen una estructura común de carpetas en su ordenador o almacenamiento elegido. La IA puede ayudarles a organizarla, pero no requiere acceso a carpetas privadas. El estudiante debe **realizar autónomamente la prueba de reproducción** desde una copia independiente del proyecto.

El tutor de la UIB solicitará al final **un ZIP con el manuscrito definitivo y los archivos necesarios para obtener los resultados efectivamente utilizados**; no se exige aportar borradores descartados, intentos exploratorios ni el historial privado. El ZIP del tutor **no sustituye** el depósito oficial del PDF ni debe contener datos restringidos sin autorización.

- [Guía de prueba autónoma y ZIP final](guides/REPRODUCIBILIDAD_Y_ZIP_FINAL.md)
- `scripts/repro_package.py`: comprobación de lista y creación opcional de ZIP **sin ejecutar ni certificar resultados**.

## Instalación rápida

**Claude Code (con acceso local autorizado):** un tutor o responsable técnico puede preparar previamente el entorno y entregar al estudiante una carpeta de proyecto ya creada. El estudiante abre esa carpeta y conversa con el agente; **no necesita clonar GitHub ni usar terminal**. El repositorio y su instalación técnica están destinados a quien configura el entorno, no al principiante.

**Codex (con acceso local autorizado):** abre una carpeta de proyecto del estudiante previamente preparada. El equipo que despliega el agente es quien configura las herramientas; los comandos y skills no son requisitos para el estudiante.

**ChatGPT web, Claude web, Gemini:** utiliza [la guía autónoma para la modalidad sin acceso local](guides/MODALIDAD_CHAT_SIN_ACCESO_LOCAL.md), que incluye los documentos adicionales y las plantillas necesarias. El estudiante gestiona las carpetas y el ZIP manualmente; no se garantiza ejecución de scripts ni acceso a archivos no adjuntados.

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
