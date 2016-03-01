#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

s = "base:hover"

p = re.compile(r'(base([:]hover)*?$)')
print(p.search(s))
