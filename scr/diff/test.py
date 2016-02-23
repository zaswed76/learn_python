#!/usr/bin/env python
# -*- coding: utf-8 -*-


from difflib import SequenceMatcher
s = SequenceMatcher(lambda x: x == " ",
                    "эдгар 1",
                    "эдгар")

print(s.ratio())

