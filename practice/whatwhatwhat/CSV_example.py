# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-20 9:48 a.m.

import csv
with open('csv_example.csv') as f:
    csv_python = csv.reader(f)

    # for row in csv_python:
    #     print("{device} is in {location}"\
    #           "and has IP {ip}.".format(
    #             device = row[0],
    #             location = row[2],
    #             ip = row[1]
    #              )
    #           )
    for row in csv_python:
        device = row[0],
        location = row[2],
        ip = row[1]

        print(f"{device} is in {location}"\
              f"and has IP {ip}")

