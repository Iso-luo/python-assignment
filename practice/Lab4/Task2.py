# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-12 9:35 a.m.
"""
Task 2
"""
"""
A. count the total number of words in the book,
and the number of times each word is used.
"""
import string


# 获取文本words列表
def get_words_list():
    with open("/Users/a123/Desktop/paragraph.txt", "r") as f1:
        f2 = f1.read()  # 这里如果是.deadline() 则已经是一个列表，for循环需要主要列表的位
        for i in f2:
            if i in string.whitespace + string.punctuation:
                f2 = f2.replace(i, ",")  # 替换后，会出现 '，，'
    f2 = f2.split(',')  # split 以'，'分割，切成列表，返回列表
    for i in f2:
        if i in string.whitespace:  # 因为有的位之前只有一个'，'，split后为空值
            f2.remove(i)
    return f2


# 一共多少字
def count_words(words_list):
    words_len = len(words_list)
    return words_len


# 给字典添值:如果字典中有该字，则value+1，否则添加k=word,v=1
def add_value(dic, word):
    if word in dic:
        dic[word] = dic.get(word) + 1
    else:
        dic[word] = 1
    return dic


# 生成{word频率}字典
def words_frequency(words_list):
    dic = {}
    count = 0
    for i in words_list:
        # print(i)
        add_value(dic, i)
    return dic


"""
B. print the 20 most frequently-used words in the book.
"""


# 给字典的值value排序
def dic_sort(dic):
    lis_v = []
    lis_k = []
    for k, v in dic.items():
        lis_v.append(v)
    lis_v.sort(reverse=True)
    n = 0
    for v in lis_v:
        for k1, v1 in dic.items():
            if v == v1:
                lis_k.append(k1)
    return lis_k


def first_20_words(lis):
    words_l = []
    if len(lis) < 20:
        return "plz give a list longer than 20"
    else:
        for i in range(20):
            words_l.append(lis[i])
    return words_l


# l = get_words_list()
# dic1 = words_frequency(l)
# lis1 = dic_sort(dic1)
# print(first_20_words(lis1))

"""
C. Print the number of different words 
used in the book
"""


# 打印所有的key
def get_keys(dic):
    return dic.keys()  # 一步到位
    # for item in dic:
    #     print(item)


lis = get_words_list()
dic1 = words_frequency(lis)
print(get_keys(dic1))
