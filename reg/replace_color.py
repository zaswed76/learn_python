#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

def style():
    with open("style.css", "r") as f:
        return f.read()

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
(.*)
(button)
(.*)
(border-color\W\s+)
(\w+)
(.*)

''', re.VERBOSE | re.DOTALL | re.IGNORECASE)

print(pat.sub(r'\1\2\3\4red\6', s))
# print(pat.findall(s))