# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-03 9:04 p.m.


import turtle
import math

wn = turtle.Screen()
wn.bgcolor("grey")


def spiral_turtle(t):
    t.color("white")
    t.shape("turtle")
    t.up()
    for i in range(0, 100, 2):
        t.stamp()
        t.fd(i)
        t.rt(24)


# 画圆 画圈式
def circle_turtle1(t, r, n):
    t.color("white")
    t.shape("turtle")
    t.up()
    for i in range(n):
        t.lt(360.0 / n)
        t.fd(2 * r * math.sin(math.pi / n))
        t.stamp()
        t.up()
    t.lt(90 + 180 / n)
    t.fd(r)
    t.stamp()


# 画圆 发牌试
def circle_turtle2(t):
    t.shape("turtle")
    t.up()
    for i in range(10):
        t.fd(50)
        t.stamp()
        t.bk(50)
        t.lt(36)


def no_name(t):
    t.shape("turtle")
    t.pu()
    for i in range(3):
        t.fd(50)
        t.stamp()


bob = turtle.Turtle()
# wn.exitonclick()
# circle_turtle1(bob, 100, 10)
# circle_turtle2(
no_name(bob)


turtle.mainloop()
