# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-07 11:02 p.m.

file = open("/Users/a123/Desktop/words_copy.txt", "r")
line = file.readline()
while line:
    values = line.strip()
    print(values)