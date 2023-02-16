import turtle
t = turtle.Pen()
t.shape('turtle')
for i in range(3):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)

t.penup()
t.goto(0.0)
t.right(90)
t.pendown()
for i in range(3):
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    
t.right(180)
for i in range(6):
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)