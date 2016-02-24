#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from diatools.lib import files_tool

from morphy.lib import diff

pat = re.compile(r"""
        [\W]+|
        _R96_|
        (?<=\d\d)г|
        \b\D{1,2}\b
                     """, re.VERBOSE)


def source_lst():
    obj = files_tool.Pickle(
        '/home/sergk/Диафильмы/миниатюры/.data.pkl')
    return obj.load().keys()


def pat_lst():
    with open("pat.txt", "r") as f:
        return [x.strip() for x in f]


def canonize_lst(lst, pat, norm):
    res = set()
    for n in lst:
        res.add(tuple(diff.canonize(n, pat, cut_ext=True, norm=norm)))
    return res


pat_set = canonize_lst(pat_lst(), pat, 1)
source_set = canonize_lst(source_lst(), pat, 1)
print(pat_set - source_set)
