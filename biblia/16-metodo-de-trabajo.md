# 16. Método de trabajo: el ciclo de capítulo

> **Documento operativo.** Define cómo se escribe esta novela: capítulo a capítulo, volumen por volumen, con una bitácora de continuidad que evita los agujeros del método.

## Por qué escribimos así (decisión del autor)

Se descarta la estructura completa de los 30 capítulos de antemano. En su lugar:

> **Primero el Volumen 1. Un capítulo a la vez.**

**La razón:** planear 30 capítulos y descubrir a mitad del camino que un personaje habla distinto, que una ruta no funciona o que un aspecto importante cambió obligaría a rehacer la estructura desde cero. La voz de un personaje no existe hasta que se escribe; el mejor plan sigue siendo **el que se escribe**.

**El riesgo que este método sí exige resolver:** la continuidad. Escribir sin estructura puede dejar objetos, rutas, reglas y promesas colgando. Para eso existe la bitácora (abajo).

## El ciclo de trabajo

Cada capítulo pasa por cuatro pasos. Ninguno se salta.

### Paso 1 — Ficha de capítulo
El agente redacta una ficha breve con los campos del bloque siguiente y se la presenta al autor. **Sin ficha aprobada, no se escribe.**

### Paso 2 — Aprobación
El autor la revisa, pide cambios, cambia el orden si hace falta o pide otra propuesta. La ficha se ajusta hasta que él diga que sí.

### Paso 3 — Redacción
Se escribe el capítulo completo. **Extensión objetivo: 4,500–5,000 palabras**, con piso de 4,000 y techo de 5,500 (decisión aprobada en la sección 18). El capítulo 1 puede pasar el techo: ya está aprobado como el más largo.

### Paso 4 — Revisión, bitácora y el rótulo «Estado»
Se actualiza la bitácora de continuidad con todo lo que el capítulo dejó vivo y **se revisa el renglón del encabezado**, que lleva la extensión y el estado de la pieza. El campo Estado solo tiene tres valores:

1. **«primer borrador»** — mientras el capítulo se acaba de escribir y todavía no pasa la revisión.
2. **«revisado; pendiente de aprobación del autor»** — después de la revisión de estilo, canon y texto a voz, y hasta que el autor dé el visto bueno.
3. **«aprobado por el autor»** — cuando el autor lo aprueba. A partir de ahí, cualquier cambio de fondo se le consulta.

*Lección del 12 de octubre de 2026:* los rótulos se quedaron en «primer borrador» después de la revisión y de la aprobación del capítulo 1. **Al cerrar cada paso del ciclo, se revisa el encabezado**, no solo la bitácora.

## Regla de accesibilidad: el texto tiene que poder leerse en voz alta

**Instrucción del autor (12 de octubre de 2026):** cada capítulo se escribe de manera que **una aplicación de texto a voz pueda leerlo sin problemas, con sus pausas naturales y sin confundir caracteres.**

### Reglas de redacción

1. **Sin marcas de formato en el cuerpo del texto.** Nada de asteriscos para negritas o cursivas, ni guiones bajos, ni acentos graves, ni almohadillas: los lectores de voz los leen como «asterisco» o los omiten mal. Si algo necesita énfasis, se logra con la redacción, no con símbolos.
2. **Puntos suspensivos siempre con tres puntos (...).** Nunca el carácter único de puntos suspensivos (…), que algunos lectores anuncian como «puntos suspensivos».
3. **Números escritos con letra en el texto narrativo.** «Cuarenta y dos», no «42». Las cifras con separadores («1,660») se leen mal o se interpretan como decimales.
4. **Nada de mayúsculas sostenidas en frases largas.** Una mayúscula de grito se tolera en una palabra suelta («¡MEGUMIN!»), pero las frases gritadas se escriben en caja normal y el grito lo llevan los signos.
5. **Documentos del mundo entre comillas angulares** («...»), no en cursiva. Los avisos, listas y cartas se leen así como una cita clara y con pausa natural.
6. **Frases cortas y puntuación generosa.** Un lector de voz respira donde hay punto. Los párrafos con diez comas seguidas se atropellan.
7. **Sin abreviaturas ni símbolos raros.** Nada de «Sr.», «pág.», barras, asteriscos decorativos ni emojis dentro de la narración.
8. **Diálogo con raya (—) al inicio de línea.** Es la convención del español y los lectores de voz la ignoran correctamente, marcando el cambio de turno con una pausa. Lo que se evita es la raya intercalada a media frase en exceso, porque desordena la entonación.
9. **Nombres extranjeros sin diacríticos raros.** Se escriben de forma que un lector en español los pueda pronunciar.
10. **Encabezado limpio.** El bloque de título del capítulo va en texto plano (título, obra, volumen, extensión y estado), sin negritas ni viñetas.
11. **Los archivos se guardan en UTF-8 con BOM (UTF-8-BOM).** Lo pide la aplicación con la que el autor escucha los capítulos (**ElevenReader**, pedido del 12 de octubre de 2026): sin el BOM, no narra los documentos como deben ir. El BOM no se ve y no cambia una sola letra del texto; solo son tres bytes al inicio del archivo. Como es fácil que un editor lo borre al guardar, **después de cualquier edición a una pieza se vuelve a aplicar**.

