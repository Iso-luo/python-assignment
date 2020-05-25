# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-07 9:58 p.m.

infile = open("/Users/a123/Desktop/words2.txt", "r")
aline = infile.readline()  # readline()只读一行,返回str,指针自动移到下一行
print("*aline: ", aline, type(aline))
print("\n\n")
line_list = infile.readlines()  # readlines()逐行读取,返回列表[str,str,..]
print("*line_list: ", line_list)
print(len(line_list))  # 行数,list位数
print(line_list[0:4])  # index(0~3)
print("\n\n")
infile = open("/Users/a123/Desktop/words2.txt", "r")
file_string = infile.read()  # read())读取整个文本，返回str
print("*file_string: \n", file_string, type(file_string))
print(len(file_string))
print("\n\n")
words_list = file_string.split()  # split()有返回值，返回分割后的列表！！！
print("$$$", words_list)
