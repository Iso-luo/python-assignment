# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-10 11:17 p.m.


def solve_list(l):
    """
    :param l: should be a nested list
    :return:
    """
    res = []
    for i in l:
        if isinstance(i, list):
            res.extend(solve_list(i))  # extend作用去括号
        else:
            res.append(i)  # 把XX加在最后一位
    return res


# print(solve_list([[[1]], [3, [2]], [[4], 5], [6, 7], [8, 9]]))
# print(solve_list([1, 2, 3, [4, [1, [3, [1, [3, [5, [1, 2], 5], 4], 2], 4], 2], 5], [[6], 7], [3, 4]]))


def solve_tuple(t):
    """

    :param t: should be a nested tuple
    :return:
    """
    r = []
    if isinstance(t, tuple):
        for i in t:
            r.extend(solve_tuple(i))
    else:
        r.append(t)
    return r


# res = (solve_tuple(((1,), (1, (1, 2, 3, (4, 5))))))
# print(res)

def print_dic(dic):
    for k,v in info:
        print(k)




info = {
    'Nancy': {
        'fruits': [{'apple': 3}, {'strawberry': 4}, {'banana': 5}],
        'money': 89
    },
    'Frank': {
        'fruits': [{'grape': 5}, {'orange': 2}, {'cherry': 20}, {'apple': 8}],
        'money': 102
    },
    'Zoey': {
        'fruits': [{'strawberry': 18}, {'cherry': 23}, {'lemon': 6}],
        'vegetables': [{'tomato': 4}, {'potato': 8}, {'tofu': 1}],
        'money': [{'fruits': 100}, {'vegetables': 20}]
    }
}

print_dic(info)
