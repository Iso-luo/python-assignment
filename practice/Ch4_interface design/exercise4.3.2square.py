# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
2. Add another parameter, named length, to square.
Modify the body so length of the sides is length,
and then modify the function call to provide a second argument.
Run the program again.Test your program with a range of values for length.
"""

import turtle


def square(t, length):      # 添加length
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()


def do_turtle(f, t, length):
    f(t, length)


bob = turtle.Turtle()   # 先创建对象


do_turtle(square, bob, 100)


