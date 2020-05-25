# -*- coding:utf-8 -*-
# !/usr/bin/env python


"""
1. Write a function called square that takes a parameter named t,
which is a turtle. It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square,
and then run the program again.
"""

import turtle


def square(t):
    t = turtle.Turtle()  # 创建对象
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()


def do_turtle(f, t):
    f(t)


bob = turtle.Turtle()


do_turtle(square, bob)
