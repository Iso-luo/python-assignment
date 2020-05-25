# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-04 3:27 p.m.

"""
1. Write a function named is_triangle that
takes three integers as arguments,
and that prints either “Yes” or “No,”
depending on whether you can or cannot form
a triangle from sticks with the given lengths.
2. Write a function that prompts the user to
input three stick lengths,
converts them to integers,
and uses is_triangle to check whether
sticks with the given lengths can form a triangle.
"""


def is_triangle(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a:
        print("Yes. It can form a triangle")
    else:
        print("No,it can't.")


def with_prompt():
    a = int(input("plz enter the first length:\n"))
    b = int(input("plz enter the second length:\n"))
    c = int(input("plz enter the third length:\n"))
    is_triangle(a, b, c)


with_prompt()

