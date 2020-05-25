# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-13 9:47 a.m.


"""
Q1. Write a program that reads a word list from a file and
prints all the sets of words that are anagrams.

需要重写！！！！！！！！1
"""
import string


# 读取单词 生成列表
def get_words_list():
    l = []
    with open("/Users/a123/Desktop/paragraph.txt", "r") as f1:
        f2 = f1.read()
        for i in f2:
            if i in "" + string.whitespace + string.punctuation:
                f2 = f2.replace(i, ",")
        f2 = f2.split(",")
        for i in f2:
            if i in "" + string.whitespace + string.punctuation:
                f2.remove(i)
        return f2

        # for i in f1:
        #     words = i.strip()  #
        #     l.append(words)
        # return l


# 判断是否同字母单词
def is_anagram(s1, s2):
    if len(s1) == len(s2):
        s1 = list(s1)
        s1.sort()
        s2 = list(s2)
        s2.sort()
        return s1 == s2
    else:
        return False


# add keys and values to dictionary
def get_all_sets(l):
    ide = 0
    new_l = []
    d = {}  # an ordinary dictionary
    # 把同字母词放在键值对中
    for i in l:
        new_l.insert(ide, i)
        for j in l[l.index(i) + 1:]:
            # print(j)
            if is_anagram(i, j):
                # new_l.insert(ide, j)
                d.setdefault(i, []).append(j)
                del j
        ide += 1
        print(l)
        print(new_l)
    return new_l
    # # 将键值对kv放在列表的同一位
    # for i in d:
    #     k = [i]
    #     v = list(d[i])
    #     k.extend(v)
    #     lis.append(k)
    # # sort list
    # len_list = sorted(lis, key=lambda little_list: len(little_list), reverse=True)
    # # return len_list
    # for i in len_list:
    #     print(i)
    #     # return lis

# r = get_words_list()
# print(get_all_sets(r))
