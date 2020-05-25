# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-02 3:29 p.m.


import turtle


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)


bob = turtle.Turtle()
draw(bob, 5, 20)
turtle.mainloop()
