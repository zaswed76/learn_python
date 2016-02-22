#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

config = dict(
    default_noise = '[\W]+'
)

def pattern(noise):
    noise.append(config['default_noise'])
    return "|".join(noise)

def canonize(source, pattern, limit=2):
    pat = re.compile(r'{}'.format(pattern), re.UNICODE)
    lst = pat.sub(" ", os.path.splitext(source)[0]).split()
    return [l for l in lst if len(l) > limit]

