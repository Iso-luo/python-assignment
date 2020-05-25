# -*- coding: UTF-8 -*-
# !/usr/bin/env python


def right_justify(s):
    print('\r'*(6-len(s)))  # \r return
    for i in s:
        print(i+'\r')


right_justify('monty')





