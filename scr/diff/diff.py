#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from difflib import SequenceMatcher

config = dict(
    default_noise = '[\W]+'
)

def pattern(noise):
    noise.append(config['default_noise'])
    return "|".join(noise)

def canonize(source, pattern, limit=2):
    pat = re.compile(r'{}'.format(pattern), re.UNICODE)
    lst = pat.sub(" ", os.path.splitext(source)[0]).split()
    return [l for l in lst if len(l) > limit or l.isdigit()]

def diff_ratio(lst1, lst2):
    res = []
    for l1, l2 in zip(lst1, lst2):
        print(l1, l2)
        res.append(SequenceMatcher(None, l1, l2).real_quick_ratio())
    return sum(res)/len(res)

def quick_diff(source, pat):
    ratio = []
    not_comp = []
    for i in pat:
        if i in source:
            ratio.append(i)
        else:
            not_comp.append(i)
    return ratio, not_comp, source

def diff_main():
    y, n, source = quick_diff(s, p)
    print(y, n)
    if not n:
        return True
    else:
        return diff_1(n, source)



def diff_1(n, source):
    lst = []
    for l in n:
        if l.isdigit():
            return False

        for s in source:
            print(l, s)
            r = SequenceMatcher(None, l, s)
            ratio = r.quick_ratio()
            if ratio > 0.85:
                lst.append(ratio)
                break
        return lst





if __name__ == '__main__':
    s = ['Самоделкин', 'космосo', '1980']
    p = ['космосе', 'Самоделкiн', '1980']

    print(diff_main())