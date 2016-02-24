#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scr.diff import diff


source = 'Оловянные Стойкие  солдатики(1965 г.).pdf'
pat = 'Стойкий оловянный солдатик_R96_ (1990 г.)'

noise = ['_R96_', '(?<=\d\d)г']


lst1 = diff.del_noise(source, diff.pattern(noise))
lst2 = diff.del_noise(pat, diff.pattern(noise))
print(lst1)
print(lst2)


