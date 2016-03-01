#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

def style():
    with open("style.css", "r") as f:
        return f.read()

def write_style(new_style):
    with open("style.css", "w") as f:
        f.write(new_style)

# s = '''
# button {
#     background: grey;
#     border-color: gray;
# }
# label {
#     background: grey;
# }
#
# label:hover {
#     background: grey;
# }
#
# button:hover {
#
#     border: 1px solid gray;
#     background: grey;
# }'''

s = style()

pat = re.compile('''
(button
.+?
(?<=border-color\:))
.+?

(\w+)
''', re.VERBOSE | re.DOTALL | re.IGNORECASE)

snew = pat.sub(r'\1 red', s)

write_style(snew)