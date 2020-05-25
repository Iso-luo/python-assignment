# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-08 4:29 p.m.
from functools import reduce

"""
Task 1. Write a function called nested_sum
that takes a nested list of integers
and adds up the elements from all the nested lists.
"""


def solve_list(l):
    res = []
    for i in l:
        if isinstance(i, list):
            res.extend(solve_list(i))
        else:
            res.append(i)
    return res


print(solve_list([[[1]], [3, [2]], [[4], 5], [6, 7], [8, 9]]))
# print(solve_list([1, 2, 3, [4, [1, [3, [1, [3, [5, [1,2], 5], 4], 2], 4], 2], 5], [[6], 7], [3, 4]]))
# print(solve_list([1, 2, 3, [4, [1, [3, [1, [3, [5, [1,2], 5], 4], 2], 4], 2], 5], [[6], 7], [3, 4]]))
# print(solve_list22([1, 2, 3, [4, [1, [3, [1, [3, [5, [1,2], 5], 4], 2], 4], 2], 5], [[6], 7], [3, 4]]))


"""
Task 2. Using the built-in reduce function, 
write a program to find the sum of even numbers between 100 and 500
"""


def get_sum():
    num_list = []
    [num_list.append(num) for num in range(100, 501)]
    num_list = num_list[:501:2]
    return reduce(lambda x, y: x + y, num_list)  # lambda:Anonymous function


# print(get_sum())
"""
Task 3. Using the built-in map function, 
write a program that takes in a list of letter in lowercase 
and returns another list of the letters in uppercase.
"""


# method 1:
def a_func(x):
    x = x.upper()
    return x


def use_map(give_a_list):
    lis = []
    r = map(a_func, give_a_list)
    for j in r:
        lis.append("".join(j))  # j list-->str
    return lis


# method2: use anonymous function
def use_map1(give_a_list):
    lis = []
    res = map(lambda x: x.upper(), give_a_list)  # lambda x: 冒号后面写如何操作x
    for i in res:
        lis.append(i)
    return lis


# method3: use list comprehensions
def use_map3(give_a_list):
    lis = []
    [lis.append(i) for i in map(lambda x: x.upper(), give_a_list)]  # append(无返回值)
    return lis


# print(use_map(['a', 'b', 'c', 'e', 'g', 'h']))
# print(use_map1(['a', 'b', 'c', 'e', 'g', 'h']))
# print(use_map3(['a', 'b', 'c', 'e', 'g', 'h']))
"""
Task 4. Given a list of number, 
return a list of the numbers that are multiples of 5. 
(Use the Built-in filter functions)
"""


def use_filter(a_list):
    lis = []
    [lis.append(i) for i in filter(lambda x: x % 5 == 0, a_list)]
    print(lis)


# use_filter(range(20))
"""
Task 5. Two words are anagrams if you can rearrange 
the letters from one to spell the other. 
Write a function called is_anagram that takes two strings and returns True. if they are anagrams.
"""


def is_anagram(s1, s2):
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    if s1 == s2:
        return True
    else:
        return False


# print(is_anagram("abcd", "dcba"))
"""
Task 6. Write a function that reads the words in “words.txt” and 
stores them as keys in a dictionary. It doesnt matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""


def check_dic(s):
    with open("/Users/a123/Desktop/words_copy.txt", "r") as file:
        words_text = file.read()
        words_list = words_text.split()
    dic = {}
    for i in words_list:
        dic[i] = ""
    if s in dic:
        return True
    else:
        return False


# print(check_dic("aaa"))

"""
Task 7. get(),set()
"""
dic = {'a': 11, 'b': 22, 'c': 33}
s1 = dic.get('a', "not exist")
s2 = dic.get('d', "not exist")
# print(s1)
# print(s2)
s3 = dic.setdefault("f", []).append("222")
# print(dic)
"""
Task 8. Write a function called XXX that takes any number of arguments and returns their sum. 
Use the code snippet below as template:
"""


def lis(t):
    r = []
    if isinstance(t, tuple):
        for i in t:
            r.append(lis(i))
    else:
        r.append(t)
    return r


def solve_list1(l):
    i = 0
    j = 0
    n = 0
    res = []
    while i < len(l):
        if isinstance(l[i], list):  # 查看l[i]元素是否是list
            l.extend(l[i])
            solve_list(l[i])
            del l[i]
        i += 1
    res.append(l)


# res = lis(((1), (1, (1, 2, 3, (4, 5)))))
# print(solve_list(res))
# print(lis(((1), (1, (1, 2, 3, (4, 5))))))
# print(strip_list(r))


# print(tuple_to_list(((1,),(1,(1,2,3,(4,5 )))))
# print(solve_list([1, 2, 3, [4, [5, 6, [7, [8, [9, [10, [11, [12]], 13], 14], 15], 16], 17], [[18]]], [19, 20]]))
"""
Task 9
Write a function called ‘most_frequent’ that 
takes a string and prints the letters in decreasing order of frequency.
"""


def most_frequent(s):
    l = []
    [l.append(i) for i in s]
    l.sort()
    return "".join(l)


print(most_frequent("zhksnfvks"))
