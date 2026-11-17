# Tutor IA del TFG en Economía — UIB

**Prototipo v0.3: tutor conversacional accesible, con auditoría de replicación.**

El tutor acompaña a estudiantes de Economía de la UIB en la formulación de preguntas, lectura de literatura, diseño de investigación, evaluación formativa y comprobación de resultados. **Sus notas son orientativas y nunca sustituyen la evaluación del profesorado.**

## Empezar: sin complejidad informática

Escribe: **«Quiero empezar mi TFG sobre…»**. El tutor debe ayudar inmediatamente y, cuando sea útil, **recomendar** abrir un proyecto y organizar las carpetas: propuesta, literatura, datos, análisis y manuscrito. El estudiante elige entre:
- **Proyecto local conectado:** con permiso, la IA puede crear y ordenar carpetas y conservar versiones de las entregas (prototipo `scripts/student_project.py`).
- **Solo chat con adjuntos:** no se necesita dar acceso al ordenador. El estudiante conserva archivos en las carpetas que cree manualmente; la IA solo analiza lo compartido.
- **Almacenamiento en la nube:** si dispone de integración compatible o comparte los documentos.

La orientación académica y la autoevaluación **no dependen** de la autorización de acceso local. Los estudiantes no necesitan Git, terminal, JSON ni comandos de versionado. El despliegue inicial del proyecto local puede requerir la ayuda de un responsable técnico.

[Guía rápida](guides/GUIA_RAPIDA_ESTUDIANTE.md) · [Modalidad solo chat (3 pasos)](guides/MODALIDAD_CHAT_SIN_ACCESO_LOCAL.md) · [Documento único para adjuntar](guides/PAQUETE_UNICO_CHAT.md) · [Recorrido v0.3](design/v0.3-recorrido-estudiante.md).

## Auditoría de replicación — petición del estudiante

En cuanto existan resultados, el estudiante puede pedir: **«Audita la replicación de mis resultados»**. El tutor IA deberá examinar datos, códigos, hojas de cálculo, tablas y manuscrito; ejecutar lo que pueda y esté autorizado; **comparar los resultados generados con las cifras y gráficos publicados**, detectar incoherencias y declarar qué no pudo verificar. La simple existencia de un ZIP o de código **no constituye una reproducción**.

La auditoría se adapta a la modalidad empírica, teórica o de revisión crítica. Se fomenta que el estudiante comprenda y repita los procedimientos; el informe no es una certificación oficial.

[Guía de auditoría y materiales](guides/REPRODUCIBILIDAD_Y_ZIP_FINAL.md).

## Entrega académica

El tutor de la UIB solicitará **un ZIP con las carpetas y archivos efectivamente empleados en la elaboración del TFG** y necesarios para comprobar sus resultados. No hace falta preparar un segundo «ZIP de reproducción», ni aportar todo lo creado y descartado durante la investigación. Se excluirán credenciales y datos restringidos sin autorización. El ZIP no sustituye el depósito oficial del manuscrito PDF.

La antigua utilidad `scripts/repro_package.py` queda **legada, opcional y no forma parte del recorrido de estudiantes v0.3**. No impone un formato de archivo ni una lista obligatoria.

## Para docentes y desarrolladores

- `instructions-portable.md`: reglas académicas y comportamiento común.
- `CLAUDE.md` / `AGENTS.md`: instrucciones específicas de agentes locales.
- `references/`: guía de TFG, rúbricas, protocolo e indicadores técnicos.
- `scripts/student_project.py`: inicializador opcional de proyecto local y captura de entregas.
- `scripts/expediente.py`: motor avanzado histórico v0.2, no exigido a estudiantes.
- `scripts/repro_package.py`: empaquetador legado, no necesario para auditar resultados.
- `tests/`: pruebas funcionales y protocolos de usabilidad.

**Estado:** prototipo técnico, aún pendiente de probar conversaciones completas y usos reales con estudiantes principiantes. No incorporar datos personales o trabajos reales al repositorio público.

## Dos precisiones de uso

- **Primer acceso local:** un alumno que parte de cero puede abrir una carpeta de proyecto previamente preparada por quien despliega el tutor, desde la opción de abrir carpeta/proyecto de su aplicación. La inicialización requiere un entorno compatible y una configuración inicial; no se ha desarrollado un instalador de un clic.
- **Archivos mezclados:** antes de comprimir, crear `TFG_para_entregar` y **copiar** únicamente los archivos empleados, sin borrar originales; después comprimir esa carpeta y probar el contenido. [Instrucciones paso a paso](guides/REPRODUCIBILIDAD_Y_ZIP_FINAL.md).