### Aplicación

- Estas reglas se aplican **a todos los capítulos** desde el capítulo 5.
- **El 12 de octubre de 2026 las siete piezas del volumen 1 se convirtieron a UTF-8-BOM** (prólogo y capítulos 1 a 6), tras el aviso del autor sobre ElevenReader. El contenido quedó idéntico: los conteos de palabras no se movieron ni una unidad.
- Los capítulos 0 a 4 se **normalizaron** el 12 de octubre de 2026 para cumplirlas, sin cambiar una sola palabra de la historia: solo se limpiaron símbolos, se pasaron las mayúsculas gritadas a caja normal y se convirtieron los puntos suspensivos.

### Herramientas

En la carpeta `herramientas/` viven los dos script que se corren a mano:

- **`utf8-bom.py`** — pasa a UTF-8-BOM todos los `.md` de `novela/` (o los archivos que se le indiquen). Es idempotente: nunca deja doble BOM. Se corre con `python3 herramientas/utf8-bom.py`.
- **`revisar-capitulos.py`** — revisa las piezas narrativas: que tengan BOM, que la extensión del encabezado coincida con el cuerpo y que se cumplan las reglas de texto a voz de arriba (sin marcas de formato, puntos suspensivos de tres puntos, sin abreviaturas, sin emojis, sin mayúsculas sostenidas, sin dobles espacios). Las fichas solo se revisan de formato. Se corre con `python3 herramientas/revisar-capitulos.py`; sale con error si encuentra algo que corregir, así que sirve de filtro **antes de cada commit**.

## La ficha de capítulo (plantilla)

```
CAPÍTULO N.º __ — «Título»

Volumen: __ | Extensión objetivo: __ palabras
Foco: ¿de quién es el capítulo?
Deseo local: ¿qué quiere Jesús (o el foco) en este capítulo?
Obstáculo: ¿qué se lo impide?
Formato narrativo: (narración lineal, diario, reporte del gremio, carta, etc.)
Referencia del canon: ¿qué evento del anime se usa, si alguno? (o "material original")
Cambio al cierre: ¿qué es distinto al terminar el capítulo?
Lo que el lector aprende: ¿qué dato, regla o vínculo queda establecido?
Gancho: ¿qué invita a leer el siguiente?
Rutas: ¿qué heroína avanza? ¿qué bandera, beso o consecuencia?
Objetos: ¿qué aparece y qué le pasa? (playera, celular, llave, libro de banderas)
Continuidad: ¿qué NO se puede olvidar de este capítulo en los siguientes?
```

## La bitácora de continuidad

Es la red de seguridad del método. Vive en la sección 17 y se actualiza **después de cada capítulo escrito**. Registra:

- **Objetos:** dónde está cada uno y en qué estado (la playera, el celular, la llave, el libro de banderas).
- **Rutas:** qué sabe cada heroína, en qué punto está su vínculo, qué pendientes dejó.
- **Mundo:** reglas, distancias, deudas, reputación de Jesús en Axel.
- **Promesas:** toda cosa que el texto insinúa y todavía no paga.
- **Estado físico y emocional de Jesús.**
- **Estado de ánimo general del grupo.**

**Regla de oro:** si la bitácora y el capítulo se contradicen, manda el capítulo — pero se corrige la bitácora **el mismo día**, no después.

## Reglas de la dinámica

