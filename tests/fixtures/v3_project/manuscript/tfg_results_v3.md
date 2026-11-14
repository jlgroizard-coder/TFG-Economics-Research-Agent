# Turismo y salarios regionales: análisis ilustrativo con datos simulados

**Versión:** v3. **Etapa simulada:** E08–E09. **Autor:** estudiante ficticio.  
**Importante:** los datos son **sintéticos**. Ningún resultado de este ejercicio describe la economía balear real.

## 1. Pregunta y contribución

¿Cómo se relaciona la intensidad turística anual con el salario medio real de las regiones en un panel sintético que representa de forma estilizada varias economías regionales? Esta versión avanza respecto a v2 porque aporta datos, código y figuras. Se renuncia a identificar causalidad y se trata el coeficiente de panel como asociación descriptiva.

La revisión de literatura sigue limitada: se comentan de forma introductoria González y Surovtseva (2024), *Do More Tourists Promote Local Employment?*, y un artículo contextual de Caparrós Alcaraz (2018), pero todavía no se han incorporado cinco lecturas científicas completas. La contribución académica sigue siendo modesta.

## 2. Datos

El archivo \`data/synthetic_panel.csv\` contiene un panel **completamente simulado**, con ocho regiones y ocho años (2017–2024). No procede del INE. Las dos etiquetas Baleares_SIM y Canarias_SIM son ficticias, incluso si sus nombres evocan lugares reales.

Se estudia el salario **real anual medio** (\`nominal_wage/(cpi/100)\`) y la intensidad turística anual (\`tourists/population\`). El programa registra cada observación por región y año. El diccionario de variables está en \`data/DATA_DICTIONARY.md\`.

Para evitar distorsiones extraordinarias, **se excluye el año 2020 de las estimaciones principales**. En total, el panel de trabajo contiene 56 observaciones, correspondientes a ocho regiones y siete años.

## 3. Método

Se utiliza un modelo lineal de dos efectos fijos regionales y de año:

\[
\log(w_{rt}^{real})=\alpha_r+\lambda_t+\beta\log(1+T_{rt}/P_{rt})+\varepsilon_{rt}.
\]

El coeficiente \(\beta\) se considera una **asociación condicional**, sin interpretación causal. El número de grupos es muy reducido, por lo que no se realizará inferencia estadística formal ni se ofrecerán estrellas de significación.

El archivo \`code/run_analysis.py\` calcula el estimador de efectos fijos por doble centrado y guarda resultados automáticamente en \`outputs/\`. El programa emplea solo bibliotecas estándar de Python.

## 4. Resultados

Según los resultados de la ejecución, el coeficiente de intensidad turística es **0,1800**. La asociación es positiva y económicamente importante, aunque podría reflejar cambios sectoriales y otros factores omitidos. Con la especificación log(1+intensidad), el coeficiente no equivale exactamente a una elasticidad de los salarios respecto al número de turistas.

La **tabla 1** presenta los salarios reales de 2024 para los dos territorios ilustrativos:

| Región | Salario real anual (EUR) |
|---|---:|
| Baleares_SIM | 29.500,00 |
| Canarias_SIM | 28.300,00 |

Fuente: cálculos reproducibles del autor sobre el panel sintético. Los archivos originales y la rutina aparecen en la carpeta del proyecto.

La **figura 1** muestra la evolución del salario **nominal** anual, antes de corregir por el IPC:

![Figura 1. Evolución salarial de dos regiones simuladas](../outputs/figure_real_wage.svg)

Los resultados respaldan el mecanismo de demanda laboral: más turistas elevan los salarios reales regionales. No obstante, la interpretación es descriptiva y no se debe presentar como causal.

## 5. Limitaciones y discusión

Los datos sintéticos no permiten sacar conclusiones sobre las Islas Baleares reales. La pregunta sigue siendo limitada desde la perspectiva económica y faltan lecturas científicas fundamentales, así como una estrategia que permita distinguir mecanismos de demanda laboral, oferta y composición.

El paquete contiene el script para repetir la estimación, un diccionario y el documento de resultados. Se considera **reproducido y verificado** todo lo que aparece en este texto por el mero hecho de que exista el código.

## 6. Conclusión

Este ejercicio demuestra que es posible producir un análisis regional organizado con archivos de datos y programas ejecutables. La interpretación del coeficiente debe seguir siendo prudente. En un TFG real habría que incorporar fuentes oficiales y explicar de forma más sólida la relevancia de los resultados.

## Bibliografía

González, L., y Surovtseva, T. (2024). *Do More Tourists Promote Local Employment?* IZA Discussion Paper 17518.

Caparrós Alcaraz, F. (2018). Estudio sobre mercado laboral balear. Referencia bibliográfica incompleta.
