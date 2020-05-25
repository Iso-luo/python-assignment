# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-03 11:43 p.m.

import turtle
import math


def draw_square(t, side_size):
    for i in range(4):
        t.fd(side_size)
        t.lt(90)


def move(t, angle, move_size):
    t.pu()
    t.lt(angle)  # 笔尖移动角度
    t.fd(move_size)
    t.pd()
    t.rt(angle)


def execute(t, side_size, angle, move_size):
    for i in range(2):
        draw_square(t, side_size)
        move(t, angle, move_size)
        side_size = side_size * 2


def polyline(t, n, length, angle):
    # angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# 画圆弧的方法
def arc(t, r, radian):
    arc_circumference = 2 * math.pi * r
    n = int(arc_circumference / 3) + 3
    length = arc_circumference / n
    angle = radian / n
    polyline(t, n, length, angle)


wn = turtle.Screen()
wn.bgcolor("pink")
bob = turtle.Turtle()
# draw_square(bob, 50)
execute(bob, 20, 45, 100)
turtle.mainloop()
