import turtle

turt = turtle.Turtle()
wn = turtle.Screen()

wn.setup(600,600)
turt.showturtle()
turt.speed(0)
turt.width(4)
_circle_size = 100
num_circles = int(wn.numinput('How many circles?', 'Enter amount to draw', 30, 2, 360))
_angle = 360 / num_circles

for i in range(num_circles):
    match i % 3:
        case 0:
            turt.pencolor('teal')
        case 1:
            turt.pencolor('red')
        case 2:
            turt.pencolor('pink')
    turt.circle(_circle_size)
    turt.left(_angle)

wn.exitonclick()