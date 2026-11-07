#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte el diálogo con raya larga (—) al formato de comillas inglesas.

Nace del barrido del 17 de octubre de 2026 (regla 12 de `biblia/16`): el autor
pidió quitar todas las rayas porque su celular no las muestra.

Uso:
    python3 herramientas/convertir-rayas-a-comillas.py            # solo informa
    python3 herramientas/convertir-rayas-a-comillas.py --aplicar  # convierte
    python3 herramientas/convertir-rayas-a-comillas.py --aplicar novela/volumen-2/13-capitulo-13.md

Reglas de conversión:
  - Las partes pares del diálogo van entre comillas rectas: "así".
  - Si sigue una etiqueta de habla (empieza en minúscula y trae verbo de habla),
    el discurso cierra con `", ` y la etiqueta termina en punto.
  - Si la acotación no es de habla, el discurso cierra con `". ` y la acotación
    se capitaliza y va como oración aparte.
  - `...` se conserva; una continuación con `...` abre comilla sin mayúscula.
  - Las comillas angulares internas («») se respetan.

Conserva el BOM de cada archivo. No toca los documentos de trabajo (FICHAS.md).
Al terminar, avisa de las rayas que no sean de diálogo, que hay que pasar a
mano a paréntesis, comas o dos puntos.

Ojo: el conversor está pensado para texto que todavía trae rayas. Pasarle un
archivo ya convertido no lo rompe, pero tampoco hace nada.
"""

import glob, re, sys

VERBOS = ('dije','dijo','digo','dice','decía','decí','diciend','pregunt','respond',
          'contest','grit','añad','agreg','sigui','segu','repit','repet','empez','empec',
          'comenz','continu','interrump','murmur','susurr','exclam','escuch',
          'leyó','leí','insist','explic','admit','coment','pidi','orden',
          'recalc','corrig','termin','prosigui','balbuce','chill','aull','rugi',
          'pens','anunci','confes','aclar','suplic','brome','tarare','gruñ','sopl',
          'tartamud','farfull','declar')

def cap(s):
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + ch.upper() + s[i+1:]
        if ch not in '¿¡"«( ':
            return s
    return s

FRASES = ('buscó la palabra', 'bajó la voz', 'se alarmó', 'otra vez aqua')

def es_etiqueta(tag):
    """¿La acotación es un verbo de habla (dijo, preguntó, le dije...)."""
    t = tag.lower()
    return any(v in t for v in VERBOS) or any(f in t for f in FRASES)

def convertir(linea):
    if not linea.startswith('—'):
        return linea
    partes = linea[1:].split('—')
    n = len(partes)
    salida = []

    for i in range(n):
        seg = partes[i]
        if i % 2 == 0:
            if i > 0:
                seg = seg.lstrip()
                if seg[:3] == '...':
                    pass
                elif seg[:1] in '.,;:':
                    seg = cap(seg[1:].lstrip())
                else:
                    seg = cap(seg)
            seg = seg.rstrip()
            if i == n - 1:
                salida.append('"' + seg + '"')
            else:
                tag = partes[i + 1].strip()
                habla = es_etiqueta(tag) and tag[:1].islower()
                if seg.endswith('...'):
                    salida.append('"' + seg + '", ' if habla else '"' + seg + '" ')
                elif seg.endswith('.') and habla:
                    salida.append('"' + seg[:-1] + '", ')
                elif seg.endswith('.'):
                    salida.append('"' + seg + '" ')
                elif seg.endswith(('?', '!', ',', ';')):
                    salida.append('"' + seg + '" ')
                elif habla:
                    salida.append('"' + seg + '", ')
                else:
                    salida.append('"' + seg + '". ')
        else:
            tag = seg.strip()
            if not es_etiqueta(tag):
                tag = cap(tag)
            siguiente = partes[i + 1] if i + 1 < n else ''
            if tag.endswith(','):
                tag = tag[:-1] + '.'
            elif tag.endswith(':'):
                pass
            elif not tag.endswith(('.', '?', '!')):
                tag += ':' if siguiente.lstrip().startswith(':') else '.'
            salida.append(tag)
            if i < n - 1:
                salida.append(' ')
    return ''.join(salida).rstrip()

def archivos():
    """Todas las piezas de novela/, salvo los documentos de trabajo."""
    return [p for p in sorted(glob.glob('novela/volumen-*/*.md'))
            if not p.endswith('FICHAS.md')]

if __name__ == '__main__':
    make = '--aplicar' in sys.argv
    pedidos = [a for a in sys.argv[1:] if not a.startswith('--')]
    pendientes = []
    for p in (pedidos or archivos()):
        crudo = open(p, 'rb').read()
        bom = crudo.startswith(b'\xef\xbb\xbf')
        lineas = crudo.decode('utf-8-sig').split('\n')
        nuevos = [convertir(l) for l in lineas]
        if make:
            datos = (b'\xef\xbb\xbf' if bom else b'') + '\n'.join(nuevos).encode('utf-8')
            open(p, 'wb').write(datos)
            print('convertido', p, '(' + ('con BOM' if bom else 'sin BOM') + ')')
        else:
            for k, (a, b) in enumerate(zip(lineas, nuevos), 1):
                if a != b and len(a[1:].split('—')) >= 5:
                    print(f'--- {p}:{k}')
                    print('  A:', a[:190])
                    print('  D:', b[:190])
        for k, l in enumerate(nuevos, 1):
            if '\u2014' in l:
                pendientes.append((p, k, l.strip()[:90]))
    if pendientes:
        print()
        print('Rayas que el conversor no toca (van a mano, regla 12):')
        for p, k, l in pendientes:
            print('  {}:{}  {}'.format(p, k, l))
    else:
        print()
        print('Sin rayas pendientes.')
