# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-04 3:22 p.m.

"""
Write a function that checks if a number is even or not.
"""


def judge():
    n = int(input("plz enter a number:\n"))
    if n % 2 == 0:
        print("It's an even")
    else:
        print("It's not an even")


judge()