#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from diatools.lib import files_tool

from morphy.lib import diff

pat_noise = re.compile(r"""
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

pat_dubl = re.compile(r'(\w+)\1{1,}')

def source_lst():
    obj = files_tool.Pickle(
        '/home/vostro/Документы/Диафильмы/Диафильмы/миниатюры/.data.pkl')
    return obj.load().keys()


def pat_lst():
    fl = "/home/vostro/project/learn_python/morphy/test/содержание.txt"
    with open(fl, "r") as f:
        return [x.strip() for x in f]


def canonize_lst(lst, norm):
    res = set()
    for l in lst:

        s = pat_noise.sub(" ", l)
        s = pat_dubl.sub(r"\1", s)

        res.add(tuple(diff.canonize(s, norm=norm)))
    return res


pat_set = canonize_lst(pat_lst(), 1)
print(len(pat_set))
source_set = canonize_lst(source_lst(), 1)
res = pat_set - source_set
print(res, len(res), sep="\n-----------------------\n")
