# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-05 10:30 p.m.


# strip 脱掉 split 和strip 都有返回值的！！
ss = "   Hello,   "
ss1 = ss.strip()  # 除去字符串头尾空白，不能删中间部分

ss2_strip1 = ss.strip(',') # 由于，外面还有空白，所以，无法脱去
ss2_strip2 = ss.strip(' ' + ',')  # 使用strip()每次只能脱去最外层
ss3 = ss.lstrip()  # 除去头空白
ss4 = ss.rstrip()  # 除去尾空白

print("*" + ss1 + "*")
print("---------------------------------------------")
print("*" + ss2_strip1 + "*")
print("*" + ss2_strip2 + "*")
print("---------------------------------------------")
print("*" + ss3 + "*")
print("*" + ss4 + "*")
s_replace = ss.replace("o", "***")
print(s_replace)

# food = "banana bread"
# print(food.capitalize())
# print("*"+food.center(50)+"*")
# print("~"+food.ljust(50)+"~")
# print("~"+food.rjust(50)+"~")
# print(food.find("e"))
# print(food.find("na"))
# print(food.find("b"))
# print(food.rfind("e"))
# print(food.rfind("na"))
# print(food.rfind("b"))
# print(food.rfind("a"))

# print("索引: ",food.index("e"))

# s = "python rocks"
# print(s.count("o")+s.count("p"))
# print(s[1]*s.index("o"))

# person = input("ur name:\n")
# greeting = "hello,{},r u {}".format(person, person)
# print(greeting)

# oPrice = float(input("enter Original Price:\n"))
# discount = float(input("enter Discount:\n"))
# newPrice = (1 - discount) * oPrice
# cal = "{:.2f} discounted by {:.3f}% is {:.4f}".format(oPrice, discount, newPrice)
# print(cal)

# a = 5
# b = 9
# setStr = "The set is {{{},{}}}.".format(a, b)
# print(setStr)

# fruit = "banana"
# print("fruit[:3]:", fruit[:3])
# print("fruit[:]:", fruit[:])
# print("fruit[1:1]:", fruit[1:1])
# print("fruit[3: -2]:", fruit[3: -2])
# print("fruit[3:-3]:", fruit[3:-3])
# print("fruit[3:-4]:", fruit[3:-4])
# print("fruit[3:-10]:", fruit[3:-10])
# print("fruit[3:99]:", fruit[3:99])

# ordinal value
# print("1:", ord("1"), "2:", ord("2")) # 1: 49 2: 50
# print("A:", ord("A"), "B:", ord("B")) # A: 65 B: 66
# print("a:", ord("a"), "b:", ord("b")) # a: 97 b: 98
# print(" :", ord(" "))
#
# print("32 is ", chr(32), "!!!!")  # 特殊，32是空格
# print("65: ", chr(65))
# print("97: ", chr(97))

# 字符串是不可改变的 但是可以迭代的
# 字符串是其自身的子字符串，空字符串是任何其他字符串的子字符串
# print('' in 'a')  # ''空字符串
# print('' in 'apple')


# import string
# print(string.ascii_lowercase)  # 小写字母
# print(string.ascii_uppercase)  # 大写
# print(string.digits)
# print(string.punctuation)
# print(string.ascii_letters)  # 大小写字母
# print(string.whitespace)
# print(string.punctuation)
# print(string.printable)

# s = "Abcd"
# s = s.upper()  # upper()1.有返回值2.callable
# print(s)

# line1 = "The situation, in Canada-proper presented the British authorities with"
# line1 = line1.replace("-", " ")  # 返回的依旧是str
# lst = line1.split()  # split() 返回列表，把句子分割成单词word
# print(lst)
