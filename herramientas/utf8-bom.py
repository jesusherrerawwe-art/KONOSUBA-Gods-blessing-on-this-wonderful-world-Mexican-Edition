#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte archivos de texto a UTF-8 con BOM (UTF-8-BOM).

La aplicación de lectura en voz alta que usa el autor (ElevenReader) pide los
documentos en UTF-8-BOM. Este script los deja así, sin tocar una sola letra
del contenido.

Uso:
    python3 herramientas/utf8-bom.py                # todos los .md de novela/
    python3 herramientas/utf8-bom.py archivo.md ...  # solo los archivos indicados

Es idempotente: si un archivo ya tiene BOM, no se le pone doble.
"""

import io
import os
import sys

BOM = b"\xef\xbb\xbf"


def convertir(ruta):
    """Devuelve 'convertido', 'ya tenía BOM' o 'error'."""
    try:
        crudo = open(ruta, "rb").read()
    except OSError as e:
        print("  ERROR  {} ({})".format(ruta, e))
        return "error"

    # Se lee como UTF-8 descartando un BOM previo (si lo hay) y se vuelve a
    # escribir con BOM. Así el archivo nunca queda con dos BOM.
    try:
        texto = crudo.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        print("  ERROR  {} (no es UTF-8 válido: {})".format(ruta, e))
        return "error"

    if crudo.startswith(BOM):
        print("  ya estaba  {}".format(ruta))
        return "ya"

    with io.open(ruta, "w", encoding="utf-8-sig", newline="") as f:
        f.write(texto)
    print("  convertido  {}".format(ruta))
    return "convertido"


def archivos_de_novela():
    """Todos los .md de novela/, en orden."""
    base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "novela")
    encontrados = []
    for carpeta, _, archivos in os.walk(base):
        for a in sorted(archivos):
            if a.lower().endswith(".md"):
                encontrados.append(os.path.join(carpeta, a))
    return encontrados


def main():
    rutas = sys.argv[1:] or archivos_de_novela()
    if not rutas:
        print("No hay archivos que convertir.")
        return 1
    print("Convirtiendo a UTF-8-BOM:")
    cuenta = {"convertido": 0, "ya": 0, "error": 0}
    for r in rutas:
        cuenta[convertir(r)] += 1
    print("Listo: {} convertidos, {} ya estaban, {} errores.".format(
        cuenta["convertido"], cuenta["ya"], cuenta["error"]))
    return 1 if cuenta["error"] else 0


if __name__ == "__main__":
    sys.exit(main())