1. **Se escribe un capítulo a la vez.** Nada de adelantar capítulos ni de escribir dos a la vez.
2. **La estructura se descubre, se registra y se respeta.** No hay plan de 30 capítulos, pero sí hay **anclas ya aprobadas** que no se mueven: los tres clímax de volumen, el diseño del capítulo 1, el cierre del epílogo y las decisiones del tablero.
3. **Todo destino ya aprobado sigue en pie.** El clímax del Vol. 1 (el Destructor) y el arco de la playera son destino, no sugerencia.
4. **Si una idea nueva cambia algo ya escrito, se anota y se decide con calma.** No se reescribe por impulso ni se ignora.
5. **Al cerrar cada volumen** se hace una revisión de conjunto: qué quedó, qué falta, qué se prometió y no se pagó.
6. **Dinámica de escritura en tres pasos (pedida por el autor el 13 de octubre de 2026):**
   1. **Confirmar rápido los puntos más importantes del capítulo anterior** (los que el nuevo capítulo tiene que respetar: fechas, objetos, promesas, estado de cada personaje).
   2. **Escribir el borrador completo del capítulo siguiente**, sin pulir de más: primero la idea central y la escena.
   3. **Pulir detalles y narración con apoyo de la biblia y del internet**, cotejando canon, nombres y continuidad. Puede tomar más tiempo; **se prefiere lento y seguro a rápido con errores** (palabras del autor).
7. **Ningún nombre propio nuevo entra al texto sin cotejarse contra el canon** (personajes, lugares, títulos). Si el nombre es original, se marca como original en la bitácora, con quién es y de dónde salió. **Regla nacida del error «Mabel» (13 de octubre de 2026):** un nombre inventado se coló en el más allá del capítulo 1 y en dos capítulos más, y hubo que retirarlo. No se repite.

**Regla 8 (nacida de la revisión de conjunto del 13 de octubre de 2026): las muletillas de la voz se auditan.**
El narrador tiene tics que le dan carácter —«mi hermano», «ya lo saben», «de verdad»—, y esos tics, cuando se repiten seguido, dejan de dar carácter y se vuelven ruido. Al cerrar el Vol. 1 se contaron y se podaron: «mi hermano» pasó de 1 vez cada ~180 palabras (cap. 10) a 1 cada ~700, que es la densidad de los capítulos aprobados. **En cada cierre de volumen se cuentan los tics y se decide cuáles se quedan.** Los que se quedan son los que cargan emoción (la última línea de una escena, el momento en que alguien se muere); los que se van son los de relleno.

**Regla 9 (13 de octubre de 2026): las palabras de México viven en la voz, no en el mundo.**
Jesús es mexicano-japonés y su narración está llena de casa: «nomás», «mijo», «cancha», «órale», «el pasillo de un cine». Eso es él y se queda. Lo que **no** se hace es poner cosas de la Tierra en la boca de la gente de este mundo: aquí nadie toma tequila, nadie come tacos y nadie escucha radio, porque esos objetos no existen en este mundo. La prueba es simple: **¿lo dice el narrador comparando, o lo dice un personaje como si existiera?** Si es el narrador, adelante; si es un personaje de Axel, se cambia por lo que sí hay (aguardiente, pan, vino de las fiestas).

**Aplicación (13 de octubre de 2026, al sellar el Vol. 1):** el autor eligió la versión **estricta** para todo el volumen y la regla se pasó al texto: se limpiaron los mexicanismos en boca de la gente del mundo —Luna («pa' qué», «órale», «mijo»), el señor barbón («órale», «pa qué», «nomás»), Aqua («pa' cuatro», «nomás», «ahorita mismo»), Wiz («mija»), Beldia («nomás», «orita», «ahorita») y el señor de la cola («mijo», «nomás»)— y el habla mexicana se quedó donde debe: en el narrador y en la boca de Jesús, que es de Guadalajara. En el epílogo, «la señora del pan me dice mijo» pasó a «me dice hijo».

## Tablero del Volumen 1 (capítulos 1–10)

| Cap. | Estado | Título | Nota |
| --- | --- | --- | --- |
| **Prólogo** | 🟩 Aprobado | «Un lugar sin ventanas» | 954 palabras · revisado y aprobado por el autor |
| 1 | 🟩 Aprobado | «Todo lo que alcancé a ver desde aquí» | 7,127 palabras · el más largo · revisado y aprobado por el autor |
| 2 | 🟩 Aprobado | «Un cuarto con ventana» | 5,217 palabras · revisado y aprobado · introduce a Luna y paga la ventana |
| 3 | 🟩 Aprobado | «La muchacha que hacía temblar los cerros» | 5,490 palabras · revisado y aprobado · entra Megumin; el grupo ya es cuatro |
| 4 | 🟩 Aprobado | «La gente que se pone enfrente» | 5,077 palabras · revisado y aprobado · entra Darkness; cuadrilla completa |
| 5 | 🟩 Aprobado | «El señor de la casa del cerro» | 5,030 palabras · revisado y aprobado · Beldia y la maldición |
| 6 | 🟩 Aprobado | «El otro elegido» | 5,148 palabras · revisado y aprobado · el lago, Mitsurugi y el séptimo día |
| 7 | 🟩 Aprobado | «La gente que sí va» | 5,004 palabras · revisado y aprobado por el autor · cierra el séptimo día |
| 8 | 🟩 Aprobado | «No me dolió» | 5,499 palabras · revisado y aprobado por el autor · la muerte y el regreso, como el canon |
| 9 | 🟩 Aprobado | «El camino del norte» | 8,343 palabras · **aprobado por el autor el 13 de octubre de 2026** · entra Wiz; se descubre que el Destructor rompió el paso |
| 10 | 🟩 Aprobado | «El segundo trueno» | 8,889 palabras · **aprobado por el autor el 13 de octubre de 2026** · el Destructor; la defensa de Axel y el teletransporte del coronatita. **No se recortó** |
| **Epílogo** | 🟩 Aprobado | «Los que vuelven» | 3,257 palabras · **aprobado por el autor el 13 de octubre de 2026** · la levantada, el nombre de la cuadrilla y los caballeros del rey |

