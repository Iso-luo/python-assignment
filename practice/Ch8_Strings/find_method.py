# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-06 7:40 a.m.

# method 1
def find1(a_string, a_char):
    i = 0
    while i < len(a_string):
        if a_string[i] == a_char:
            return i
        else:
            i += 1
    if i == len(a_string):
        return -1


# method 2
def find2(a_string, a_char):
    i = 0
    while i < len(a_string):
        if a_string[i] == a_char:
            return i
        else:
            i += 1
    if i == len(a_string):
        return -1


# method 2
# def find(astring, achar):
#     ix = 0
#     found = False
#     while ix < len(astring) and not found:
#         if astring[ix] == achar:
#             found = True
#         else:
#             ix = ix + 1
#     if found:
#         return ix
#     else:
#         return -1


# print(find("Compsci", "p"))
# print(find("Compsci", "C"))
# print(find("Compsci", "i"))
# print(find("Compsci", "x"))

print(find2("Compsci", "p"))
print(find2("Compsci", "C"))
print(find2("Compsci", "i"))
print(find2("Compsci", "x"))

