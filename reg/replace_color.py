#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

s = '''button {
    background: grey;
    border-color gray;
}'''

pat = re.compile('''
(button\s+\{)
(.*)
(border-color\s+)
(\w+)
(\W*)

''', re.VERBOSE | re.DOTALL | re.IGNORECASE)

print(pat.findall(s))