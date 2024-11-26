import turtle as t


star = t.Turtle()
wn = t.Screen()




wn.setup(800, 800)
star.speed(10)
star.hideturtle()

pointsinput = int(wn.numinput("How Many?", "Enter the amount of points you'd like as an odd number", 5, 3, 101))


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
    
        
while pointsinput % 2 == 0:
    pointsinput = 0
    pointsinput = int(wn.numinput("How Many?", "Enter the amount of points you'd like as an odd number", 5, 2, 101))
points = list(range(1, pointsinput+1))
angle = 180 - (180/pointsinput)
drawStar()
t.exitonclick()



