# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-09 12:42 a.m.
a=(1,2,3,4,5)
b=[1,2,3,4,5]
c="zhangkang"

la=map(str,a)
lb=map(str,b)
lc=map(str,c)

print(la)
print(lb)
print(lc)

print map(lambda x: x % 2, range(7))
[0, 1, 0, 1, 0, 1, 0]