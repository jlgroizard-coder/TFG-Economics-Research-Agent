# Auditoría de replicación y materiales del TFG — guía para estudiantes

El estudiante puede pedir en cualquier momento a su tutor IA: **«Audita la replicación de los resultados de mi TFG»**. La IA examinará la documentación y los datos que tenga a su disposición, ejecutará procedimientos cuando esté autorizada y sea técnicamente posible, y comparará sus salidas con los resultados del manuscrito. **No debe afirmar haber reproducido lo que no ha podido ejecutar o contrastar**.

## Organización recomendada, no barrera de entrada

Al comenzar, el tutor IA puede recomendar crear un proyecto con carpetas para propuesta, literatura, datos, análisis, manuscrito y evaluaciones. Quien no autorice acceso local puede crear las carpetas manualmente y adjuntar únicamente los archivos que elija. No hace falta Git ni terminal para solicitar orientación o una evaluación informativa.

## Qué debe revisar la auditoría de la IA

1. **Fuente y trazabilidad:** origen y condiciones de uso de los datos, variables, transformaciones y periodos.
2. **Ejecución:** programas o cálculos efectivamente ejecutados, versiones y dependencias. Si la IA no puede ejecutarlos, debe explicar cómo probarlos y declarar esa limitación.
3. **Correspondencia:** comprobar tamaño de muestra, estadísticas, coeficientes, tablas, figuras, unidades, títulos y afirmaciones del texto frente a las salidas.
4. **Alcance y resultado:** distinguir reproducción completa, parcial o no comprobada; describir discrepancias concretas y próximos pasos para resolverlas. Una ejecución correcta del programa no valida automáticamente su identificación causal ni su calidad científica.
5. **Autonomía del estudiante:** debe comprender el procedimiento, revisar las discrepancias y poder explicar la obtención de sus resultados. Puede repetir una prueba desde una copia limpia para comprobar que no depende de rutas o archivos externos.

La auditoría es **formativa**; no sustituye la revisión del profesor de la UIB.

## ZIP solicitado por el tutor académico

En la entrega final, el profesor solicitará **un único ZIP con las carpetas y archivos realmente empleados en la elaboración del TFG** y necesarios para examinar o replicar los resultados incluidos: manuscrito final, datos compartibles, documentación de fuentes, programas, hojas de cálculo, tablas y gráficos utilizados, e instrucciones suficientes para comprender las dependencias.

**No hace falta incluir** todas las versiones descartadas, archivos exploratorios no utilizados, conversaciones con la IA, informes de autoevaluación o archivos de funcionamiento del agente. Tampoco hay que preparar un ZIP adicional específico de «reproducción» ni un inventario técnico obligatorio.

**Si tienes borradores descartados mezclados con datos o programas utilizados, no comprimas directamente todas las carpetas del proyecto.** Prepara primero una copia limpia de lo que vas a entregar:

1. Crea una carpeta nueva llamada `TFG_para_entregar`.
2. Dentro, reproduce únicamente las subcarpetas relevantes, por ejemplo `03_datos`, `04_analisis`, `05_manuscrito` y `07_entrega`.
3. Copia **solo los archivos que aparecen efectivamente en el trabajo** o que son indispensables para obtener las tablas, figuras y resultados. No muevas ni borres los originales: copia los seleccionados.
4. En Windows puedes seleccionar archivos individuales con **Ctrl + clic**; en macOS, con **Comando (⌘) + clic**. Utiliza «Copiar» y después «Pegar» en la carpeta limpia.
5. Revisa el contenido de cada subcarpeta, comprueba que no haya credenciales, identificadores personales ni datos restringidos sin autorización y que tampoco falten archivos necesarios.
6. Comprime `TFG_para_entregar` con la opción de comprimir del explorador/Finder; descomprímelo en otra ubicación y comprueba que es posible seguir el análisis desde esa copia.

No hace falta un segundo ZIP de reproducción ni un fichero manifiesto obligatorio. Este procedimiento evita incluir sin querer pruebas descartadas al comprimir carpetas de trabajo enteras.

El estudiante puede comprimir las carpetas seleccionadas con el explorador de archivos de su ordenador. Si su IA tiene acceso y permiso, puede ayudar a revisar su contenido. No debe adjuntar contraseñas, credenciales ni información restringida sin autorización. Cuando no sea posible compartir datos protegidos, documentará las fuentes y las instrucciones de acceso legítimo.

El ZIP para el tutor es un complemento de trabajo y **no sustituye el depósito institucional del PDF** conforme a las instrucciones de la Facultad.

## Pregunta útil para el tutor IA

> «Quiero que audites la replicación de los resultados que presento en mi TFG. Comprueba mis datos, programas, tablas y figuras frente al manuscrito. Ejecuta lo que esté autorizado y explica qué resultados has verificado, cuáles no coinciden y cuáles no puedes comprobar. Después dime qué carpetas y archivos utilizados debo incluir en el ZIP que entregaré al profesor».

