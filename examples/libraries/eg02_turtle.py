import turtle

turt = turtle.Turtle()
wn = turtle.Screen()

wn.setup(800, 800)
wn.bgcolor('ivory')

turt.showturtle()

turt.forward(150)
turt.setheading(90)
turt.forward(50)
turt.penup()
turt.goto(-100, 0)
turt.pendown()
turt.circle(100)
turt.penup
turt.goto(-200, 100)
turt.pendown
turt.dot()
turt.penup()
turt.goto(100, -200)
turt.pendown
turt.pencolor("red")
turt.fillcolor('yellow')
turt.begin_fill()
turt.forward(120)
turt.right(150)
turt.forward(100)
turt.end_fill()

wn.exitonclick()