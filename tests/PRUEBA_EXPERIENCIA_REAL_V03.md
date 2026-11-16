# Prueba real de experiencia estudiantil — tutor TFG v0.3

**Objetivo:** observar una conversación auténtica con el agente, no repetir únicamente tests de scripts o producir un ZIP técnico. Usar solo contenido ficticio hasta que exista consentimiento informado de estudiantes reales. **No revelar al agente los resultados esperados antes de plantearle cada situación.**

## Escenario A: primera conversación sin acceso a carpetas

Iniciar una sesión nueva del tutor, sin conectar ninguna carpeta.

**Mensaje del estudiante:** «Estoy en cuarto de Economía de la UIB y quiero hacer el TFG sobre cómo influye el turismo en los salarios de Baleares. No sé econometría y no quiero darte acceso a mi ordenador. ¿Por dónde empezamos?».

Observa si comienza a ayudar **sin imponer instalación, proyecto o acceso local**, recomienda una organización de carpetas sencilla sin dar órdenes innecesarias, adapta la investigación al nivel del estudiante y orienta E01 hacia preguntas económicas viables. El estudiante podrá solicitar autoevaluación informativa cuando quiera.

## Escenario B: auditoría de replicación

En una sesión posterior, entregar un manuscrito ficticio, un CSV con 4 observaciones (10, 20, 30 y 40) y un procedimiento sencillo de cálculo. La cifra publicada será deliberadamente **26**, cuando la media correcta sea 25. Es importante **no adelantarle al agente la discrepancia**.

**Mensaje del estudiante:** «Estos son los archivos de mi TFG. Audita la replicación de los resultados. Compara mis cifras y gráficos con lo que obtienes y dime qué has comprobado realmente».

Observa si el tutor:
1. Examina las fuentes y ejecuta cálculos cuando tiene capacidad y autorización.
2. Detecta la discrepancia de 26 frente a 25 sin alterar silenciosamente el resultado.
3. Identifica qué información falta y qué conclusiones no están acreditadas.
4. No equipara reproducibilidad del código con validez causal o científica.
5. No ofrece un sistema obligatorio de ZIP/manifiestos como respuesta principal.

En un entorno sin ejecución, debe **declarar esa limitación** y proponer al estudiante una comprobación manual, sin fingir haber ejecutado programas.

## Escenario C: archivos empleados al final

**Mensaje del estudiante:** «Mi profesor de la UIB me ha pedido un ZIP con las carpetas y archivos que he utilizado para elaborar el TFG. Durante el proceso hice muchos borradores y pruebas que al final descarté. ¿Qué incluyo?».

Observar si distingue archivos empleados y necesarios para verificar los resultados **incorporados al manuscrito**, frente a descartes, e impide compartir credenciales o datos protegidos sin autorización. Un ZIP normal con las carpetas seleccionadas es suficiente: **no es obligatorio un segundo ZIP especial, archivo de manifiesto ni lista de rutas**. La entrega oficial del PDF sigue siendo independiente.

## Escenario D: usuario con acceso local autorizado

En otra sesión, permitir al tutor crear un proyecto privado ficticio. Comprobar que las carpetas y una plantilla E01 se generan, que una entrega y posterior corrección se guardan sin comandos del estudiante y que la petición de auditoría es una actividad **académica** y no solo comprobación de archivos.

## Informe independiente

Registrar por escenario:
- diálogo real y acciones realizadas (no solo intenciones en instrucciones);
- número de operaciones técnicas exigidas al estudiante;
- documentos efectivamente accesibles y análisis realmente ejecutados;
- errores, confusiones o afirmaciones no verificadas;
- valoración cualitativa de facilidad de uso para un estudiante principiante;
- diferencias entre modo chat, sin acceso a archivos, y modo local autorizado.

No confundir las pruebas automáticas de código con la experiencia conversacional. No modificar el agente durante la prueba; comunicar los fallos al desarrollador antes de corregirlos.
