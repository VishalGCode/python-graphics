from turtle import *

speed(0)
bgcolor("black")
pensize(2)

for i in range(135):
    fd(i)
    rt(150)
    color("#909090")
    for a in range(2):
        fd(i)
        lt(35)
        hideturtle()

done()