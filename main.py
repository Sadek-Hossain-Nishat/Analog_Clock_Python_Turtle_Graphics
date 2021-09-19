import turtle
import time
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
c.color('green')
d.color('red')
b.color('blue')
c.pensize(7)
d.pensize(8)
b.pensize(6)
e=turtle.Turtle()
e.speed(30000000)
e.penup()
e.goto(0,-120)
e.pendown()
e.circle(120)
e.penup()
e.home()
e.pendown()
e.left(90)

a=30
e.hideturtle()
for i in range(1,13):
    e.right(a)
    e.penup()
    e.forward(100)
    e.write(i)
    e.goto(0,0)
    e.pendown()


b.speed(1000)
c.speed(1000)
d.speed(1000)
import time
while True:
    h=int(time.strftime('%H'))
    m=int(time.strftime('%M'))
    s=int(time.strftime(('%S')))
    c.home()
    c.left(90)
    c.right(0.1*60*m)
    c.forward(70)

    d.home()
    d.left(90)
    d.right(h*30+(m/60)*30)
    d.forward(45)

    b.home()
    b.left(90)
    b.right(s*6)
    b.forward(90)
    time.sleep(1)
    b.undo()
    c.undo()
    d.undo()

turtle.done()




