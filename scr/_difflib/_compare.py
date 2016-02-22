#!/usr/bin/env python
# -*- coding: utf-8 -*-




import os
import re

dir1 = "/home/vostro/temp/Диафильмы_DJVU"
dir2 = "/home/vostro/project/diafilmtools/examples/содержание.txt"


def lst_1():
    first_lst = os.listdir(dir1)
    return sorted(first_lst)


def lst_2():
    with open(dir2, "r") as f:
        return [x.strip() for x in f]




orig = "Садко (1963) [+audio].djvu"
orig2 = "Самокат с мотором (1970).djvu"
orig3 = "Самоделкин в космосе (1979).djvu"

p = "Садко_R96_ (1990 г.)"
p2 = "Саламанский виноград. Принц-краб_R96_(1980 г.)"
p3 = "Самоделкин в космосе_R96_(1979 г.)"




s = "Самоделкин в космосе_R96_(1979 г.)"
s2 = "Самоделкин в космосе (1979).djvu"

noise = ['_R96_', '\bг\b']




