# -*- coding: UTF-8 -*-
# !/usr/bin/env python


def do_twice(f, x):     # runs a function twice
    f(x)
    f(x)


def print_twice(bruce):     # prints the argument twice
    print(bruce)
    print(bruce)


do_twice(print_twice, "spam")   # runs a function twice


def do_four(f4, x4):    # runs a function four times
    do_twice(f4, x4)
    do_twice(f4, x4)


do_four(print_twice, "I'm do_four")


