# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-06 6:18 p.m.

"""
Q1. Write a function called estimate_pi that uses this formula
to compute and return an estimate of π.
It should use a while loop to compute terms of the summation
until the last term is smaller than 1e- 15 (which is Python notation for 10−15).
You can check the result by comparing it to math.pi.
"""
from math import sqrt, pow, factorial, pi, exp, e


def estimate_pi():
    a = 2 * sqrt(2) / 9801
    k = 0
    x = 0
    y = 0.1  # Assign a number which bigger than 0 for y randomly!!!
    while y > 1e-15:
        y = factorial(4 * k) * (1103 + 26390 * k) / (pow(factorial(k), 4) * pow(396, (4 * k)))
        x += y
        k += 1
    result = 1 / (a * x)
    return result


# print(estimate_pi())


"""
Q2. Write a function that takes a string as an argument 
and displays the letters backward, one per line.
"""


# method 1
def reverse_word(s):
    s = list(s)
    new_letter = []
    for i in range(len(s)):
        new_letter.append(s[-i - 1])
    return "".join(new_letter)


# print(reverse_word("abcd"))
# print(reverse_word("abcdefg"))


# method2
def reverse_word2(s):
    letter = []
    [letter.append(i) for i in s[::-1]]  # [::-1] traverse from back to front
    return "".join(letter)


# print(reverse_word2("abcdf"))
"""
Q3. There is a string method called count. Read the documentation of this method 
and write an invocation that counts the number of a(s)’ in 'banana'.
"""


def invocation():
    s = "banana"
    num = s.count("a", 0, len(s))
    return num


# print(invocation())
"""
Q4. A step size of -1 goes through the word backwards, 
so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from lab 1.
"""


def is_palindrome(s):
    new_list = []
    [new_list.append(i) for i in s[::-1]]
    new_word = "".join(new_list)
    if new_word == s:  # the values of two strings are equal but addresses values are different
        return True
    return False


# print(is_palindrome("abcacba"))
# print(is_palindrome("redivider"))

"""
Q5
Write a function called has_no_e that returns True if the given word doesnt have the letter “e” in it.
Modify your program from the previous section to 
print only the words that have no “e” 
and compute the percentage of the words in the list have no “e.”
"""


# def has_no_e(word):
#     if "e" not in word:
#         return True
#     return False

def has_no_e(word):
    return not ("e" in word)


# print(has_no_e("word"))


def judge():
    count = 0
    total = 0
    word_list = []
    with open("/Users/a123/Desktop/words.txt", "r") as file:
        for i in file:
            if "e" not in i:
                count += 1
                word_list.append(i[:-1])
            total += 1
        print(("the percentage of having no 'e': {:.2%}".format(count / total)), "\n", "\n".join(word_list))


print(judge())
