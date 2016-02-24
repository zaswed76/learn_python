#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import os
import re

import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def not_noise(source, pattern, cut_ext=False):
    """
    удаляет "шум" исходя из арг. pattern
    :param source: str
    :param pattern: re.compile
    :param cut_ext: bool
    :return: str
    """
    if cut_ext:
        source = os.path.splitext(source)[0]
    return pattern.sub(" ", source)


def canonize(source, pattern, cut_ext=False, sorted=True, norm=False):
    """
    удаляет шум и возврашает отсортированный список (по умолчанию)
    :param source:
    :param pattern:
    :param cut_ext:
    :param sorted:
    :return:
    """
    lst = not_noise(source, pattern, cut_ext).split()
    if norm: lst = normalize(*lst)
    else: lst = [x.lower() for x in lst]
    if sorted: lst.sort()
    return lst

def normalize(*c):
    lst = []
    for i in c:
        lst.append(morph.normal_forms(i)[0])
    return lst


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit

    pat = re.compile(r"""
        [\W]+|
        _R96_|
        (?<=\d\d)г|
        \b\D{1,2}\b
                     """, re.VERBOSE)
    s = 'Сказка про Ивашку-глиняшку_R96_ (1982 г.)'
    s2 = 'Сказка про Ивашку - Глиняшку (1982).jpg'

    a = wrapper(canonize, s, pat, cut_ext=1, norm=0)
    b = wrapper(canonize, s2, pat, cut_ext=1, norm=0)
    print(a())
    print(b())

    print(timeit.timeit(a, number=2000))
    print(timeit.timeit(b, number=2000))
    # print(timeit.timeit(normalize, number=2000))



