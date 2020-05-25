# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-14 6:31 p.m.

import os

# def walk(dirname):
#     for name in os.listdir(dirname):
#     path = os.path.join(dirname, name)
#     if os.path.isfile(path):
#         print(path)
#             else:
#                 walk(path)

l = os.listdir("/Users/a123/Desktop")
print("os.listdir(): ",l)

print("1:", os.path.join('/aaa', 'bbb', 'ccc.txt'))

# '/bbb'有/的时候，/aaa就不要了
print("2:", os.path.join('/aaa', '/bbb', 'ccc.txt'))

print("3:", os.path.join('aaa', '/bbb', 'ccc.txt'))

# ./不知道啥意思
print("4:", os.path.join('aaa', './bbb', 'ccc.txt'))

# /ccc.txt 前面有/时，前面的路径就都不要了？？？？？
print("5:", os.path.join('/aaa', '/bbb', '/ccc.txt'))

print("6:", os.path.join('aaa', 'bbb', '/ccc.txt'))

# 判断是不是文件
path = os.path.isfile("/Users/a123/Desktop/mydownload/exam.ipynb")
print(path)

# 生成当前的绝对路径
path1 = os.path.abspath("../fresh")
print(path1)

# 当前文件或文件夹是否存在
path2 = os.path.exists("mydownload")
print(path2)

path3 = os.path.isdir("/Users/a123/Desktop")
print(path3)
