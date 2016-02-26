#!/usr/bin/env python
# -*- coding: utf-8 -*-


import timeit



import re
# data = 'aaa'
# pat = re.compile('(.+)\1')
#
#
#
# def search():
#     return pat.findall(data)
# print(search())
# print(timeit.timeit(search, number=112500))


p = re.compile(r'(\w+)\1{1,}')
print(p.sub(r'\1', 'долллар пукпыуп ыукпукп'))

