# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-17 5:32 p.m.

"""
Task5. read the first file and write the contents into the
second file (creating it if necessary).
If an error occurs while opening,
reading,
writing,
or closing files,
your program should catch the exception, print an error message, and exit.
"""
import os


def sed(f_name1, f_name2):
    try:
        with open(f_name1, "r") as f1:
            content = f1.read()
            # if os.path.isfile(f_name2):
            with open(f_name2, "a") as f2:  # with open的时候，如果没有f_name2文件夹，会自动创建出来
                f2.write(content)
    except IOError:
        print("Error: no such", f_name1, "file")
    finally:
        f1.close()


sed("/Users/a123/Desktop/paragraph.txt", "/Users/a123/Desktop/paragraph001.txt")  # 注意paragraph01.txt前面没有slash(/)
