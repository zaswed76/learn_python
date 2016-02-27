#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def get_config(path):
    with open(path, "r") as f:
        return f.read()

def set_config(path, config):
    with open(path, "w") as f:
        f.writelines(config)

config = get_config("config.txt")

p_search = re.compile('[^#]')
p_sub = re.compile('=')

print(config)