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

- [`novela/volumen-1/`](novela/volumen-1/) — Volumen 1: prólogo, capítulos 1 a 10 y epílogo. **Terminado y aprobado por el autor** (12 de 12 piezas).
  - [`00-prologo.md`](novela/volumen-1/00-prologo.md) — «Un lugar sin ventanas».
  - [`FICHAS.md`](novela/volumen-1/FICHAS.md) — fichas de diseño de cada pieza del volumen.
- [`novela/volumen-2/`](novela/volumen-2/) — Volumen 2: capítulos 11 a 20. Carpeta abierta el 13 de octubre de 2026; se escribe capítulo a capítulo.
  - [`00-resumen-volumen-1.md`](novela/volumen-2/00-resumen-volumen-1.md) — resumen del Volumen 1: historia, reparto, tiempo, banderas y lo que quedó abierto.
  - [`11-capitulo-11.md`](novela/volumen-2/11-capitulo-11.md) — «La verdad en voz alta». **Aprobado por el autor** (17 de octubre de 2026).
  - [`12-capitulo-12.md`](novela/volumen-2/12-capitulo-12.md) — «La cuenta». **Aprobado por el autor** (17 de octubre de 2026).
  - [`FICHAS.md`](novela/volumen-2/FICHAS.md) — fichas de diseño del volumen, con el capítulo 11 ya cerrado.

Los archivos de la novela llevan **UTF-8 con BOM (UTF-8-BOM)**, el formato que usaba la aplicación de lectura en voz alta (**ElevenReader**). **El requisito quedó revocado por el autor el 17 de octubre de 2026:** las piezas nuevas se escriben **sin BOM** y las viejas conservan el que ya tienen. `python3 herramientas/utf8-bom.py` sirve para convertir si alguna vez hace falta, y `python3 herramientas/revisar-capitulos.py` revisa formato, extensión y reglas de lectura en voz alta (sin exigir el BOM).

## Biblia de referencia

Consulta la [biblia de referencia](biblia/README.md), organizada en 18 secciones: las 11 primeras documentan el universo de referencia; de la 12 a la 15 está el diseño del proyecto (protagonista, romance y rutas); y de la 16 a la 18, el método de trabajo, la bitácora de continuidad y los estándares de extensión de una novela ligera.

## Dedicatoria

Dedicada con mucho cariño a una persona muy especial de Guadalajara que, después de una larga lucha contra el cáncer, ahora está en un lugar mejor, acompañado de sus waifus favoritas y viviendo aventuras alocadas. ❤️

> Que cada nueva aventura sea tan divertida, caótica y extraordinaria como él la habría imaginado.

## Aviso

Esta es una obra de fan fiction creada por admiración y cariño. *KonoSuba!* y sus personajes originales pertenecen a sus respectivos creadores y titulares de derechos. Este proyecto no oficial no busca reemplazar ni representar una publicación oficial.
