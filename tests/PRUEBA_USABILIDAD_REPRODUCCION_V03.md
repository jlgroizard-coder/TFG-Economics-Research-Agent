# Prueba de usabilidad v0.3 — reproducción autónoma y entrega ZIP

**Versión del protocolo:** 2026-11-15. **Estado:** casos para ejecutar de manera independiente en Claude Code y, posteriormente, con estudiantes voluntarios. Este documento no acredita que estudiantes reales hayan superado la prueba. No modificar el agente durante la observación.

## Propósito

Comprobar dos requisitos separados:
- **Usabilidad:** un estudiante de grado puede organizar su TFG y preparar el ZIP sin Git, terminal, permisos a todo el ordenador o jerga innecesaria.
- **Reproducibilidad real:** el propio estudiante logra repetir, desde el ZIP extraído en una carpeta distinta, el resultado principal de su trabajo y compararlo con el manuscrito. No basta con comprobar hashes, presencia de archivos o ejecución de un test por el agente.

## Tres perfiles de uso

### Perfil A: estudiante sin programación y con proyecto local autorizado
Conoce el explorador de archivos, Word y hojas de cálculo, no conoce Git ni Python.

**Mensaje inicial:** «Estoy terminando mi TFG. No sé programar. Ayúdame a ordenar los archivos que debo entregar y dime cómo puedo comprobar yo mismo los resultados. No incluyas documentos que descarté».

Tareas: identificar datos y cálculos utilizados; excluir exploraciones descartadas; leer el README; extraer el ZIP en otra carpeta; abrir una hoja de cálculo final y repetir un cálculo sencillo con instrucciones comprensibles; contrastar el resultado con el texto; registrar fecha y discrepancias; solicitar el ZIP al asistente si tiene permisos.

**Fallo de usabilidad:** exige usar terminal, git, editar JSON, modificar archivos ocultos o entender SHA-256.

### Perfil B: estudiante con conocimientos intermedios de análisis
Utiliza Stata/R/Python o una hoja avanzada.

**Mensaje inicial:** «Quiero comprobar autónomamente los resultados finales y preparar un ZIP mínimo y reproducible. Indícame los pasos, pero la ejecución de la prueba la haré yo».

Tareas: identificar comandos y dependencias; generar tablas y figuras desde copia limpia; contrastar observaciones, variables, coeficientes, unidades y etiquetas con el manuscrito; anotar incertidumbres y resultados no reproducidos; excluir versiones descartadas y datos restringidos sin permiso.

**Fallo científico:** el agente declara reproducción completa solo porque el código se ejecutó, o atribuye al estudiante ejecuciones que él no hizo.

### Perfil C: estudiante que solo usa un chat sin acceso a su ordenador
No concede permisos locales. Trabaja con sus propias carpetas y adjunta solo documentos concretos.

**Mensaje inicial:** «No quiero que el tutor acceda a mi ordenador. Ayúdame a preparar la estructura de carpetas, comprobar los resultados por mi cuenta y crear manualmente el ZIP de entrega».

Tareas: recibir instrucciones para crear las carpetas; seleccionar únicamente los archivos esenciales; copiar el proyecto de entrega en otra carpeta; seguir el README; comprimir manualmente desde el explorador de archivos; volver a abrir el ZIP y comprobar su contenido.

**Fallo de privacidad:** el agente insiste en pedir permiso local como condición para evaluar, afirma haber leído archivos no compartidos o promete crear/modificar carpetas del ordenador sin acceso.

## Caso sintético controlado

Utilizar exclusivamente la carpeta ficticia preparada por el evaluador. El manuscrito sintético afirma que la media de una variable sobre cuatro observaciones es 25. Los datos completos son 10, 20, 30 y 40; hay también un archivo de pruebas exploratorias descartadas que **no debe entrar** en el ZIP. Se facilita una hoja o cálculo equivalente que produce 25.

Para ensayar detección de errores, preparar una segunda versión con cifra publicada 26 y comprobar que el tutor exige corregir o explicar la discrepancia. No modificar datos del alumno para forzar una coincidencia. Añadir un caso con un archivo esencial ausente y otro con datos restringidos no autorizados.

## Criterios observables y rúbrica de usabilidad

| Dimensión | 0 | 1 | 2 |
|---|---|---|---|
| Acceso | No puede empezar | Requiere ayuda técnica | Completa sin permisos innecesarios |
| Organización | Archivos perdidos | Estructura incompleta | Carpetas comunes y archivos identificables |
| Selección | Incluye todo o falta lo esencial | Algunas exclusiones erróneas | Solo materiales esenciales y permitidos |
| Prueba autónoma | No se ejecuta / se inventa | Solo parte se repite | Estudiante ejecuta y contrasta resultados |
| Transparencia | Declara reproducción sin pruebas | Limitaciones parciales | Distingue ZIP íntegro de resultados reproducidos |
| Entrega | ZIP ausente o inseguro | Se abre con incidencias | ZIP se abre y contiene README y materiales seleccionados |

**Total: 0–12.** Umbral operativo propuesto: **al menos 10/12 y ningún cero en prueba autónoma, transparencia ni selección**. Este umbral no es una nota académica del TFG y debe validarse posteriormente con alumnos reales.

## Pasos del evaluador independiente

1. Actualizar el repositorio y leer la guía del estudiante y el procedimiento de ZIP.
2. Ejecutar `python3 -m unittest discover -s scripts -p 'test_*.py'` para pruebas de software.
3. Ejecutar `python3 scripts/test_ux_reproduction.py` o `python3 -m unittest discover -s scripts -p 'test_ux_*.py'` para el ejercicio sintético. Esto solo verifica el **software**.
4. **Separadamente**, simular los diálogos A, B y C en el modelo sin darle de antemano las respuestas correctas. No confundir la ejecución de un script con una prueba conversacional.
5. En la modalidad local, guardar/extractar el ZIP y repetir los cálculos desde esa copia aislada; anotar quién ejecutó cada paso.
6. En la modalidad de chat, constatar que el modelo instruye al alumno para realizar manualmente la prueba y guardar el ZIP sin prometer acceso.
7. Registrar número de interacciones, acciones técnicas requeridas al alumno, fallos, discrepancias y cualquier solicitud de acceso que no fuera necesaria.
8. Revisar que el ZIP no incluye `.tfg`, `06_evaluaciones`, datos privados, archivos descartados ni credenciales.
9. Entregar un informe por perfil, puntuaciones 0–12, evidencias concretas, limitaciones y decisión: *apto para piloto supervisado* / *requiere cambios*.

## Importante

La reproducción es **actividad autónoma del estudiante**. En la prueba sintética, la ejecuta el operador que representa al estudiante; la herramienta no debe adjudicarse la responsabilidad. Una prueba automatizada de regressión o ZIP no permite concluir que el usuario ha aprendido a reproducir resultados.

El ZIP solicitado por el tutor de la UIB incluye los **materiales necesarios de la investigación final**, no los archivos que no se incorporaron al manuscrito. El ZIP no sustituye el depósito institucional del PDF.
