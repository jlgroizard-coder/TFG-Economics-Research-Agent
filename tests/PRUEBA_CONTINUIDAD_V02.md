# Prueba v0.2 — continuidad de expediente (ciega)

## Escenario A: un capítulo no se entrega otra vez
En un expediente privado, el estudiante presentó en v2 una revisión de literatura verificada. En v3 solo aporta un capítulo de resultados. El agente debe buscar la revisión de v2 y mantener su puntuación **si comprueba que sigue vigente y accesible**. Si no está disponible, debe informar \`no_aportada_ahora\` y evitar reducir la calificación global por omisión del archivo.

## Escenario B: cambio de investigación
Si el estudiante cambia la pregunta, el país, el periodo o las variables, los archivos anteriores pueden quedar **desactualizados**. No conservar puntos cuando la evidencia ya no es pertinente.

## Escenario C: auditoría técnica
\`tests/fixtures/v3_project/\` reproduce exactamente los archivos publicados pero contradice el manuscrito. Debe salir una evaluación técnica positiva y una puntuación baja de correspondencia; la calidad científica no se infiere de la técnica.

## Mensaje de prueba
> Evalúa el expediente privado del estudiante a través de sus revisiones, no solo el último documento. Se ha aportado una v3 de resultados, pero su revisión de literatura está en v2. Comprueba cuáles evidencias siguen vigentes y cuáles no están accesibles; si faltan piezas esenciales, no calcules una nota global definitiva. Da por separado la calidad científica, la reproducibilidad técnica y la correspondencia manuscrito–resultados. Explica el alcance de cada una.

No publicar expedientes reales para probar el agente; utilizar datos ficticios o trabajos anonimizados con autorización y permisos adecuados.

## Escenario D: revisión legítima del mismo archivo (v0.2.3)

1. Registrar y evaluar `02_literatura/revision.md` en v2.
2. Ejecutar `begin-revision` **antes** de editar; comprobar que se ha preservado el original y que la nota anterior es obsoleta.
3. Editar **la misma ruta**, registrar artefacto v3 y revalidar criterio B con evidencia localizable.
4. Confirmar que puede registrarse nueva evaluación global si no existen otras evidencias bloqueadas.
5. Alterar la copia histórica en un segundo expediente de prueba: la nota global debe ser rechazada.
6. Intentar editar sin `begin-revision`: el programa debe rechazar la revisión y exigir restaurar el original.

No convertir el marcado `vigente_verificada` en una certificación automática de lectura o evaluación humana.
