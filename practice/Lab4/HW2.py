# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-14 5:20 p.m.

"""
Q2. In a large collection of MP3 files,
there may be more than one copy of the same song,
stored in different directories or with different file names.
The goal of this exercise is to search for duplicates.
"""
"""
1. Write a program that 
searches a directory and all of its subdirectories, recursively,
and returns a list of complete paths for all files with
a given suffix (like .mp3).
Hint: os.path provides several useful functions for manipulating file and path names.
"""
import os


def walk(dirname):
    """
    :param dirname: 路径字符串
    :return:
    """
    lst = []
    for name in os.listdir(dirname):  # name是dirname的下一级的名称
        path = os.path.join(dirname, name)  # 把路径dirname和其下一级连接起来
        if os.path.isfile(path):  # 路径名指向文件 name是否是filename
            if path.endswith(".png"):
                lst.append(path)
        else:
            lst.extend(walk(path))
    return lst


# lst1 = walk("/Users/a123/Desktop/documents")
# print(lst1)

"""
2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files.
If two files have the same checksum, they probably have the same contents.
"""


def compute_checksum(filename):
    cmd = 'md5 ' + filename
    f1 = os.popen(cmd)
    res = f1.read()
    # stat = f1.close()
    return res


def recognize_duplicates(lst):
    res_list = []
    for path in lst:
        res_list.append(compute_checksum(path).strip("\n"))
    return res_list


# lis = walk("/Users/a123/Desktop/documents")
# print(lis)
# lst2 = recognize_duplicates(lis)
# print(lst2)

"""
3. To double-check, you can use the Unix command diff.
"""


def use_diff(filename1, filename2):
    cmd = 'diff ' + filename1 + " " + filename2
    f1 = os.popen(cmd)
    res = f1.read()
    return res


def second_check(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i, len(lst)):
            if i < len(lst) - 1:
                res = use_diff(lst[i], lst[j])
                print(res)


lis = walk("/Users/a123/Desktop/documents")
print(second_check(lis))
