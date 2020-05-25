# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-18 7:12 p.m.
"""
Task5. Write a definition for a class named Kangaroo with
the following methods:
1. An __init__ method that initializes an attribute
named pouch_contents to an empty list.
2. A method named put_in_pouch that takes an object of any
type and adds it to pouch_contents.
3. A __str__ method that returns a string representation of
the Kangaroo object and the contents of the pouch.
Test your code by creating two Kangaroo objects,
assigning them to variables named kanga and roo,
and then adding roo to the contents of kanga’s pouch.
"""


class Kangaroo:
    def __init__(self):
        self.pouch_contents = list()

    def put_in_pouch(self, a):
        self.pouch_contents.append(str(a))

    def __str__(self):
        return ",".join(self.pouch_contents)


kanga = Kangaroo()
roo = Kangaroo()
roo.put_in_pouch("lalala")
roo.put_in_pouch("yayaya")
kanga.put_in_pouch("zazaza")
kanga.put_in_pouch(roo)
print(kanga)