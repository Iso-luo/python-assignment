# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-11 3:35 p.m.

"""
Task 1. Write a program that reads a file,
breaks each line into words, strips whitespace
and punctuation from the words, and converts them to lowercase.
"""
import string


def read_a_file():
    f1 = open("/Users/a123/Desktop/paragraph.txt", "r")
    para = f1.read()  # 获取整个文本
    # print(para)
    # print(para[0]) 可以看出para[0]只表示一个字母，那我们就用空格将每个单词分开
    # 替换所有punctuation,生成word列表
    for i in para:
        if i in string.punctuation + string.whitespace:
            para = para.replace(i, ",")
    para = para.split(",")  # 以"，"分割，返回list
    # 移除所有不符合的元素
    for i in para:
        if i in string.whitespace:  # 发现里面有""，""，
            para.remove(i)  # 要用list.remove().而不是del i
    # 转小写
    new_words = []
    for j in para:
        new_words.append(j.lower())  # j.lower()有返回值 需要用一个新列表接收
    return new_words


print(read_a_file())
