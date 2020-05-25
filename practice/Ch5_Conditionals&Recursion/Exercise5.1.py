# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-01 11:02 p.m.

"""
Write a script that reads the current time
and converts it to a time of day in hours, minutes, and seconds,
plus the number of days since the epoch.
"""
import time


def year_to_days():
    leap_year = 0  # 闰年
    average_year = 0  # 平年
    for year in range(1970, 2020):
        if year % 4 == 0 and year % 100 != 0:  # 闰年366天
            leap_year += 1
        elif year % 100 == 0:
            if year % 4 == 0:  # 闰年
                leap_year += 1
            else:  # 平年,365天
                average_year += 1
    return leap_year * 366 + average_year * 365


def months_to_days(current_month):
    solar_month = 0  # 大月31天
    lunar_month = 0  # 小月30天
    special_month = 0
    l = [1, 3, 5, 7, 8, 10, 12]
    for month in range(1, current_month):
        if month in l:
            solar_month += 1
        elif month == 2:
            special_month += 1
        else:
            lunar_month += 1
    return solar_month * 31 + special_month * 29 + lunar_month * 30


def convert_time():
    system_seconds = time.time()
    seconds_of_days = (year_to_days() + months_to_days(5)) * 24 * 60 * 60
    remainder_seconds = system_seconds - seconds_of_days
    hours = remainder_seconds // (60 * 60)
    minutes = (remainder_seconds - hours * 60 * 60) // 60
    seconds = (remainder_seconds - hours * 60 * 60 - minutes * 60)
    print("一天中的秒数", remainder_seconds,"\n")
    print("system_seconds:", system_seconds, "\n", year_to_days() + months_to_days(5), "days\n", hours, "hours\n", minutes, "min\n",
          seconds, "sec\n")


convert_time()
print("年化天：", year_to_days())
print("月化天：", months_to_days(5))
