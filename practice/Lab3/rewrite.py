# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-12 11:45 p.m.

"""
Q1. Write a program that reads a word list from a file and
prints all the sets of words that are anagrams.
"""


def get_words_list():
    with open("/Users/a123/Desktop/paragraph.txt", "r") as f1:
        for i in f1:
            print(i)

