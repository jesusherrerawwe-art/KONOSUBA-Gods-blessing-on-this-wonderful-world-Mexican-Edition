#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisa los capítulos de la novela: formato, extensión y reglas de texto a voz.

Uso:
    python3 herramientas/revisar-capitulos.py            # todos los .md de novela/
    python3 herramientas/revisar-capitulos.py novela/volumen-1/07-capitulo-7.md

Las piezas narrativas (prólogo y capítulos) se revisan completas; los documentos
de trabajo, como FICHAS.md, solo se revisan de formato y extensión. Se reconoce
como pieza narrativa la que lleva el bloque de encabezado con la línea «Estado:».

Revisa, por archivo:
  1. El formato del texto. Desde el 17 de octubre de 2026 el autor revocó el
     requisito de UTF-8-BOM: los archivos nuevos van sin BOM y los viejos lo
     conservan. Solo se marca falta si un archivo trae dos BOM pegados.
  2. La extensión en palabras del cuerpo (sin contar el encabezado) contra el
     número que anuncia el propio encabezado.
  3. Las reglas del diálogo (regla 12 de biblia/16): ninguna raya larga (—) en
     el texto, el diálogo entre comillas inglesas rectas y las comillas
     balanceadas (número par en cada línea).
  4. Las reglas de texto a voz de biblia/16: sin marcas de formato en el cuerpo,
     puntos suspensivos de tres puntos, sin abreviaturas, sin emojis, sin
     frases largas en mayúsculas, sin dobles espacios ni espacios antes de
     signo de puntuación.

No es infalible: las líneas marcadas como AVISO conviene leerlas antes de
tocar el texto.
"""

import glob
import io
import os
import re
import sys

BOM = b"\xef\xbb\xbf"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D]")
MAYUS_LARGA = re.compile(r"\b[A-ZÁÉÍÓÚÜÑ]{5,}\b")
ABREV = re.compile(r"\b(Sr|Sra|Srita|Dr|Dra|pág|págs|núm|etc|aprox|Cap)\.", re.I)
MARCA = re.compile(r"\*\*|\*|__|`|^\s*#{1,6}\s*$")
ESPACIO_DOBLE = re.compile(r"[^\s]  +[^\s]")
ESPACIO_SIGNO = re.compile(r"\s+[,.;:!?]")
FALTA_ESPACIO = re.compile(r"[a-záéíóúüñ][A-ZÁÉÍÓÚÜÑ]")
SUSP_U = "\u2026"


def espacio_antes_de_punto(linea):
    """Avisos de espacio antes de signo de puntuación."""
    return list(ESPACIO_SIGNO.finditer(linea))


def revisar(ruta):
    crudo = open(ruta, "rb").read()
    texto = crudo.decode("utf-8-sig")
    lineas = texto.split("\n")
    cuerpo = "\n".join(lineas[5:])  # el encabezado son las cinco primeras líneas

    encabezado = "\n".join(lineas[:5])
    es_pieza = "Estado:" in encabezado  # las fichas y demás documentos de trabajo no llevan encabezado

    hallazgos = []

    if crudo.startswith(BOM + BOM):
        hallazgos.append(("FALTA", "el archivo tiene dos BOM"))

    # Regla 12: ninguna raya; el diálogo va entre comillas inglesas.
    if es_pieza:
        for n, linea in enumerate(lineas, 1):
            if "\u2014" in linea:
                hallazgos.append(("FALTA", f"línea {n}: raya prohibida en el texto ({linea.strip()[:50]})"))
            if linea.count('"') % 2:
                hallazgos.append(("FALTA", f"línea {n}: comillas impares ({linea.strip()[:50]})"))
            if '""' in linea:
                hallazgos.append(("AVISO", f"línea {n}: dos comillas pegadas"))

    palabras = len(re.findall("[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+", cuerpo))
    anunciado = re.search(r"Extensi[oó]n:\s*([\d,]+)", "\n".join(lineas[:5]))
    if anunciado:
        n = int(anunciado.group(1).replace(",", ""))
        if n != palabras:
            hallazgos.append(("AVISO", "el encabezado dice {} palabras y el cuerpo tiene {}".format(n, palabras)))

    if not es_pieza:
        if "…" in cuerpo:
            hallazgos.append(("AVISO", "documento de trabajo: usa puntos suspensivos de un solo carácter (…)"))
        return palabras, hallazgos

    if SUSP_U in cuerpo:
        hallazgos.append(("FALTA", "hay puntos suspensivos de un solo carácter (…) en {} lugar(es)".format(cuerpo.count(SUSP_U))))
    for i, l in enumerate(lineas[5:], start=6):
        if MARCA.search(l):
            hallazgos.append(("FALTA", "línea {}: marca de formato ({})".format(i, l.strip()[:60])))
        if MAYUS_LARGA.search(l):
            hallazgos.append(("AVISO", "línea {}: mayúsculas sostenidas «{}»".format(i, MAYUS_LARGA.search(l).group(0))))
        if ABREV.search(l):
            hallazgos.append(("AVISO", "línea {}: abreviatura «{}»".format(i, ABREV.search(l).group(0))))
        if EMOJI.search(l):
            hallazgos.append(("AVISO", "línea {}: emoji fuera del encabezado".format(i)))
        if ESPACIO_DOBLE.search(l):
            hallazgos.append(("AVISO", "línea {}: doble espacio".format(i)))
        for m in espacio_antes_de_punto(l):
            hallazgos.append(("AVISO", "línea {}: espacio antes de signo («{}»)".format(i, l[max(0, m.start() - 12):m.end() + 6].strip())))
        if FALTA_ESPACIO.search(l):
            hallazgos.append(("AVISO", "línea {}: falta un espacio después del punto («{}»)".format(i, FALTA_ESPACIO.search(l).group(0))))
    if "\t" in cuerpo:
        hallazgos.append(("FALTA", "hay tabuladores en el cuerpo"))

    return palabras, hallazgos


def main():
    rutas = sys.argv[1:]
    if not rutas:
        rutas = []
        for carpeta, _, archivos in os.walk(os.path.join(RAIZ, "novela")):
            for a in sorted(archivos):
                if a.lower().endswith(".md"):
                    rutas.append(os.path.join(carpeta, a))
    total, problemas = 0, 0
    for r in rutas:
        nombre = os.path.relpath(r, RAIZ)
        palabras, hallazgos = revisar(r)
        total += palabras
        cuenta = {"FALTA": 0, "AVISO": 0}
        for tipo, _ in hallazgos:
            cuenta[tipo] += 1
        problemas += cuenta["FALTA"]
        print("{:<40} {:>6} palabras | faltas:{} avisos:{}".format(nombre, palabras, cuenta["FALTA"], cuenta["AVISO"]))
        for tipo, desc in hallazgos:
            print("   {} {}".format(tipo, desc))
    print("Total: {} palabras en {} archivo(s). Faltas que corregir: {}.".format(total, len(rutas), problemas))
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
