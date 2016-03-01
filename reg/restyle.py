#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


def regular_expression(selector, property, replacement):
    pat = re.compile('''
        ({selector}
        .+?
        (?<={property}\:))
        .+?
        (\w+)
         '''.format(selector),
    re.VERBOSE | re.DOTALL | re.IGNORECASE)
    return pat, replacement

def restyle(source, regular_expression, replacement):
    return regular_expression.sub(r'\1 replacement', source)

def file_name():
    try:
        name = sys.argv[1]
    except IndexError:
        print("первым аргументом должно быть имя файла")
        sys.exit()
    else: return name

class ReStyle:
    def __init__(self, file):
        self.file = file
        self._style = None

    @property
    def style(self):
        with open(self.file, "r") as f:
            return f.read()

    @style.setter
    def style(self, new_style):
        with open(self.file, "w") as f:
            f.write(new_style)



def main():




if __name__ == '__main__':
    rs = ReStyle('test_style')
    print(rs.style)
    rs.style = "new"