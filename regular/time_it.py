#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
setup = """
import re
pat = re.compile('s')
s = 'asd'
"""
print("asd".replace("s", "!"))
print(timeit.timeit('"asd".replace("s", "!")', number=1000000))
print(timeit.timeit('pat.sub("!",s)', setup=setup, number=1000000))