**Leyenda:** ⬜ vacío · 🟨 en diseño · 🟦 en redacción o revisión (pendiente de aprobación) · 🟩 aprobado por el autor, cerrado o fijado

**Estructura fija del volumen:** prólogo corto + 10 capítulos + epílogo. **No hay páginas de interludio** (decisión del autor, sección 18).

**Revisión del volumen:** completada el 12 de octubre de 2026 sobre las siete piezas escritas (aspecto físico, voces, ambientación, canon, ortografía y texto a voz). Informe para el autor: `REVISION-VOLUMEN-1.md`. **Decisiones del autor: las cuatro quedaron resueltas el 12 de octubre y están aplicadas.**

**Capítulo 7 (12 de octubre de 2026):** escrito, revisado y **aprobado por el autor** (ficha incluida). Siguiente en fila: el capítulo 8, con su ficha primero.

**Capítulo 8 (12 de octubre de 2026):** escrito, revisado y **aprobado por el autor** (ficha incluida).

**Capítulo 9 (12 de octubre de 2026):** escrito y revisado (ficha y texto entregados juntos, con las cuatro decisiones de diseño ya aprobadas por el autor); **aprobado por el autor el 13 de octubre de 2026.** **No se recortó:** se dejó largo, según la indicación del autor del 12 de octubre («si el capítulo se extiende de más, no lo recortes, déjalo así»).

**Cierre del Volumen 1 (13 de octubre de 2026):** el autor pidió «terminemos con el Volumen I» y con eso se escribió **el capítulo 10 («El segundo trueno», 8,889 palabras)** y **el epílogo («Los que vuelven», 3,257 palabras)**, los dos con la dinámica de tres pasos (borrador completo, después pulido con biblia e internet) y los dos **revisados y aprobados por el autor el 13 de octubre de 2026**. Cuatro decisiones se tomaron con el autor ese día: los dos usos de Drenar del canon **más un tercero «de corazón»**; **Megumin se lastima de verdad** (la pierna, cicatriz del volumen y pendiente del Vol. 2); **la acusación de traición cae sobre Jesús**; y el epílogo **«todo junto»** (fiesta, nombre nuevo y caballeros). El nombre de la cuadrilla queda fijado en **«Los que vuelven»**, elegido por el autor. Con esto el volumen queda **completo y sellado**: el 13 de octubre el autor aprobó el capítulo 9, el capítulo 10 y el epílogo, así que **las doce piezas están aprobadas**.

**Después de la aprobación (13 de octubre de 2026):** la **revisión de conjunto del Vol. 1** ya se hizo sobre las doce piezas (informe `REVISION-VOLUMEN-1-CIERRE.md`), la auditoría de nombres pasó a limpio y las decisiones que el informe pedía quedaron cerradas con el autor ese mismo día: **Darkness revela su identidad en privado en el Vol. 2**; **el apodo de Jesús cae en escena en el Vol. 2**; el rango de Aqua se escribe **archisacerdotisa**; y **el Vol. 2 abre con el juicio de Sena**. **Carpeta del Volumen 2 abierta** (`novela/volumen-2/`), con su `FICHAS.md` esperando: **pendiente inmediato, la ficha del capítulo 11.**

## Estado de los volúmenes

| Volumen | Capítulos | Estado |
| --- | --- | --- |
| **Vol. 1** | 1–10 | ✅ **Terminado y aprobado por el autor** (12 de 12 piezas, 13 de octubre de 2026) |
| **Vol. 2** | 11–20 | 🔨 En diseño — es el volumen activo: **abre con el juicio de Sena**; incluirá el capítulo de fútbol ✅ y el clímax de Hans ✅ |
| **Vol. 3** | 21–30 | ⏸️ Pendiente — incluirá la boda de Darkness ✅ y el cierre del hilo de los padres ✅ |
