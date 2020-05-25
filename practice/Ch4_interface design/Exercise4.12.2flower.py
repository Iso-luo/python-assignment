# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-01 12:21 a.m.

# from fundamental import arc

import turtle
import math
# 画折线的方法
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


# 多边形
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)  # 用了画折线的方法


# 圆
def circle(t, r):  # 给了圆的半径和角度
    arc(t, r, 360)  # 用了画圆弧的方法


def petal(t, r, angle):
    """
    Draws a petal using two ars
    :param t:Turtle
    :param r: radius
    :angle: degrees
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """
    draw a flower with n petals
    :param t: Turtle
    :param n: number of petals
    :param r: radius of arc
    :param angle: degrees that subtends the arc 弧线的对角度
    :return: None
    """
    petal_angle = 360.0/n
    for i in range(n):
        petal(t, r, angle)
        t.lt(petal_angle)


def pen_move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()
pen_move(bob, 50)
flower(bob, 50,10,50)
turtle.mainloop()

