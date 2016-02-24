#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from diatools.lib import files_tool

from morphy.lib import diff

pat = re.compile(r"""
        Рус-Eng|
        первая|
        вторая|
        цветной|
        кадров|
        [\W_]+|
        R96|
        чб|
        2ч|3ч|
        audio|
        часть|
        text|
        (?<=\d\d)г|
        \b\D{1,2}\b|
        \d

                     """, re.VERBOSE | re.I)


def source_lst():
    obj = files_tool.Pickle(
        '/home/sergk/Диафильмы/миниатюры/.data.pkl')
    return obj.load().keys()


def pat_lst():
    fl = "/home/sergk/project/learn_python/morphy/test/содержание2.txt"
    with open(fl, "r") as f:
        return [x.strip() for x in f]


def canonize_lst(lst, pat, norm):
    res = set()
    for n in lst:
        res.add(tuple(diff.canonize(n, pat, cut_ext=0, norm=norm)))
    return res


pat_set = canonize_lst(pat_lst(), pat, 1)
print(len(pat_set))
source_set = canonize_lst(source_lst(), pat, 1)
res = pat_set - source_set
print(res, len(res), sep="\n-----------------------\n")
