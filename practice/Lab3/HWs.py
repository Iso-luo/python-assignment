# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-10 1:34 p.m.

"""
Write a program that reads a word list from a file and
prints all the sets of words that are anagrams.
"""


# change file to list
def get_words_list():
    l = []
    with open("/Users/a123/Desktop/words 2.txt", "r") as f1:
        for i in f1:
            words = i.strip()
            l.append(words)
        return l


# compare two words
def is_anagram(s1, s2):
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    if s1 == s2:
        return True
    else:
        return False


# add keys and values to dictionary
def get_all_sets(l):
    index = 0
    lis = []
    d = {}  # an ordinary dictionary
    for i in l:
        for j in l[l.index(i) + 1:]:
            # print(j)
            if is_anagram(i, j):
                d.setdefault(i, []).append(j)
                l.remove(j)
    # return d
    # emerge k v
    for i in d:
        k = [i]
        v = list(d[i])
        k.extend(v)
        lis.append(k)
    # sort list
    len_list = sorted(lis, key=lambda little_list: len(little_list), reverse=True)
    # return len_list
    for i in len_list:
        print(i)
        # return lis


# r = get_words_list()
# print(get_all_sets(r))

"""
Q2. The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that 
takes a list and returns True if there is any element that 
appears more than once. It should not modify the original list.
"""


def has_duplicates(lis):
    for i in range(len(lis)):
        j = i + 1
        while j < len(lis):
            if lis[i] == lis[j]:
                return True
            else:
                j += 1
    return False


# print(has_duplicates([1,(1,2),(3,2),3,4,5,'a','b']))
"""
2. If there are 23 students in your class, 
what are the chances that two of you have the same birthday? 
You can estimate this probability by generating random 
samples of 23 birthdays and checking for matches. 
Hint: you can generate random birthdays with the randint function 
in the random module.
"""
import random


def get_birthdays():
    lis = []
    for i in range(23):
        s = str(random.randint(1920, 2000)) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1, 31))
        lis.append(s)
    return lis


def cal_proportion():
    true_sum = 0
    n = 10000
    for i in range(n):
        if has_duplicates(get_birthdays()):
            true_sum += 1
    p = true_sum / n
    return '{:.4%}'.format(p)


print(get_birthdays())
print(cal_proportion())

"""
Q3. Write a function that takes a list of numbers and 
returns the cumulative sum; that is, a new list where the ith element 
is the sum of the first i+1 elements from the original list. 
For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
"""


def a_func(lis, index):
    if index < 0:
        return 0
    elif index >= 0:
        return lis[index] + a_func(lis, index - 1)


def cumulative_sum(lis):
    new_lis = []
    for i in range(len(lis)):
        print(lis, i)
        new_lis.append(a_func(lis, i))
    return new_lis

# print(a_func([1, 2, 3, 4, 9], 3))
# print(cumulative_sum([1, 2, 3, 4, 5, 22]))
