import turtle
import colorsys as cs
wc = turtle.Screen()
sq = turtle.Turtle()
sq.speed(0)
wc.bgcolor("black")
turtle.delay(100)

for i in range(5):
    step = i * (1/5)
    sq.color(cs.hsv_to_rgb(step,1,1))
    sq.forward(100)
    sq.right(144)
sq.hideturtle()
turtle.done()




