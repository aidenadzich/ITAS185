import turtle
import tkinter
import random

t = turtle.Turtle()


def draw(x, y):
    t.penup()
    t.setpos(x, y)
    colour = random.choice(['red', 'green', 'blue', 'magenta'])
    t.fillcolor(colour)
    t.begin_fill()
    t.pendown
    t.circle(10)
    t.end_fill()
    t.penup

def quitit():
    wn.bye()

wn = turtle.Screen()
wn.setup(800,800)
t.speed(0)
t.hideturtle()

wn.onclick(draw)

wn.onkey(quitit, 'q')
wn.listen()

tkinter.mainloop()