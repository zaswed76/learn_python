#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = '''

[base]
border: green
color: green;
bg: green

[second]
border: green
color: green;
bg: green

[base:hover]
border: green
color: green;
bg: green
[second]
border: green
color: green;
bg: green
'''

p = re.compile('''
(\[base
.+?
(?<=color\:))
(\s+)
(\w+)

''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
print(p.sub(r'\1 red', s))