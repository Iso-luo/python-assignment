# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-17 4:27 p.m.
"""
Task4.
1. Read the documentation and
2. use it to print the names of the files in a given directory and
its subdirectories.
"""
import os


def walk(dirname):
    for name in os.listdir(dirname):        # name是文件或文件夹的名字
        print(name)
        path = os.path.join(dirname, name)  # directory+subdirectories
        if os.path.isfile(path):            # 是否是文件
            print(path)
        else:
            walk(path)


walk("/Users/a123/Desktop/documents")
