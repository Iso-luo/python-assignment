# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-02 3:54 p.m.
"""
To draw a Koch curve with length x, all you have to do is
1. Draw a Koch curve with length x/3.  2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.  4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.  6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.
"""
'''
1. Write a function called koch that 
takes a turtle and a length as parameters, 
and that uses the turtle to draw a Koch curve 
with the given length.
'''

import turtle
import math


def koch(t, n):
    if n < 10:
        t.fd(n)
        return None
    m = n / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()
