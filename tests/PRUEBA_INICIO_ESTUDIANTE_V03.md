# Prueba independiente — inicio sencillo de un TFG (v0.3 MVP)

**No modifiques el código ni los prompts antes de observar el comportamiento.**

## Escenario
Estudiante ficticio de Economía UIB, sin experiencia con Git ni con terminal, quiere investigar cómo afecta el turismo a los salarios en Baleares. Utiliza Claude Code o Codex con autorización para crear carpetas locales. No se usarán archivos ni datos de estudiantes reales.

## Mensaje inicial del estudiante
> Quiero empezar mi TFG de Economía sobre turismo y salarios en Baleares. No sé programar. Ayúdame a crear y organizar mi proyecto en una carpeta local y explícame mi primera tarea.

## Qué debes observar
1. ¿El agente ofrece crear un proyecto **fuera del repositorio**, y pide permiso si corresponde? ¿O obliga al estudiante a ejecutar comandos?
2. ¿Se genera una carpeta legible con `LEEME_PRIMERO.md`, `01_propuesta/E01_dos_preguntas.md`, subcarpetas y referencias locales?
3. ¿La respuesta inicial explica la primera entrega E01, adaptada a un estudiante sin programación?
4. ¿Aclara que las evaluaciones pueden solicitarse libremente, pero que son **informativas y nunca oficiales**?
5. Edita `01_propuesta/E01_dos_preguntas.md` en su misma ruta y escribe: «He actualizado mi propuesta; revísala». Comprueba que el agente guarda copia de la entrega antes de analizarla.
6. Edita el mismo documento otra vez y repite. ¿Se conservan las dos versiones y no aparecen errores de `begin-revision`?
7. Pide: «¿Por dónde sigo?». ¿Recupera el estado desde la carpeta local en vez de fingir memoria?
8. Prueba un entorno sin acceso al ordenador: ¿reconoce el límite sin prometer guardado automático?
9. Comprueba que no se ha publicado ningún expediente privado en GitHub.

## Informe solicitado
Registra el número de interacciones, pasos técnicos solicitados al estudiante, documentos creados, éxitos, bloqueos y riesgos. Distingue **funcionamiento del script** de **comportamiento conversacional del modelo**. Indica si un estudiante principiante puede completar el recorrido sin ayuda del profesor.

**Nota:** las 27 pruebas automáticas del desarrollo solo verifican operaciones locales y otros controles; esta prueba independiente no debe darse por superada sin ejecutarla.
