# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-15 4:06 p.m.
"""
Task 3.Write a constructor( __init__ method) for the Point class that
takes x and y as optional parameters and assigns them to the corresponding attributes.
A. Write a __str__ method for the Point class. Test by creating a Point object and
use the print function to print an instance of the class.
B. Write an __add__ method for the Point class.
"""


class Point:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        a = self.x+self.y
        b = other.x+other.y
        return a+b


p1 = Point(1,2)
p2 = Point(3,4)
print(p1+p2)
print(p1.__add__(p2))

