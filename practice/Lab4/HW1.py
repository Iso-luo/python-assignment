# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-12 6:26 p.m.

"""
Q1.Modify the previous program to read a word list and then
print all the words in the book that are not in the word list.
How many of them are typos?
How many of them are common words that should be in the word list,
and how many of them are obscure?
Python provides a data structure called set that
provides many common set operations.
Read the documentation and write a program that uses set subtraction
to find words in the book that are not in the word list.
"""
import string


def word_process(line, lst):
    line = line.replace("-", " ")
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace + "")
        word = word.lower()
        lst.append(word)


# 返回单词list
def file_process(filename):
    lst = []
    with open(filename, "r") as f1:
        for i in f1:
            word_process(i, lst)
    return lst


def subtract(lst1, lst2):
    return set(lst2) - set(lst1)


words_list = file_process("/Users/a123/Desktop/words.txt")
article_list = file_process("/Users/a123/Desktop/A Modest Proposal.txt")
not_in_word_list = subtract(words_list, article_list)
print("not_in_word_list:", not_in_word_list)
