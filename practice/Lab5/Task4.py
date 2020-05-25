# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-15 4:43 p.m.

"""
Task 4. Create a Time class that has instant attributes: hour, minutes and seconds.
A. Write a __str__ method for the Time class to print an output in the format: 02:34:10
Hint: Try to use the “format” method of String
"""
from datetime import datetime


class Time:
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        assert 0 <= self.hour <= 23 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59
        return f"{'%02d' % self.hour}:{'%02d' % self.minutes}:{'%02d' % self.seconds}"


t = Time(2, 34, 10)
print(t)

# 使用以下格式 '%02d'%i， 0是占位符
# for i in range(25):
#     print(f"{'%02d' % i}")
"""
B. Write a boolean function called is_after that takes two Time objects, t1 and t2, 
and returns True if t1 follows t2 chronologically and 
False otherwise. Challenge: don’t use an if statement
"""


def is_after(t1, t2):
    if t1.hour < t2.hour:
        return True
    elif t1.minutes < t2.minutes:
        return True
    elif t1.seconds < t2.seconds:
        return True
    else:
        return False


t1 = Time(2, 30, 59)
t2 = Time(2, 30, 49)
print(t1, t2)
print(is_after(t1, t2))
