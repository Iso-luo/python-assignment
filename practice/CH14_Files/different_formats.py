# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-11 10:06 a.m.


# f = open("writing.txt", mode="w", encoding = "utf-8")
# # dir(f.write)
# f.write("this is the file\n")
# f.write("this is a new line\n")

camels = 42
float_val = 0.001
# print("there are %d camels" % (camels))
# print("xxx %d xxx %g"%(camels,float_val))
# print("xxx {a} xxx {b}".format(a = camels, b = float_val))
# print("xxx {} xxxx {} ". format(camels, float_val))
# print("xxx {:.3} xxx {:.2}".format(camels, float_val))

# var1 = "xxx {} xxx {}"
# print(var1.format(3,4))

var = f"xxx {camels} xxx {float_val}"
print(var)

var2 = f"xxx {str(camels)} xxx {float_val}"
print(var2)
