# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-12 11:53 a.m.

"""
Write a program that
1.reads a text from a file,
2.counts word frequencies, and
3.prints one line for each word, in descending order of frequency, with log f and log r.
Use the graphing program of your choice to plot the results and check whether they form a straight line.
Can you estimate the value of s?
"""
import string
import matplotlib.pyplot as pyplot


# 获取文本words列表
def get_words_list():
    with open("/Users/a123/Desktop/paragraph.txt", "r") as f1:
        f2 = f1.read()  # 这里如果是.deadline() 则已经是一个列表，for循环需要主要列表的位
        for i in f2:
            if i in string.whitespace + string.punctuation:
                f2 = f2.replace(i, ",")  # 替换后，会出现 '，，'
    f2 = f2.split(',')  # split 以'，'分割，切成列表，返回列表
    for i in f2:
        if i in "" + string.whitespace + string.punctuation:  # 因为有的位之前只有一个'，'，split后为空值
            f2.remove(i)
    # 转小写
    new_words = []
    for j in f2:
        new_words.append(j.lower())  # j.lower()有返回值 需要用一个新列表接收
    return new_words


# 一共多少字
def count_words(words_list):
    words_len = len(words_list)
    return words_len


# 给字典添值:如果字典中有该字，则value+1，否则添加键值对 k=word,v=1
def add_value(dic, word, words_list):
    if word in dic:
        dic[word] = dic.get(word) + 1 / count_words(words_list)  # 每增加一个word f增加（1/总字数）
    else:
        dic[word] = 1 / count_words(words_list)
    return dic


# 生成{word:频率}字典
def words_frequency(words_list):
    dic = {}
    count = 0
    for i in words_list:
        # print(i)
        add_value(dic, i, words_list)
    return dic


# process value：将次数变为frequency，给字典的值value排序 {word:frequency}
def sort_values(dic):
    lis_v = []  # 创建value列表
    for k, v in dic.items():
        lis_v.append(v)
    lis_v.sort(reverse=True)  # 按频率从大到小排列 descending order
    return lis_v


# 在原来的dict找到value对应的key,生成key的列表
def get_corresponding_key(dic, lis_v):
    lis_k = []  # 创建key列表
    for v in lis_v:
        for k1, v1 in dic.items():
            if v == v1:
                lis_k.append(k1)
    return lis_k


# 合并键值对 word:frequency,生成元组列表[(k,v),(k,v),()...,()]
def emerge_key_value(lis_k, lis_v):
    new_order = []
    zipped = zip(lis_k, lis_v)  # 生成zip对象,[(),(),()...,()]
    # print(zipped)
    for i in zipped:  # 遍历列表中的元组
        new_order.append(i)
    return new_order


# 将元组列表[(k,v),(k,v),()...,()]，变为字典，并添加value1:（log f和log r）
def get_f_rank(new_order_lis):
    each_value_list = []
    dic = {}
    r = 1
    # 给字典的每个value添加多个值 变为：{word:[log f,log r],word:[log f,log r],...}
    for i in new_order_lis:
        each_value_list.append(i[1])  # 空列表追加frequency
        each_value_list.append(r)  # 追加 rank
        dic[i[0]] = each_value_list  # {frequency:rank}
        each_value_list = []  # 重置用于添加字典values的列表
        r += 1
    return dic


def make_plot(dic):
    pyplot.clf()  # Clear figure清除所有轴，但是窗口打开，这样它可以被重复使用。
    pyplot.xscale('log')  # 指定x轴 线性刻度、指数刻度
    pyplot.yscale('log')  # 指定y轴线性刻度、指数刻度
    pyplot.title('Verifying Zipf', color='grey', fontsize="large")
    pyplot.xlabel('rank of frequency ')
    pyplot.ylabel('frequency')
    for k, v in dic.items():
        y = v[0]  # frequency
        x = v[1]  # rank
        # print(y, x)
        pyplot.plot(y, x, 'bo')
    pyplot.show()


lis = get_words_list()
dic1 = words_frequency(lis)
lis_v1 = sort_values(dic1)
lis_k1 = get_corresponding_key(dic1, lis_v1)
new_order1 = emerge_key_value(lis_k1, lis_v1)
dic2 = get_f_rank(new_order1)
# print(dic2)
make_plot(dic2)
