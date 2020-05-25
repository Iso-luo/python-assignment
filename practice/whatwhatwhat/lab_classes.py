# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-20 4:05 p.m.

class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1

    def printcounter():  # class 里面的function不为对象所用
        return (ExampleClass.counter)


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)
print(ExampleClass.counter)
print(ExampleClass.printcounter())
# print(exampleObject1.printcounter())
print(ExampleClass.__dict__)
