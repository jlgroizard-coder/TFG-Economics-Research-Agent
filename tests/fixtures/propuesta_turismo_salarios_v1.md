# Propuesta de investigación — borrador v1

**Título:** *El impacto causal del turismo en los salarios de Baleares: un análisis regional, sectorial y municipal (2015–2024)*  
**Estudiante:** Estudiante ficticio (caso de prueba)  
**Asignatura:** Trabajo de Fin de Grado en Economía (UIB)  
**Etapa:** E03 — propuesta inicial  
**Modalidad:** Empírica cuantitativa  
**Fecha:** Noviembre de 2026

> Este documento es un **caso ficticio creado para probar un tutor IA**. No procede de ningún alumno real. Las afirmaciones, datos y referencias que aparecen en la propuesta deben someterse al mismo escrutinio que los de cualquier borrador académico; no se presupone que sean correctos.

## 1. Introducción y motivación

El turismo es el motor de la economía balear y, por tanto, debería tener efectos positivos sobre los salarios de los residentes. Cuando llegan más turistas, aumenta la demanda de hoteles, restaurantes y servicios complementarios. Las empresas contratan a más trabajadores, se reduce el desempleo y, como consecuencia necesaria, suben los salarios. Este razonamiento es suficiente para anticipar que los destinos turísticos pagarán mejor a sus trabajadores.

Este trabajo demostrará que el aumento de visitantes internacionales entre 2015 y 2024 **causó** un incremento de los salarios en Baleares. La elección del periodo permite incluir tanto el crecimiento anterior a la pandemia como la recuperación posterior. También permitirá recomendar políticas de expansión turística para mejorar el nivel de vida de los trabajadores.

Los datos mostrarán qué porcentaje de las diferencias salariales entre Baleares, Canarias y el resto de España se explica por el volumen de turistas. La hipótesis es que cuanto mayor sea el número de visitantes, mayor será el salario. El trabajo será el primero en estudiar la relación entre turismo y salarios de manera causal en las islas españolas.

## 2. Pregunta, objetivos e hipótesis

La pregunta principal es: **¿Cuánto aumenta el salario de un trabajador de Mallorca cuando llegan un millón de turistas adicionales a Baleares?** Para responderla utilizaré el salario medio anual de cada comunidad autónoma, de modo que las estimaciones permitirán explicar lo que ocurre en Mallorca, Menorca, Ibiza y Formentera por separado.

Los objetivos son (i) medir la evolución de la remuneración de los residentes en Baleares; (ii) comparar los salarios de hostelería en Baleares con el salario medio de todas las actividades económicas en Canarias y España; (iii) separar los efectos de la productividad, la estacionalidad, la inmigración y el turismo; (iv) estimar el efecto causal del turismo; y (v) proponer una recomendación normativa.

La hipótesis H1 es que más turistas implican necesariamente un salario superior, porque la demanda laboral se desplaza hacia la derecha. La hipótesis H2 es que este efecto será mayor en Mallorca, pues concentra gran parte de los visitantes y tiene una industria turística consolidada. No se consideran mecanismos de oferta laboral, movilidad geográfica o reasignación entre sectores porque complicarían innecesariamente el análisis.

## 3. Literatura y contribución

La teoría económica predice que un desplazamiento positivo de la demanda de servicios eleva el empleo y los salarios de equilibrio. En mercados competitivos, la llegada de turistas genera ingresos que se transmiten de forma inmediata a todos los trabajadores, con independencia de su cualificación, jornada y sector.

González y Surovtseva (2024) analizan el turismo en España utilizando shocks en destinos internacionales alternativos. Sus resultados demuestran que una desviación estándar más de turistas aumenta **un 3 % el salario medio regional**, sin efectos relevantes sobre la composición sectorial del empleo. Este resultado confirma que el turismo eleva necesariamente los salarios, por lo que no será preciso analizar otros mecanismos.

El artículo de Martínez y Ferrer (2022), *Tourism Booms and Wage Convergence in the Balearic Islands*, publicado en *Journal of Mediterranean Labour Economics*, concluye que el turismo explica el 80 % de la brecha salarial entre Baleares y Canarias. Es una referencia fundamental para el proyecto, aunque todavía no se ha localizado el texto íntegro ni su DOI.

La Encuesta Anual de Estructura Salarial del INE también demuestra que Baleares es la región española con los salarios más altos durante todo el periodo 2015–2024, lo que corrobora la hipótesis. La literatura es, por tanto, unánime y no deja preguntas relevantes pendientes. La principal contribución de este TFG será repetir el resultado con datos más recientes.

## 4. Datos y variables

Se combinarán tres bases:

- **INE, Encuesta Anual de Estructura Salarial (EAES):** utilizaré los salarios por hora de los trabajadores de hostelería de Mallorca, Menorca, Ibiza y Formentera para todos los años entre 2015 y 2024. Estos datos se obtendrán directamente de las tablas públicas de la EAES, sin solicitar microdatos.
- **FRONTUR:** número de turistas internacionales llegados cada año a cada municipio balear, desagregado por isla, comunidad autónoma de origen del trabajador y profesión del visitante. La información estará disponible en una única tabla descargable.
- **INE, EPA:** tasa de desempleo de cada región española, por año, sector y tipo de contrato, para controlar las condiciones del mercado laboral.

