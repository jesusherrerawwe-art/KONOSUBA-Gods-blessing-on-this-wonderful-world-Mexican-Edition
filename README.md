# KONOSUBA — God’s blessing on this wonderful world! (Mexican Edition)

![Póster de KONOSUBA — Mexican Edition](poster.webp)

## Sobre la obra

Esta es una **novela ligera original inspirada en el universo de *KonoSuba!***, con una aventura propia, humor disparatado y el espíritu irreverente que caracteriza a este maravilloso mundo.

### Título de la obra

> ## 『**KONOSUBA! — La bendición de Jesús en este maravilloso mundo**』
> ### *(Edición Mexicana)*

**Por qué este título:** el título oficial de la serie original es *God's Blessing on This Wonderful World!* — *«La bendición de Dios en este maravilloso mundo»*. Aquí el protagonista **se llama Jesús**, así que el juego de palabras funciona solo, en los dos sentidos: la bendición que él recibe y la bendición que él trae. Es un homenaje, no una burla.

**Título aprobado por el autor el 12 de octubre de 2026.** Las alternativas que estuvieron en la mesa quedaron descartadas como nombre de la obra, aunque las dos siguen viviendo dentro del texto: «El Rebaño Sagrado» es el apodo de la afición de las Chivas y «Un cuarto con ventana» es el título del capítulo 2.

## La novela

El texto de la novela vive en la carpeta [`novela/`](novela/), separada de la biblia porque es el entregable final.

### Volumen 1 — terminado y aprobado (12 de 12 piezas, 65,035 palabras)

| # | Pieza | Título | Palabras | Estado |
| --- | --- | --- | --- | --- |
| 00 | [Prólogo](novela/volumen-1/00-prologo.md) | «Un lugar sin ventanas» | 954 | aprobado por el autor |
| 01 | [Capítulo 1](novela/volumen-1/01-capitulo-1.md) | «Todo lo que alcancé a ver desde aquí» | 7,127 | aprobado por el autor |
| 02 | [Capítulo 2](novela/volumen-1/02-capitulo-2.md) | «Un cuarto con ventana» | 5,217 | aprobado por el autor |
| 03 | [Capítulo 3](novela/volumen-1/03-capitulo-3.md) | «La muchacha que hacía temblar los cerros» | 5,490 | aprobado por el autor |
| 04 | [Capítulo 4](novela/volumen-1/04-capitulo-4.md) | «La gente que se pone enfrente» | 5,077 | aprobado por el autor |
| 05 | [Capítulo 5](novela/volumen-1/05-capitulo-5.md) | «El señor de la casa del cerro» | 5,030 | aprobado por el autor |
| 06 | [Capítulo 6](novela/volumen-1/06-capitulo-6.md) | «El otro elegido» | 5,148 | aprobado por el autor |
| 07 | [Capítulo 7](novela/volumen-1/07-capitulo-7.md) | «La gente que sí va» | 5,004 | aprobado por el autor |
| 08 | [Capítulo 8](novela/volumen-1/08-capitulo-8.md) | «No me dolió» | 5,499 | aprobado por el autor |
| 09 | [Capítulo 9](novela/volumen-1/09-capitulo-9.md) | «El camino del norte» | 8,343 | aprobado por el autor |
| 10 | [Capítulo 10](novela/volumen-1/10-capitulo-10.md) | «El segundo trueno» | 8,889 | aprobado por el autor |
| 11 | [Epílogo](novela/volumen-1/11-epilogo.md) | «Los que vuelven» | 3,257 | aprobado por el autor |

### Volumen 2 — en escritura (capítulos 11 a 20)

| # | Pieza | Título | Palabras | Estado |
| --- | --- | --- | --- | --- |
| 11 | [Capítulo 11](novela/volumen-2/11-capitulo-11.md) | «La verdad en voz alta» | 5,560 | aprobado por el autor |
| 12 | [Capítulo 12](novela/volumen-2/12-capitulo-12.md) | «La cuenta» | 7,237 | aprobado por el autor |
| 13 | Capítulo 13 | pendiente de ficha | — | no escrito |

Documentos de trabajo del volumen: [`volumen-1/FICHAS.md`](novela/volumen-1/FICHAS.md) (fichas de diseño de cada pieza) y [`volumen-2/00-resumen-volumen-1.md`](novela/volumen-2/00-resumen-volumen-1.md) + [`volumen-2/FICHAS.md`](novela/volumen-2/FICHAS.md).

**Total de narrativa escrita y aprobada: 77,832 palabras.**

Los archivos de la novela llevan **UTF-8 con BOM (UTF-8-BOM)**, el formato que usaba la aplicación de lectura en voz alta (**ElevenReader**). **El requisito quedó revocado por el autor el 17 de octubre de 2026:** las piezas nuevas se escriben **sin BOM** y las viejas conservan el que ya tienen. `python3 herramientas/utf8-bom.py` sirve para convertir si alguna vez hace falta, y `python3 herramientas/revisar-capitulos.py` revisa formato, extensión y reglas de lectura en voz alta (sin exigir el BOM).

**Cómo se escriben los diálogos (decisión del autor, 17 de octubre de 2026):** **sin rayas**. El autor lee en el celular y la raya larga (—) no se le muestra, así que el texto usa **comillas inglesas rectas** para el diálogo (`"así"`), **comas y puntos** en las acotaciones de habla, y **paréntesis, comas o dos puntos** para los incisos del narrador. Los `FICHAS.md` conservan rayas porque son documentos de trabajo. El revisor marca falta si aparece una raya o si una línea queda con comillas impares, y `python3 herramientas/convertir-rayas-a-comillas.py` sirve para reconvertir texto viejo.

## Biblia de referencia

Consulta la [biblia de referencia](biblia/README.md), organizada en 18 secciones: las 11 primeras documentan el universo de referencia; de la 12 a la 15 está el diseño del proyecto (protagonista, romance y rutas); y de la 16 a la 18, el método de trabajo, la bitácora de continuidad y los estándares de extensión de una novela ligera.

## Dedicatoria

Dedicada con mucho cariño a una persona muy especial de Guadalajara que, después de una larga lucha contra el cáncer, ahora está en un lugar mejor, acompañado de sus waifus favoritas y viviendo aventuras alocadas. ❤️

> Que cada nueva aventura sea tan divertida, caótica y extraordinaria como él la habría imaginado.

## Aviso

Esta es una obra de fan fiction creada por admiración y cariño. *KonoSuba!* y sus personajes originales pertenecen a sus respectivos creadores y titulares de derechos. Este proyecto no oficial no busca reemplazar ni representar una publicación oficial.
