# -*- coding:utf-8 -*-
# !/usr/bin/env python

import turtle
import math

t = turtle.Turtle()


def polygon(a, n, length):  # Turtle的对象a，边长length，边数n
    angle = 360.0 / n  # Because the numerator is a floating-point number 浮点数, the result is a floating-point
    for i in range(n):
        a.fd(length)
        a.lt(angle)
    turtle.mainloop()


def circle(a, r):  # 半径r
    circumference = 2 * math.pi * r  # 圆的周长
    n = 50  # 周长分成n份
    length = circumference / n  # 每份的长度
    polygon(a, n, length)