La variable dependiente será el **salario bruto medio anual nominal**, aunque la pregunta se refiere al poder adquisitivo y las conclusiones hablarán de salarios reales. El turismo se medirá mediante el número absoluto de visitantes, sin dividirlo por la población residente ni por la capacidad alojativa. Esto permite comparar directamente Baleares con Madrid, Canarias y Castilla-La Mancha.

Como la relación se estudia por municipios, cada observación será una pareja municipio-año. Sin embargo, el salario se obtiene como promedio por comunidad autónoma y año; todos los municipios de Baleares recibirán el mismo salario regional. Si hay valores ausentes se sustituirán por cero. El año 2020, con una caída excepcional de turistas, se conservará sin análisis separado porque ofrece una variación exógena especialmente útil.

No he descargado todavía las tablas concretas ni comprobado sus dimensiones, pero el acceso debería ser sencillo.

## 5. Metodología

La ecuación principal será:

\[
\log(w_{it})=\alpha_i+\lambda_t+\beta\log(T_{it})+\gamma U_{it}+\delta H_{it}+\varepsilon_{it},
\]

donde \(i\) representa municipios, \(t\) años, \(w\) el salario bruto nominal medio de la comunidad autónoma, \(T\) el número de turistas internacionales, \(U\) el desempleo regional y \(H\) el empleo en hostelería. Los términos \(\alpha_i\) y \(\lambda_t\) son efectos fijos municipales y de año.

Los efectos fijos eliminan toda endogeneidad, incluido el hecho de que los salarios altos puedan atraer trabajadores o turistas. Por ello, \(\beta\) se interpretará como el **efecto causal del turismo** sobre el salario individual, y un coeficiente de 0,05 significará que **un millón de turistas adicionales** incrementa los salarios un 5 %.

Además, se utilizará como instrumento el número de pasajeros del aeropuerto de Palma. El instrumento será válido porque todos los pasajeros son turistas y porque el tráfico aéreo solo puede afectar a los salarios mediante el gasto turístico. También se introducirá el empleo hotelero contemporáneo como control para aislar mejor el efecto neto del turismo. Los errores estándar se estimarán sin agrupamiento, pues los efectos fijos ya corrigen la correlación entre observaciones.

Se realizará un contraste de significación al 5 %. Si el coeficiente \(\beta\) es significativo, quedará demostrada la causalidad. Si no lo es, se eliminarán los controles que reduzcan su significación hasta identificar una especificación adecuada.

## 6. Resultados preliminares

La siguiente tabla resume las estimaciones principales previstas. Se ha preparado antes de descargar los datos, utilizando cifras aproximadas que representan lo que esperamos encontrar.

| Modelo | Coeficiente turismo | Error estándar | Observaciones | Efectos fijos |
|---|---:|---:|---:|---|
| (1) Básico | 0,080*** | 0,011 | 170 | No |
| (2) Regiones y años | 0,062*** | 0,014 | 170 | Sí |
| (3) Municipios y años | 0,051*** | 0,009 | 240 | Sí |
| (4) IV pasajeros de Palma | 0,093*** | 0,018 | 240 | Sí |

*Nota: *** p < 0,01. Fuente: cálculos propios previstos con INE y FRONTUR.*

La especificación (3) será la preferida, porque tiene el mayor número de observaciones y un coeficiente razonable. Como se estudian 17 comunidades autónomas durante 10 años, la muestra básica contiene 170 observaciones. La variación municipal permitirá disponer de 240 observaciones una vez añadidos los efectos fijos.

La tabla demuestra que el turismo eleva los salarios entre un 5 % y un 9 %. El efecto es estadísticamente significativo en todas las especificaciones, de modo que la hipótesis queda confirmada antes de ejecutar las regresiones.

## 7. Viabilidad y calendario

Dedicaremos una semana a descargar los datos, otra a estimar los modelos y una tercera a redactar el informe final. Como ya sabemos qué signo tendrán los coeficientes, no deberían surgir dificultades importantes. No se contempla una estrategia alternativa si los datos salariales municipales no existen.

La propuesta se presentará al tutor en diciembre. El código, las bases de datos procesadas y las figuras no se incluirán en la entrega final porque el documento Word contendrá las tablas definitivas. El paquete de reproducción se considerará opcional.

## 8. Conclusiones esperadas

El resultado esperado es que el turismo mejore los salarios de todos los trabajadores residentes de las islas. La política económica debe favorecer el crecimiento continuado del número de visitantes para elevar el bienestar de la población, ya que los salarios nominales son un indicador suficiente del nivel de vida y no es necesario estudiar los precios de la vivienda ni la estacionalidad.

La principal aportación del trabajo será demostrar rigurosamente esta relación mediante una regresión con efectos fijos y variables instrumentales. Los resultados serán aplicables a todas las islas y municipios baleares.

## Bibliografía

González, L., y Surovtseva, T. (2024). *Do More Tourists Promote Local Employment?* IZA Discussion Paper 17518. https://iza.org/publications/dp/17518/do-more-tourists-promote-local-employment

Instituto Nacional de Estadística. *Encuesta Anual de Estructura Salarial*. https://www.ine.es/

Martínez, J., y Ferrer, M. (2022). *Tourism Booms and Wage Convergence in the Balearic Islands*. *Journal of Mediterranean Labour Economics*, 14(2), 105–132.

Instituto Nacional de Estadística. *FRONTUR: estadística de movimientos turísticos en fronteras*. https://www.ine.es/
