# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-02 3:06 p.m.


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(4, 0)
