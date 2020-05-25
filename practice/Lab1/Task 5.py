# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-04 2:56 p.m.

"""
Task 5
1. Write a function that draws a grid like the following:
"""


def plus_minus(n):
    '''

    :param n: the number of "+---"
    :return:
    '''
    for i in range(n):
        print("+", "- " * 3, end="")
    print("+\r")


def vertical(n):
    '''

    :param n: the number of "|   "
    :return:
    '''
    for j in range(4):
        for i in range(n):
            print("|", "  " * 3, end="")
        print("|\r")


def multiple(n,m):
    '''

    :param n: number of rows
    :param m: number of columns
    :return:
    '''
    for i in range(m):
        plus_minus(n)
        vertical(n)
    plus_minus(n)

'''
2. Write a function that draws a similar grid 
with four rows and four columns.
'''

multiple(4, 5)