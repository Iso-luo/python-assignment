# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-11 11:26 a.m.

# var1 = 19
# var2 = 83.9834
# var3 = False
# var4 = [123, "hello", True, var2]
# var5 = {'a': 2, ('first', 'last'): ['james', 'williams']}
# # var6 =
# var7 = str("hello python")
# print(type(var7))
# dt = dict()
# print(type(dt))


# Defining own class
class Point():  # classname with capital letter, func with 小写字母
    """
    this represents a point in 2-D
    """

    # x = 333
    # y = 222

    # constructor??
    def __init__(self):  # 在class里的function叫做method，每一个method 参数都要有self
        """
        this is a contructor in python
        this method is called whenever you initialize a new object from a class
        每次创建一个instance实例的时候 该方法__init__(self)都会被调用
        """
        print("我是__init__(),我被调用了")
        print("打印self的内容： ", self)  # 该操作打印了class的一个instance地址值， self相当于java的this
        self.x = 0
        self.y = 0

    def my_method(self):
        print("pXXX.my_method()： 调用我自己的方法")

    def my_method222(self, xxx, yyy):
        print(xxx, yyy, "\t")


print("*", dir(Point))
# print(help(Point))#-->None
print("--------------------------------------------------------")
p1 = Point()  # 创建对象！！p1 is an instance of this class
print(p1)
p1.my_method()
p1.my_method222("花花", "狗狗")
print("--------------------------------------------------------")
p2 = Point()  # 创建对象！！p2 is an instance of this classes
print(p2)
print("--------------------------------------------------------")
p3 = Point()  # 创建对象！！p3 is an instance of this classes
print(p3)
print("--------------------------------------------------------")

print(p1.__dict__)
print("--------------------------------------------------------")
#
p1.x = 10  # instance attributes, the attributes of object p1
p1.y = 5  # instance attributes

print(p1.x)
print(p2.x)  # p2沿用父类中的x
print("属性attribute __dict__: ", p1.__dict__)
print("属性attribute __dir__: ", p1.__dir__())
print("属性attribute __hash__: ", p1.__hash__())
print("属性attribute __class__: ", p1.__class__)
print("--------------------------------------------------------")
x_axis = p1.x + p2.x
print(x_axis)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
print("--------------------------------------------------------")
print(p1)
del p1
print(Point)
print("--------------------------------------------------------")
