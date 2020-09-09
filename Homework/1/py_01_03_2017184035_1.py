import turtle

def MoveTo(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def PrintOh():
    turtle.setheading(270)
    turtle.forward(30)
    MoveTo(turtle.xcor()-50,turtle.ycor())
    turtle.setheading(0)
    turtle.forward(100)

def PrintU():
    turtle.setheading(0)
    turtle.forward(100)
    MoveTo(turtle.xcor()-50,turtle.ycor())
    turtle.setheading(270)
    turtle.forward(30)

def PrintI(long):
    turtle.setheading(270)
    if(long == True):
        turtle.forward(200)
    else:
        turtle.forward(100)

def PrintYeo():
    turtle.setheading(0)
    turtle.forward(30)
    MoveTo(turtle.xcor()-30,turtle.ycor()-20)
    turtle.forward(30)
    MoveTo(turtle.xcor(),turtle.ycor()+90)
    turtle.setheading(270)
    turtle.forward(150)

def PrintGiyeok():
    turtle.setheading(0)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)

def PrintNieun():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    
def PrintJieut():
    turtle.setheading(0)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(144)
    MoveTo(turtle.xcor()+50, turtle.ycor()+50)
    turtle.left(90)
    turtle.forward(72)

def PrintChieut():
    turtle.setheading(270)
    turtle.forward(30)
    MoveTo(turtle.xcor()-50,turtle.ycor())
    PrintJieut()


def PrintHieut():
    PrintOh()
    MoveTo(turtle.xcor()-50, turtle.ycor()-20)
    turtle.setheading(180)
    turtle.circle(40)

turtle.speed(0)
MoveTo(-250,230)
PrintChieut()
MoveTo(-250,80)
PrintOh()
MoveTo(-150,230)
PrintI(True)
MoveTo(-100,200)
PrintJieut()
MoveTo(-100,80)
PrintU()
MoveTo(-100,50)
PrintNieun()
MoveTo(100,230)
PrintHieut()
MoveTo(170,160)
PrintYeo()
MoveTo(100,50)
PrintGiyeok()
turtle.exitonclick()
