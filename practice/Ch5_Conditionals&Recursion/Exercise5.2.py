# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-02 1:41 p.m.
"""
Exercise 5.2. Fermat’s Last Theorem says that
there are no positive integers a, b, and c such that a^n + b^n = c^n
for any values of n greater than 2.
1. Write a function named check_format that takes four parameters- a, b, c and n
and checks to see if Fermat’s theorem holds. If n is greater than 2 and
a^n + b^n = c^n
the program should print, “Holy smokes, Fermat was wrong!”
Otherwise the program should print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n,
converts them to integers, and uses check_format to check
whether they violate Fermat’s theorem.
"""


def check_format():
    a = int(input('plz enter a:\n'))
    b = int(input('plz enter b:\n'))
    c = int(input('plz enter c:\n'))
    n = int(input('plz enter n:\n'))
    if n > 2:
        if a ^ n + b ^ n == c ^ n:
            print("Holy smokes,Fermat was wrong!")
        else:
            print("No, that doesn’t work.")
    else:
        print("plz enter an 'n' which is lager than 2")


check_format()
