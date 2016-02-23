#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os
import re
from difflib import SequenceMatcher

config = dict(
    default_noise = '[\W]+'
)

def pattern(noise):
    noise.append(config['default_noise'])
    return "|".join(noise)

def canonize(source, pattern, limit=2):
    pat = re.compile(r'{}'.format(pattern), re.UNICODE)
    lst = pat.sub(" ", os.path.splitext(source)[0]).split()
    return [l for l in lst if len(l) > limit]

def genshingle(source):
    import binascii
    shingleLen = 1 #длина шингла
    out = []
    for i in range(len(source)-(shingleLen-1)):
        out.append (binascii.crc32(' '.join( [x for x in source[i:i+shingleLen]] ).encode('utf-8')))

    return out

def compaire (source1,source2):
    print(source1, source2, "!!")
    same = 0
    for i in range(len(source1)):
        if source1[i] in source2:
            same = same + 1

    return same*2/float(len(source1) + len(source2))*100

def main():
    text1 = u'Самоделкина на космос (1979)' # Текст 1 для сравнения
    text2 = u'Самоделкин в космосе_R96_(1979 г.)' # Текст 2 для сравнения
    noise = ['_R96_', '\bг\b']
    cmp1 = genshingle(canonize(text1, pattern(noise)))
    cmp2 = genshingle(canonize(text2, pattern(noise)))


    print(compaire(cmp1,cmp2))

# Start program
main()
