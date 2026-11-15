# Prueba autónoma de reproducibilidad y ZIP final — TFG Economía UIB

**Orientación del tutor académico para el curso 2026–27.** El estudiante es responsable de comprobar que puede reproducir sus resultados y de preparar un ZIP con los materiales que realmente sustentan el TFG. Este ZIP es un **requisito de trabajo del tutor**; no se presenta aquí como sustituto ni como norma general del depósito oficial de la UIB. La entrega oficial del manuscrito PDF seguirá las instrucciones de la Facultad.

## Una misma estructura, use o no un tutor IA conectado

Mantén una carpeta de proyecto en el ordenador, aunque trabajes únicamente mediante chat y adjuntos. Si utilizas la modalidad de nube, reproduce la estructura en tu almacenamiento elegido.

- \`01_propuesta/\`: la propuesta aprobada y sus versiones relevantes
- \`02_literatura/\`: bibliografía y fichas esenciales, **sin obligación de incluir todos los PDF de terceros**
- \`03_datos/\`: datos que se pueden compartir, diccionario, fuentes y permisos
- \`04_analisis/\`: programas y pasos necesarios para generar resultados
- \`05_manuscrito/\`: manuscrito de trabajo (no es obligatorio incluir borradores históricos)
- \`06_evaluaciones/\`: informes formativos privados (no es obligatorio enviarlos al tutor)
- \`07_entrega/\`: PDF definitivo, README de reproducción, lista de archivos a incluir
- \`.tfg/\`: historial interno opcional del agente, **no incluir en el ZIP**

No tienes que entregar notas descartadas, versiones intermedias no utilizadas, búsquedas fallidas, cachés, conversaciones ni todo el trabajo exploratorio. **Sí debes incluir lo indispensable para comprobar todas las cifras, tablas, gráficos y afirmaciones principales del manuscrito.**

## Prueba autónoma obligatoria antes de entregar

1. **Selecciona:** identifica los archivos realmente usados por tu TFG. Añádelos a \`07_entrega/ARCHIVOS_INCLUIDOS.txt\`, una ruta relativa por línea. Incluye el PDF final y \`07_entrega/README_REPRODUCCION.md\`.
2. **Explica:** en el README detalla requisitos, origen y fecha de los datos, transformaciones, programas y orden de ejecución, y señala exactamente qué tablas y figuras produce cada paso.
3. **Comprueba:** aparta una copia del paquete de los archivos de trabajo, descomprímela en otra carpeta y trabaja solo desde allí. Si el análisis usa Excel, Stata, R, Python u otro programa, abre los datos y ejecuta el procedimiento indicado. Si es un trabajo teórico, verifica las derivaciones o simulaciones; si es una revisión crítica, repite el protocolo de búsqueda/selección con sus límites.
4. **Contrasta:** compara con el TFG los números clave, unidades, periodos, tamaños muestrales, tablas y figuras. No basta con que los archivos existan: **el resultado debe coincidir**. Corrige y repite si hay discrepancias.
5. **Documenta:** en el README indica fecha, programa, entorno, pruebas ejecutadas, diferencias y si la reproducción fue **completa, parcial o no conseguida**. Nunca afirmes que está verificada si no se realizó.
6. **Prepara el ZIP:** incorpora solo lo seleccionado. Antes de enviarlo, comprueba que se abre, que no faltan archivos y que no contiene datos privados o de terceros sin permiso.
7. **Entrega:** facilita al tutor de la UIB el ZIP de materiales y la entrega institucional del PDF por los canales que correspondan. No asumas que el ZIP sustituye al depósito de Aula Digital.

## Qué hacer con datos restringidos o de gran tamaño

Nunca compartas información protegida o sin autorización. Si no puedes adjuntar los microdatos, incluye un diccionario, fuente oficial, condiciones de acceso y código que permita reproducir el análisis a quien tenga permisos legítimos; indica claramente que la reproducción de extremo a extremo **no se puede verificar sin ellos**. El tutor decidirá si la documentación es suficiente. No incorpores archivos protegidos al ZIP por comodidad.

## Lista de comprobación personal

- [ ] El ZIP contiene la versión final del TFG.
- [ ] He incluido únicamente los archivos necesarios para verificar mis resultados.
- [ ] He documentado las fuentes, variables, programas y pasos.
- [ ] He ejecutado yo mismo el procedimiento desde otra carpeta o copia limpia.
- [ ] He comparado resultados, gráficos y tablas con el manuscrito.
- [ ] He explicado cualquier diferencia, imposibilidad o restricción de acceso.
- [ ] He comprobado que el ZIP no incluye archivos privados o sin permiso.
- [ ] Sé explicar al tutor cómo se obtiene cada resultado principal.

## Herramienta de ayuda (opcional)

Si el agente tiene permiso de lectura de tu proyecto, puede comprobar la lista de archivos y crear el ZIP con \`scripts/repro_package.py\`. **Eso solo verifica la estructura e integridad del archivo comprimido; no realiza ni sustituye la reproducción académica que debes ejecutar tú mismo.** Si trabajas únicamente mediante chat, puedes preparar el ZIP manualmente con el explorador de archivos y utilizar exactamente esta lista de comprobación.

Las evaluaciones de la IA son formativas y no sustituyen la evaluación del profesor o tribunal de la UIB.
