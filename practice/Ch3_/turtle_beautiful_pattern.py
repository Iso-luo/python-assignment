import turtle
import time


#turtle.speed('fastest')
turtle.pensize(2)
turtle.bgcolor('pink')
colors = ['red', 'orange', 'yellow', 'green']
turtle.tracer(False)
for x in range(500):
    turtle.forward(2 * x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
time.sleep(5)
