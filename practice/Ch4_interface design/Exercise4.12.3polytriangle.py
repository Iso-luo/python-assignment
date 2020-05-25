# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-01 4:39 p.m.


import turtle
import math


def triangle(t, n, radius):
    turn_angle = 90.0 + 180.0 / n
    side_length = 2 * radius * math.sin(math.pi / n)  # 对于sinθ 来说，360度等于2Pi!!!
    for i in range(n):
        t.pd()
        t.fd(radius)
        t.lt(turn_angle)
        t.fd(side_length)
        t.lt(turn_angle)
        t.pu()
        t.fd(radius)
        t.lt(180)


bob = turtle.Turtle()
triangle(bob, 20, 100.0)
turtle.mainloop()
