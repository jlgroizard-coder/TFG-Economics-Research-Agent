# Expediente privado y continuidad de evidencia entre versiones (v0.2)

El repositorio público contiene **solo el agente y casos sintéticos**. El expediente real de cada estudiante vive fuera del repositorio, en una carpeta privada con permisos gestionados por la persona estudiante o tutor. No se transmite automáticamente a ningún proveedor; la persistencia se logra guardando archivos y volviéndolos a abrir en cada sesión. Las aplicaciones web sin acceso a esos archivos deben pedir que el usuario los aporte.

## Archivos del expediente

- `expediente.json`: inventario de documentos, criterios, decisiones y comprobaciones, según `schemas/expediente.schema.json`.
- `evaluaciones/`: informes por fecha y versión. Nunca sobrescribir evaluaciones anteriores.
- `01_propuesta/`, `02_literatura/`, `03_datos_raw/`, `04_datos_work/`, `05_codigo/`, `06_resultados/`, `07_texto/` y `09_entrega/`: materiales de investigación.
- `decisiones.md`: actas y cambios de pregunta, método, datos, supuestos.

## Estados de evidencia obligatorios

- **vigente_verificada**: existe un artefacto concreto, se ha leído/comprobado y es aplicable al estado actual del proyecto.
- **vigente_no_verificada**: existe, pero no ha podido comprobarse.
- **no_aportada_ahora**: el documento estaba antes, pero no se ha adjuntado ni se ha podido reabrir en esta sesión.
- **desactualizada**: estaba comprobado, pero una modificación de pregunta, muestra, método o resultados exige revalidarlo.
- **refutada**: una prueba o fuente fiable contradice la afirmación o resultado.
- **pendiente**: acción prevista sin producto acreditado.

El registro histórico conserva las evidencias, pero **no conserva automáticamente los puntos**. Toda puntuación actual requiere evidencia vigente y aplicable. No convertir `no_aportada_ahora` en cero ni asumir que el estudiante ha perdido el trabajo; indicar **calificación provisional / incompleta** para los criterios afectados y pedir la última versión de los archivos correspondientes. No extrapolar una nota global completa si falta material esencial. Si el usuario pide explícitamente una evaluación limitada al archivo nuevo, puntuar solo su calidad con la etiqueta **evaluación parcial**, sin compararla con la nota global anterior.

## Protocolo de nueva versión

1. Identificar versión, etapa E01–E14, pregunta/método actual y documentos que han cambiado.
2. Abrir `expediente.json` y localizar materiales anteriores potencialmente pertinentes.
3. Comprobar cambios de dependencias: si cambia variable, muestra, modelo o datos, revisar qué tablas, conclusiones y referencias quedan desactualizadas.
4. Leer físicamente los documentos antiguos y nuevos cuando estén accesibles. Si no se puede, marcar `no_aportada_ahora` y pedir los archivos. No fingir verificación.
5. Registrar, por **criterio A–H**, evidencia, estado, ruta, versión, fecha y qué comprobación se hizo.
6. Decidir si la revisión es del expediente completo o solo de un capítulo; declarar el alcance.
7. Emitir nota completa y de etapa solo cuando sea defendible con las evidencias vigentes. Si hay evidencia esencial inaccesible, presentar puntuación **provisional de lo observado**, especificar criterios no evaluables y no compararla como una nota global con versiones completas.
8. Aplicar por separado los indicadores técnico y de correspondencia del documento `references/indicadores-tecnicos.md`.
9. Registrar diferencias verificadas contra la versión anterior y tres tareas siguientes.

## Ejemplos de continuidad

- En v3 se entrega solo un capítulo de resultados; la literatura de v2 se conserva en archivo accesible y sigue ajustada a la pregunta: **releerla y mantener su evaluación**, no borrarla.
- La literatura de v2 no está disponible hoy: **no_aportada_ahora**, sin deducir que se eliminó.
- Se cambia una pregunta sobre datos oficiales por una simulación sin justificación: la pertinencia anterior puede estar **desactualizada**; la calificación no tiene por qué subir.
- Se genera un script que reproduce CSV, pero el texto ofrece otra cifra: código **reproducible**, correspondencia **incorrecta** y resultado científico **no sustentado**.

## Controles del registro v0.2.1

El comando `audit` muestra **el último estado efectivo por combinación criterio–artefacto** (no suma estados históricos). Si falta el archivo registrado, su estado efectivo se presenta como `no_aportada_ahora`; si cambió el hash, `desactualizada`. Estos diagnósticos técnicos **no prueban ni refutan contenido científico**.

Para registrar una **nota global**, deben existir evidencias documentadas en A–H y no puede haber evidencia efectiva inaccesible o desactualizada sin revisar. Para un criterio realmente vacío o pendiente, se admite evidencia con estado `pendiente`, pero debe documentarse la ausencia real; un documento simplemente inaccesible no se convierte en puntuación cero. Esta barrera es conservadora y no sustituye revisión del informe por el tutor.

`add-decision --change pregunta|ambito|periodo|datos|variables|metodo|hipotesis --detail "..." ` registra cambios e invalida conservadoramente la evidencia dependiente; `set-question --question "..." --reason "..." ` hace lo mismo para la pregunta. El mapa de dependencias es una **heurística**: obliga a revalidar, pero no impone automáticamente un suspenso.

`revoke-evaluation --version ... --report ... --reason ...` anula una evaluación **sin borrarla**, y `audit` verifica hashes de los informes.

Una presentación parcial puede mostrar `19,0 puntos observados de 55 puntos evaluables`, pero **nunca** transformarlo en nota global sobre 10 ni compararlo con una evaluación completa.
