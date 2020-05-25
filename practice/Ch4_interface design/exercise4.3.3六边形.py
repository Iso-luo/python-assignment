# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
3. Make a copy of square and change the name to polygon多边形.
Add another parameter named n and modify the body so it draws an n-sided regular polygon.
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
"""
import math
import turtle


def polygon(t, length, n):      #
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()


def do_turtle(f, t, length, n):
    f(t, length, n)


bob = turtle.Turtle()   # 先创建对象


do_turtle(polygon, bob, 100, 6)



