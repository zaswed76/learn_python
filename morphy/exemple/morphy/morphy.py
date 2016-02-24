#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

print(morph.normal_forms("сказочник"))
print(morph.normal_forms("сказочница"))
print(morph.normal_forms("сказочный"))