#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = '55-55-55'

p = re.compile('(\d+)(\W)(.+)')
print(p.sub(r'\1:\3', s))