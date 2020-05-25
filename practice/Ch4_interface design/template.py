# -*— coding:utf-8 -*-

import math
import turtle


def polyline(t, n, length, angle):  # 画折线
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):      # 画多边形
    step_angle = 360.0/n             # 圆每个角的度数
    polyline(t, n, length, step_angle)


def arc(t, r, angle):           # 画弧形 angle圆弧所对的角
    arc_length = 2 * math.pi * r * abs(angle) / 360    # 弧长
    n = int(arc_length / 4) + 3     # 边的个数n， 为啥？？？？？？
    step_length = arc_length / n    # 每个边长
    step_angle = float(angle) / n   # 每个角度数
    #t.lt(step_angle/2)              # 为啥？？？？
    polyline(t, n, step_length, step_angle)
    #t.rt(step_angle/2)              #
    turtle.mainloop()


bob = turtle.Turtle()
arc(bob, 100, 270)
# polygon(bob, 5, 100)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

# if __name__ == '__main__':
#     bob = turtle.Turtle()
#
#     # draw a circle centered on the origin
#     radius = 100
#     # bob.pu()
#     bob.fd(radius)
#     bob.lt(90)
#     # bob.pd()
#     turtle.mainloop()
#     circle(bob, radius)
#
#     # wait for the user to close the window

