# Rúbrica formativa — TFG Economía UIB (100 puntos)

**No sustituye la evaluación oficial UIB.** Cada punto requiere evidencia; calificar un texto formalmente bonito sin sustancia científica no merece una nota alta.

| Criterio | Máx. | Evidencia para nota alta |
|---|---:|---|
| A. Pregunta y contribución | 15 | Pregunta delimitada, relevancia y contribución viable |
| B. Literatura científica | 15 | Artículos originales comprendidos, comparados y citados correctamente |
| C. Teoría e hipótesis | 15 | Mecanismos, supuestos y predicciones económicas fundamentadas |
| D. Metodología | 15 | Diseño adecuado, identificación o límites de inferencia claros |
| E. Datos/evidencia o validación teórica | 10 | Fuentes, calidad, procesado o demostración transparente |
| F. Resultados e interpretación | 10 | Resultados pertinentes, magnitudes y limitaciones justificadas |
| G. Reproducibilidad | 10 | Código/derivaciones, fuentes, documentación y verificaciones |
| H. Escritura, estructura y requisitos | 10 | Argumentación, claridad, referencias y formato UIB |
| **Total** | **100** | **Nota /10 = puntos /10** |

## Descriptores por criterio
0% ausente o erróneo; 25% superficial; 50% aceptable con carencias importantes; 70% sólido; 85% excelente para grado; 100% excepcional para grado y con evidencia verificable. Justifica puntajes con secciones o archivos, no impresiones.

## Doble calificación
- **Nota completa actual**: puntos demostrados sobre 100; dimensiones sin evidencia = 0. Si no hay material evaluable, indicar «no evaluable».
- **Nota relativa a la etapa**: puntos demostrados en dimensiones pertinentes / máximos exigibles en esa etapa × 10. No constituye pronóstico de nota final.

| Etapa | Máximos exigibles (subcriterios) | Total |
|---|---|---:|
| E01 | A15, C5, H5 | 25 |
| E02 | A15, B15, C10, H5 | 45 |
| E03–E04 | A15, B15, C15, D15, E5, H10 | 75 |
| E05–E08 | A15, B15, C15, D15, E10, F5, G5, H10 | 90 |
| E09–E14 | Todos | 100 |

### Regla de conversión obligatoria entre escalas

Para evitar que cada modelo invente un procedimiento, aplicar siempre el siguiente algoritmo:

1. Asignar una puntuación completa `s_i` en cada dimensión A–H, entre 0 y su máximo `M_i`, con evidencia.
2. Para la **nota de etapa**, obtener de la tabla anterior el máximo exigible `m_i` por dimensión (0 si todavía no se exige). Calcular **`e_i = s_i × m_i / M_i`**, conservando al menos dos decimales internamente.
3. Calcular **`nota_completa = Σ s_i / 10`** y **`nota_etapa = 10 × Σ e_i / Σ m_i`**.
4. Aplicar el tope grave pertinente sobre ambas notas si se refiere a un requisito ya exigible; no imponer por adelantado topes por resultados o reproducibilidad todavía no exigibles, salvo fabricación de evidencia o faltas de integridad presentes.
5. Mostrar los `s_i`, `e_i`, `M_i`, `m_i`, denominadores y topes, con redondeo final a **una cifra decimal**. No redondear antes de calcular.

**Ejemplo E03:** si E (datos) obtiene `s_E = 2/10`, su puntuación para la etapa es `e_E = 2 × 5/10 = 1/5`. Esta regla es **proporcional y predeterminada**, no una decisión discrecional del asistente.

En etapas tempranas, explicar criterios aún no exigibles. Evitar comparar directamente la nota de etapa con una nota del TFG final.

## Topes por fallos graves
- Sin pregunta económica clara: máximo 5,9/10.
- Sin literatura académica original realmente trabajada, o citas clave inventadas: máximo 5,9/10; fraude/plagio requiere evaluación humana y no debe premiarse.
- Metodología incompatible con la pregunta, causalidad central injustificada o resultados no sustentados: máximo 5,9/10.
- TFG empírico final sin datos/código trazables ni explicación de restricciones: máximo 7,0/10.
- Conclusiones incompatibles con resultados: máximo 6,9/10.
- No otorgues sobresaliente *final* sin evidencia del trabajo terminado.

Aplica el tope más bajo tras sumar criterios y explica qué evidencia permitiría levantarlo.

## Modalidades
Para teoría, E evalúa pruebas y su consistencia; G evalúa trazabilidad de derivaciones/simulaciones. Para revisión crítica, E evalúa corpus y selección; G evalúa posibilidad de replicar la búsqueda y síntesis. No exijas econometría donde no corresponda.

## Interpretación
0–4,9 insuficiente; 5–6,9 básico; 7–7,9 notable; 8–8,9 muy sólido; 9–10 excepcional para nivel de grado. Nunca redondear estratégicamente para subir de tramo.


## Alcance y disponibilidad de evidencia (v0.2)
La fórmula anterior solo se aplica a un **expediente completo evaluable**. Si una sección no acompaña al último envío, consultar documentos anteriores accesibles y verificar su vigencia antes de puntuar. Si evidencia esencial no puede reabrirse, indicar `no evaluable` para esa dimensión y una **evaluación provisional**, sin convertir automáticamente el ausente en cero ni presentar una nueva nota global definitiva. Los indicadores técnicos independientes se encuentran en `references/indicadores-tecnicos.md`.
