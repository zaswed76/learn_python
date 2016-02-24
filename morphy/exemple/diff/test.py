#!/usr/bin/env python
# -*- coding: utf-8 -*-


from difflib import SequenceMatcher
s = SequenceMatcher(lambda x: x == " ",
                    "колобок",
                    "колобок")

print(s.ratio())

