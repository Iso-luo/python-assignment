# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-02 2:35 p.m.
"""
1. Write a function named is_triangle that takes three integers as arguments,
and that prints either “Yes” or “No”, depending on whether you can or cannot
form a triangle from sticks with the given lengths.
"""


def is_triangle(side1, side2, side3):
    if side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1:
        print("Yes")
    else:
        print("No")


"""
2. Write a function that prompts the user to input three stick lengths,
converts them to integers, and uses is_triangle to check 
whether sticks with the given lengths can form a triangle.
"""

def judge():
    a = float(input("plz enter side1:"))
    b = float(input("plz enter side2:"))
    c = float(input("plz enter side3:"))
    is_triangle(a, b, c)


judge()