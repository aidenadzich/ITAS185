import turtle as t

house = t.Turtle()
wn = t.Screen()

house.penup()
house.hideturtle()

def triangle(size, colour):
    house.pendown()
    house.fillcolor(colour)
    house.begin_fill()
    for _ in range(3):
        house.forward(size)
        house.left(120)
    house.end_fill()
    house.penup()

def square(size, colour):
    house.pendown()
    house.fillcolor(colour)
    house.begin_fill()
    for _ in range(4):
        house.forward(size)
        house.right(90)
    house.end_fill()
    house.penup()

def rectangle(width, height, colour):
    house.pendown()
    house.fillcolor(colour)
    house.begin_fill()
    for _ in range(2):
        house.forward(width)
        house.right(90)
        house.forward(height)
        house.right(90)
    house.end_fill()
    house.penup()

def circle(radius, colour):
    house.pendown()
    house.fillcolor(colour)
    house.begin_fill()
    house.circle(radius)
    house.end_fill()
    house.penup()

def draw_house():
    house.goto(-100, 75)
    rectangle(200, 150, "darkorchid4")

    house.goto(-110, 75)
    triangle(220, "lightblue")

    house.goto(60, -35)
    rectangle(20, 40, "red")
    house.goto(65, -55)
    circle(1, "black")
    
    house.goto(-80, 0)
    square(10, "darkgray")
    house.goto(-70, 0)
    square(10, "darkgray")
    house.goto(-80, -10)
    square(10, "darkgray")
    house.goto(-70, -10)
    square(10, "darkgray")

    house.goto(-200, 25)
    rectangle(20, 100, "brown")
    house.goto(-190, 25)
    circle(50, "green")



draw_house()

t.exitonclick()