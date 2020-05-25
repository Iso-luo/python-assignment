# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-06 8:41 a.m.


import math


#
# def theta(m1, m2, r):
#     a = -3 * math.pi * (r ** 3)
#     b = math.sqrt((m1 * m2) / (2 * (r ** 2)))
#     c = math.log10((3 * m1) / (4 * m2))
#     d = math.exp(math.tan(r))
#     print(a * b * c * d)


def theta(m1, m2, r):
    a = -3 * math.pi * (r ** 3)
    b = math.sqrt((m1 * m2) / (2 * (r ** 2)))
    c = math.log10((3 * m1) / (4 * m2))
    d = math.exp(math.tan(r))
    print(a * b * c * d)


theta(10, 20, 5)

theta(10, 20, 5)
theta(1, 2, 3)
