# Tres indicadores independientes v0.2

Son **formativos, independientes y no acumulables**. Solo el primero es la rúbrica científica de 100 puntos. Los otros dos son diagnósticos y NO se suman, promedian ni sustituyen la nota del TFG.

## I. Calidad científica del TFG (0–10)

Usar exclusivamente \`references/rubrica.md\`, con criterios A–H, modalidad, evidencia vigente, topes y nota relativa a etapa.

## II. Reproducibilidad técnica (0–10)

Puntuar **solo si se ha examinado un paquete suficientemente completo**. La presencia de carpetas por sí sola no demuestra reproducción. Asignar **no evaluable** si no hay artefactos, permisos o herramientas para verificar. Si no se ejecuta, puede ofrecerse diagnóstico estructural, pero **no nota numérica de ejecución**.

| Dimensión | Puntos | Criterio |
|---|---:|---|
| T1 Acceso y procedencia | 2 | Fuentes y permisos, datos o instrucciones reproducibles |
| T2 Entorno | 2 | Versiones, dependencias, instrucciones y configuración |
| T3 Ejecución | 3 | Código ejecutado; pruebas; errores documentados; salidas regeneradas |
| T4 Determinismo y seguimiento | 2 | Salidas comparadas, semillas, hashes o tolerancias explícitas |
| T5 Documentación y trazabilidad | 1 | README, diccionario y mapa script-tabla |

Los datos sintéticos **pueden recibir nota técnica alta** si están correctamente documentados. No se debe penalizar por ser sintéticos en este indicador; sí debe advertirse que no justifican conclusiones sobre datos oficiales reales.

## III. Correspondencia manuscrito–resultados (0–10)

No es una nota de reproducción técnica. Exige contrastar texto, tablas, figuras, unidades y fuentes con sus salidas. Si el texto o resultados no están accesibles, asignar **no evaluable**; no inventar puntuación.

| Dimensión | Puntos | Criterio |
|---|---:|---|
| C1 Números y muestra | 4 | Coeficientes, N, periodos y valores reproducidos coinciden |
| C2 Figuras y tablas | 2 | Leyendas, ejes, unidades y cifras correctas |
| C3 Interpretación | 2 | Conclusiones compatibles con evidencia y diseño |
| C4 Trazabilidad | 2 | Correspondencia explícita entre afirmaciones, scripts y salidas |

Para puntuaciones bajas, citar **discrepancias verificadas** y su fuente. No afirmar manipulación o fraude sin pruebas; solicitar explicación y trasladar cuestiones de integridad al tutor humano. La coincidencia numérica no demuestra causalidad ni validez externa.

## Informe obligatorio

Mostrar tres líneas distintas: **calidad científica: N/10 o no evaluable; reproducibilidad técnica: N/10 o no evaluable; correspondencia manuscrito–resultados: N/10 o no evaluable**, seguidas del alcance, evidencia examinada y límites. La puntuación técnica nunca compensa una debilidad científica.
