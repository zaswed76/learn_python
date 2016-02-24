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
    res = pattern.sub(" ", source)
    return res.replace("ё", "е")


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
        [\W_]+|
        R96|
        чб|
        2ч|3ч|
        audio|
        часть|
        (?<=\d\d)г|
        \b\D{1,2}\b|
        \d_

                     """, re.VERBOSE | re.I)
    s = 'Сказка о том, кто ходил страху учиться (1989) [2ч]'
    s2 = 'Сказка о том, кто ходил страху учиться. Часть 2_R96_ (1989 г.)'

    a = wrapper(canonize, s, pat, cut_ext=0, norm=0)
    b = wrapper(canonize, s2, pat, cut_ext=0, norm=0)
    print(a())
    print(b())

    print(timeit.timeit(a, number=2000))
    print(timeit.timeit(b, number=2000))
    # print(timeit.timeit(normalize, number=2000))



