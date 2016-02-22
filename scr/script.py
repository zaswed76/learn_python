#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scr.diff import diff

s = "Самоделкин в космосе_R96_(1979 г.)"
s2 = "Самоделкин в космосе (1979).djvu"

noise = ['_R96_', '\bг\b']


lst1 = diff.canonize(s, diff.pattern(noise))
lst2 = diff.canonize(s2, diff.pattern(noise))

print(lst1)
print(lst2)
