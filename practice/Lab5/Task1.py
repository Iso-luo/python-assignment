# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-15 3:39 p.m.


"""
Task 1. Create a new class called Point. This class will have a “x” and “y” attribute.
write a function called distance_between_points that takes two Points as arguments
and returns the distance between them.
Test you function by instantiating two instances and assigning them x and y attributes.
"""


class Point:
    x = 0
    y = 0


def distance_between_points(a, b):  # function
    return abs(a - b)


print(dir(Point))
p1 = Point()
p2 = Point()
p1.x = 1
p2.y = 5
print(distance_between_points(p1.x, p2.y))
