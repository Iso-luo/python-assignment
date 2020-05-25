# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-18 9:10 p.m.
"""
Q1. Write an add method for Points that works with either a Point object or a tuple:
• If the second operand is a Point, the method should return a new
Point whose x coordinate is the sum of the x coordinates of the operands,
and likewise for the y coordinates.
• If the second operand is a tuple, the method should add
the first element of the tuple to the x coordinate
and the second element to the y coordinate,
and return a new Point with the result.
"""


class Point():
    def __add__(self, other):
        self.x = 1
        self.y = 1
        if isinstance(other, Point):
            self.x = other.x + self.x
            self.y = other.y + self.y
        elif isinstance(other, tuple):
            self.x = other[0] + self.x
            self.y = other[1] + self.y
        else:
            return self.x+self.y+other
        return self.x, self.y


p = Point()
p1 = Point()
p1.x = 9
p1.y = 9
t = (5, 5)
print(p+t)
print(p+p1)
print(p+4)
