# Caso ficticio v3: ejecución y auditoría reproducible

**Datos totalmente sintéticos; no son cifras oficiales ni resultados reales de Baleares.**

Este caso es una prueba ciega para el Tutor IA del TFG de Economía UIB. Incluye un manuscrito, 64 observaciones sintéticas, un diccionario y un script sin dependencias de terceros. Se ejecuta con Python 3.9+.

## Reproducción

Situado en esta carpeta:

```bash
python3 code/run_analysis.py
python3 -m unittest discover -s code -p 'test_*.py'
```

El script escribe `outputs/summary.json`, `outputs/regional_2024.csv` y `outputs/figure_real_wage.svg` (se incluyen resultados generados con el mismo script). Solo se permite afirmar que un resultado se ha reproducido si se ha ejecutado el código y contrastado con el documento.

## Advertencias

La simulación no procede de INE, FRONTUR ni EPA. Los nombres geográficos son ilustrativos. Ninguna observación debe utilizarse para conclusiones económicas reales sobre España.

El manuscrito tiene deficiencias deliberadas. **No se enumeran aquí** para preservar el carácter ciego de la prueba.

## Archivos

- `data/synthetic_panel.csv`: fuente artificial, no se modifica durante la ejecución
- `data/DATA_DICTIONARY.md`: unidades y procedencia
- `code/run_analysis.py`: estimación descriptiva y generación de archivos
- `code/test_analysis.py`: pruebas de estructura y finitud, no validez económica
- `outputs/`: salidas generadas y publicadas como referencia
- `manuscript/tfg_results_v3.md`: documento a contrastar
