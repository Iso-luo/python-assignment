# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-09 12:53 p.m.

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(inventory.get("apples", 5))

import string

dic = {}
l = []
s = input('plz input a sentence:\n')
s = s.lower()
s1 = ""
for i in list(string.ascii_lowercase):
    dic[i] = s.count(i)
    if dic[i] == 0:
        del dic[i]
print(list(dic.items()))
dic_items = list(dic.items())

