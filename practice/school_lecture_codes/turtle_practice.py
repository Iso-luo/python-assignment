# -*- coding:utf-8 -*-
# !/usr/bin/env python

import turtle
import math


def square():
    for i in range(4):
        bob.fd(100)
        bob.lt(90)


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


if __name__ == '__main__':
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  # set the window background color
    bob = turtle.Turtle()
    bob.color("darkgreen")  # make tess blue
    bob.pensize(3)  # set the width of her pen
    # draw a circle centered on thr origin
    radius = 100
    bob.pu()  # 提笔
    bob.fd(radius)
    bob.lt(90)
    bob.pd()  # 落笔
    circle(bob, radius)
    # waiting for user to close the window
    turtle.mainloop()
