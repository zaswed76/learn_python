#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scr.diff import diff

sss = "Азбука нравственности (1989)"
xxx = "Азбука"

noise = ['_R96_', '(?<=\d\d)г']


lst1 = sorted(diff.canonize(sss, diff.pattern(noise)))
lst2 = sorted(diff.canonize(xxx, diff.pattern(noise)))
print(lst1)
print(lst2)


