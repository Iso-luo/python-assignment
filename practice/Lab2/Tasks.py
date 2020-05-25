# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-06 4:15 p.m.

from math import sqrt
import string

"""
Task 1
"""


def square_root(a, x):
    epsilon = 0.0000001
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


print(square_root(33, 8))
'''
Task 2
'''


def test_square_root(x):
    for i in range(1, 10):
        w = '%.1f' % i  # 小数点后取一位
        j = i
        xx = square_root(j, x)
        yy = sqrt(j)
        z = abs(yy - xx)
        print(w.ljust(5), str(xx).ljust(20), str(yy).ljust(20), z, "\t\n")


# test_square_root(10)
"""
Task 3.Write a Python program to add 'ing' 
at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
"""


def word_structure():
    word = input("plz input your word:\n")
    if len(word) < 3:
        print("plz enter a longer word")
        return word
    else:
        if "ing" in word[-3:]:
            word += "ly"
        else:
            word += "ing"
        return word


# print(word_structure())
"""
Task 4. Write a program that reads words.txt and prints only the words with 
more than 20 characters (not counting whitespace).
"""


# method 1
def read_lines():
    file = open("/Users/a123/Desktop/words.txt", "r")
    for i in file:
        if len(i) > 20:
            print(i)


# read_lines()
# method 2
def read_lines2():
    with open("/Users/a123/Desktop/words.txt", "r") as file:
        new_list = []
        for i in file:
            if len(i) > 20:
                new_list.append(i[:-1])  # remove \n,only occupy one array
        print(new_list)


# read_lines2()
"""
Task 5. there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it.
"""


# method 1
def three_consecutive():
    new_word_list = []
    with open("/Users/a123/Desktop/words.txt", "r") as file:
        s = string.ascii_lowercase
        for word in file:
            if len(word) >= 6:
                for i in s:
                    aim_str = i * 2
                    if aim_str in word:
                        for m in s:
                            aim_str = i * 2 + m * 2
                            if aim_str in word:
                                for n in s:
                                    aim_str = i * 2 + m * 2 + n * 2
                                    if aim_str in word:
                                        new_word_list.append(word[:-1])
        return new_word_list


# print(three_consecutive())
# method 2
def three_consecutive2():
    new_word_list = []
    with open("/Users/a123/Desktop/words.txt", "r") as file:
        for word in file:
            if len(word) >= 6:
                for i in range(len(word) - 6):
                    if word[i] == word[i + 1] and word[i + 2] == word[i + 3] and word[i + 4] == word[i + 5]:
                        new_word_list.append(word)
        return new_word_list


# print(three_consecutive2())
"""
Task 6. Write a function called rotate_word that 
takes a string and an integer as parameters, 
and that returns a new string that contains the letters from 
the original string “rotated” by the given amount.

You might want to use the built-in functions ord, which converts a character to a numeric code,
and chr, which converts numeric codes to characters.
"""
import math


def rotate_word(s, num):
    """
    :param s: a string
    :param num: shift number
    :return:
    """
    s = list(s)
    lis = []
    for i in s:
        mark = ord(i) + num
        if ord("a") <= ord(i) <= ord("z"):
            if mark > ord("z"):
                mark = ord("a") + ((mark - ord("z")) % 26-1)
            elif mark < ord("a"):
                mark = ord("z") - ((ord("a") - mark) % 26-1)
        elif ord("A") <= ord(i) <= ord("Z"):
            if mark > ord("Z"):
                mark = ord("A") + ((mark - ord("Z")) % 26-1)
            elif mark < ord("A"):
                mark = ord("Z") - ((ord("A") - mark) % 26-1)
        lis.append(chr(mark))
    return "".join(lis)


# print(rotate_word("cheer", 7))
# print(rotate_word("melon", -10))
# print(rotate_word("A", 3))
# print(rotate_word("Z", 1))


