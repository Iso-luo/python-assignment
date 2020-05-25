# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-19 6:12 p.m.


def __str__(self):
    lis0 = self.network_portion
    lis1 = [[], [], [], []]
    res = [[], [], [], []]
    for i in range(4):
        for index in range(8):
            if lis0[i] // 2 ** (7 - index) == 0:
                lis1[i].append(0)
            else:
                lis0[i] = lis0[0] - 2 ** (7 - index)
                lis1[i].append(1)
    for i in range(4):
        res = sum([(lis1[i][index]) * 2 ** (7 - index) for index in range(8)])
        print(res)
    # return res