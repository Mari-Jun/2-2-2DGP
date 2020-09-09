import turtle

def MoveTo(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def DrawLineRecur(row, count):
    if(count<0):
        return
    
    if(row==True):
        turtle.setheading(90)
    else:
        turtle.setheading(0)

    turtle.forward(500)

    if(row==True):
        MoveTo(turtle.xcor()+100,turtle.ycor()-500)
    else:
        MoveTo(turtle.xcor()-500,turtle.ycor()+100)

    DrawLineRecur(row,count-1)


def DrawRowLine(x,y):
    turtle.setheading(90)
    for count in range(0,6):
        MoveTo(x+count*100,y)
        turtle.forward(500)

def DrawColumnLine(x,y):
    turtle.setheading(0)
    for count in range(0,6):
        MoveTo(x,y+count*100)
        turtle.forward(500)

    
turtle.speed(0)
DrawRowLine(0,0)
DrawColumnLine(0,0)
turtle.exitonclick()
