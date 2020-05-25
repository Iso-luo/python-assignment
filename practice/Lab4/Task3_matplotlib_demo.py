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


# 处理一行
def line_process(line, hist):
    line = line.replace('-', " ")
    for w in line.split():  # line.split()是一个list，然后处理每个word中多余的符号
        w = w.strip(string.whitespace + string.punctuation)
        w = w.lower()
        hist[w] = hist.get(w, 0) + 1  # 把一个一个词及对应的count夹在dictionary里面


# 处理文件
def file_process():
    hist = {}
    with open("/Users/a123/Desktop/paragraph.txt", "r") as f1:
        for line in f1:
            line_process(line, hist)
        return hist


def total_words(dic):
    return sum(dic.values())


# process value：将次数变为frequency，给字典的值value排序 {word:frequency}
def sort_items(dic):
    w_f = []  # 创建value列表
    for k, v in dic.items():  # 把{k:v}储存成(v,k)
        w_f.append((v, k))
    w_f.sort(reverse=True)  # 知识点：会按照元组(a,b,c)的第0位进行排序！！！！
    return w_f


# 将元组列表[(k,v),(k,v),()...,()]，变为字典，并添加value1:（log f和log r）
def get_freq_rank(sort_items):
    each_value_list = []
    dic = {}
    r = 1
    # 给字典的每个value添加多个值 变为：{word:[log f,log r],word:[log f,log r],...}
    for i in sort_items:
        each_value_list.append(r)  # 追加 rank
        each_value_list.append(i[0])  # 空列表追加frequency
        dic[i[1]] = each_value_list  # {frequency:rank}
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
        y = v[1]  # frequency
        x = v[0]  # rank
        # print(y, x)
        pyplot.plot(y, x, 'bo')
    pyplot.show()


line1 = "The situation, in Canada-proper presented the British authorities with"

dic1 = file_process()
lst1 = sort_items(dic1)
print(lst1)
dic2 = get_freq_rank(lst1)
print(dic2)
make_plot(dic2)
