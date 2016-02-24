#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = [('aa', 'bb'), ('xx', 'zz'), ('cc', 'rr')]
t2 = [('aa', 'bs')]

a = set(t2) - set(t)
print(a)
p = ['aa']