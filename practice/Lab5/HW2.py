# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-19 4:25 p.m.
"""
Q2.The IP address class should be instantiated by a four-item list
(where the first item in the list is the highest octet in the address)
and a mask (should be represented by an integer of value 0 to 32)
• method getNetwork() returns a list representing the network portion of the IP address
• method getMask() return a list representing the mask as four octets (i.e. 255.255....)
• method getAddress() returns a list representing the address
• implement __str__ method to print the IP address
"""


class IPv4Address:
    def __init__(self, network_portion, mask):
        self.network_portion = network_portion
        self.mask = mask

    def get_network(self):
        lis = []
        for i in self.network_portion:
            if self.network_portion.index(i) < 4:
                lis.append(i)
            else:
                lis.append(0)
        return lis

    def get_mask(self):
        lis = []
        l0, l1, l2, l3 = [], [], [], []
        for i in range(33):
            if i < self.mask:
                lis.append(1)
            else:
                lis.append(0)
        for index in range(len(lis)):
            if 0 <= index <= 7:  # index()对于不同位置的相同值，只显示第一个坐标
                l0.append(lis[index])
            elif 8 <= index <= 15:
                l1.append(lis[index])
            elif 16 <= index <= 23:
                l2.append(lis[index])
            else:
                l3.append(lis[index])
        res0 = sum([(l0[index]) * 2 ** (7 - index) for index in range(8)])
        res1 = sum([(l1[index]) * 2 ** (7 - index) for index in range(8)])
        res2 = sum([(l2[index]) * 2 ** (7 - index) for index in range(8)])
        res3 = sum([(l3[index]) * 2 ** (7 - index) for index in range(8)])
        return [res0, res1, res2, res3]

    def __str__(self):
        return str(self.network_portion)


ipv4 = IPv4Address([10, 0, 1, 7], 26)
net = ipv4.get_network()
mask = ipv4.get_mask()
print(net, mask)
print(ipv4)
