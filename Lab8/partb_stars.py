import turtle as t


star = t.Turtle()
wn = t.Screen()

pointsinput = int(wn.numinput("How Many?", "Enter the amount of points you'd like", 30, 2, 360))

points = list(range(1, pointsinput+1))

angle = 180 - (180/pointsinput)

wn.setup(800, 800)
star.speed(10)
star.hideturtle()

def drawStar():
    star.penup()
    star.goto(-200, 0)
    star.fillcolor("yellow")
    star.pencolor("orange")
    star.pendown()
    star.begin_fill()
    for _ in points:
        star.forward(400)
        star.right(angle)
    star.end_fill()

    

drawStar()

t.exitonclick()

