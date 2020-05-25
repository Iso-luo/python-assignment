# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-04 10:50 a.m.


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return     # return 就是跳出循环了
            # print(index) 输出1 3 5
        index += 1
    return -1


def in_both(letter, a,b):
    for letter in a:
        if letter in b:
            print(a.index(letter))
        else:
            print("No")


# find("banana", "a")

word = 'banana'
word2 = "apple"
new_word = word.upper()
# print(new_word)
print(word.find("a"))
print("a" in word)
in_both("a", word,word2)

