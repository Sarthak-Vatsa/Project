import turtle
obj = turtle.Turtle()
wn = turtle.Screen()
# wn.bgcolor("lightsalmon")
wn.title("Nine Men Morris")
obj.speed(6)
#initial position
obj.up()
obj.goto(0,0)
# obj.begin_fill()
# obj.fillcolor("orange")
#making 3 nested boxes with dots
step =300
for i in range(0,3):
    obj.goto(-step,step)
    for j in range(0,4):
        obj.down()
        obj.dot()
        obj.forward(step)
        obj.dot()
        obj.forward(step)
        obj.right(90)
    obj.up()
    step = step-100
# obj.end_fill()

#further lines
step=100
obj.up()
obj.goto(0,0)
for i in range(0,4):
    obj.forward(step)
    obj.down()
    obj.forward(step*2)
    obj.up()
    obj.goto(0,0)
    obj.right(90)
obj.hideturtle()
#mandatory to see the python turtle graphics
turtle.done()
