# -*- coding: UTF-8 -*-
# !/usr/bin/env python


def get_plus_minus():
    a = '+ '+('- '*4)  # +----
    return a


def get_vertical():
    b = '|'+(" "*9)    # |
    return b


def get_many(f, num):   # 拼接 num次
    c = f() * num
    return c


def print_horizon(d, sign): # 组合重复部分和
    print(d+sign)


def do_cycle(x):    # x 为
    for i in range(0, x*5+1):
        if i % 5 == 0:
            print_horizon(get_many(get_plus_minus, x), '+')
        else:
            print_horizon(get_many(get_vertical, x), '|')


do_cycle(2)
do_cycle(4)
do_cycle(5)

