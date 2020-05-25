# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-07 11:25 p.m.

infile = open("/Users/a123/Desktop/words_copy.txt", "r")
aline = infile.readline()  # readline()只读一行,返回str, 指针自动下移到第二行
print("用readline(): ", aline, type(aline))
print("-------------------------------------------------------")
line_list = infile.readlines()  # readlines()逐行读取,返回[str,...]
print("用readlines(): ", line_list)
print(len(line_list))  # 行数,list位数
print(line_list[0:4])  # index(0~3)
print("-------------------------------------------------------")
infile = open("/Users/a123/Desktop/words_copy.txt", "r")#指针已经指到结尾，需要重新打开文件
file_string = infile.read()  # read())读取整个文本，返回str
print("用read(): ", file_string, type(file_string))
print(len(file_string))
print("-------------------------------------------------------")

# 从文本获取单词
def char_count():
    l = []
    fin = open("/Users/a123/Desktop/words_copy.txt", "r")
    print(type(fin),fin,end="!!!")
    print("-------------------------------------------------------")
    for i in fin:
        w = i.strip()  # 得到每个单词
        l.append(w)
    return l


print(char_count())
