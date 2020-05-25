# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-04 3:33 p.m.


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


#   method1, use while loop
def is_palindrome(word):
    i = 0
    while i <= (len(word) - 1) // 2:
        if word[i] is word[-(i + 1)]:
            i += 1
        else:
            return False
    if i == (len(word) - 1) // 2 + 1:
        return True


#   method2, use list
def is_palindrome1(word):
    word_a = list(word)
    word_b = list(word)
    word_b.reverse()
    print(word_a, word_b)
    if word_a == word_b:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


# word1 = "ae"
# print("I get:", middle(word1))

word2 = "abcccba"
word3 = "redivider"
print(is_palindrome(word2))
is_palindrome1(word2)
