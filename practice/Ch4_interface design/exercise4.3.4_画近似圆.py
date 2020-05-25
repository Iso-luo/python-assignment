# -*- coding:utf-8 -*-
# !/usr/bin/env python


"""
Write a function called circle that takes a turtle, t, and radius, r, as parameters
and that draws an approximate circle by calling polygon with an appropriate
length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that
length * n = circumference.
"""

import math
import turtle


def polyline(t, n, length, angle):  # 画折线
    for i in range(n):
        t.forward(length)
        t.lt(angle)  # angle是每个角的度数
    turtle.mainloop()


def polygon(r):  # r为半径
    circumference = 2 * math.pi * r  # 圆形周长
    n = int(circumference / 20) + 3  # 方形边数n  (假设将周长划分为20份) n>=3
    length = circumference / n  # 方形每边长度length
    angle = 360.0 / n  # 方形顶角
    t = turtle.Turtle()  # 创建turtle对象t
    polyline(t, n, length, angle)
    print('n=', n)


def circle(t, r):  # 传参数
    polygon(r)


bob = turtle.Turtle()
circle(bob, 5)  # 执行
