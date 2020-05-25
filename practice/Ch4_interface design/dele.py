# -*- coding:utf-8 -*-
# !/usr/bin/env python

def countdown(n):
    if n <= 0:
        print("blast off")
    else:
        print(n)
        countdown(n - 1)


def factorial(n):  # 阶乘
    if not isinstance(n, int) or n < 0:
        print("要0或正整数哦")
        return None
    if n == 0:  # base case
        return 1
    else:
        result = n * factorial(n - 1)
        return result


def factorial1(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial1(6)
print(f)
