# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
Make a more general version of circle called arc that
takes an additional parameter angle,
which determines what fraction of a circle to draw.
angle is in units of degrees, so when angle=360,
arc should draw a complete circle.
"""

import math
import turtle


def polyline(t, n, length, angle):  # 画折线
    for i in range(n):  # range(int类型)
        t.fd(length)
        t.lt(angle)  # angle每个角


def arc(t, r, angle):  # angle 圆弧的角
    arc_length = 2 * math.pi * r * abs(angle) / 360  # abs()一定要加，否则负的角度失效
    n = int(arc_length / 4) + 3  # int()一定要加，n必须是int才可以迭代
    step_length = arc_length / n
    step_angle = float(angle) / n  # float()一定要加，否则即使angle=360，圆也画不全
    t = turtle.Turtle()
    polyline(t, n, step_length, step_angle)
    print(n)
    # turtle.mainloop()


bob = turtle.Turtle()
arc(bob, 100, 360)  # 从图像结果可以看出，圆心角的度数和分成的多边形的边数不是一一对应
