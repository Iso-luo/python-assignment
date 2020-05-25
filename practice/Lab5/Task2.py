# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-15 4:01 p.m.
"""
Task 2. Create a new class called Rectangle,
this class will have width, height and corner attributes.
The corner attribute is an instance of the Point class created in task1.
"""
"""
A. Write a function called “find_center” that takes a Rectangle has an argument and 
returns a Point that contains the coordinates of the center of the Rectangle. 
(Assuming the corner of the rectangle is on the origin)
"""


class Point:
    x = 0.0
    y = 0.0


class Rectangle:  # 如果写成Rectangle(Point),则表示继承Point类了，所以不能这么写
    width = 100.0
    height = 200.0
    corner = Point


# p1 = Point()
# rec = Rectangle()
# print(rec.corner.x)

# 找到矩形的中心坐标
def find_center(rec):
    rec.corner.x = rec.width / 2
    rec.corner.y = rec.height / 2
    return rec.corner.x, rec.corner.y


"""
B. Write a function named move_rectangle that takes a Rectangle and 
two numbers named dx and dy. It should change the location of the rectangle by 
adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.
"""


# 移动矩形，角的坐标从(0,0)变为(1,1)
def move_rectangle(rec, dx, dy):
    rec.corner.x = rec.corner.x + dx
    rec.corner.y = rec.corner.y + dy
    return rec.corner.x, rec.corner.y


p2 = Point()
rec1 = Rectangle()
# print(find_center(rec1))
print(move_rectangle(rec1, 1, 1))
