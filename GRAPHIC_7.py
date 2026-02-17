from turtle import*
import colorsys as rs
tracer(10)
pensize(3)
bgcolor("black")
h = 0.8
for i in range(250):
    c = rs.hsv_to_rgb(h,1,1)
    h += 0.004
    color(c)
    up()
    goto(-8,25)
    fd(i)
    down()
    rt(900)
    fillcolor(c)
    begin_fill()
    circle(15, 320)
    end_fill()
    bk(i/4)
    radians
done()
