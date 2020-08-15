import math
import turtle


fred = turtle.Turtle()
sc = turtle.Screen()
sc.reset()
sc.setworldcoordinates(0,-1.5,360,1.5)
fred.color("white")

turtle.bgcolor("black")
bob = turtle.Turtle()
bob.color("white")

duda = turtle.Turtle()
luly = turtle.Turtle()
luly.color("white")
duda.color("white")

for angle in range(1000):
    yf = math.sin(math.radians(angle))
    yb = math.cos(math.radians(angle))
    fred.goto(angle,yf)   
    bob.goto(angle,yb)
    duda.goto(angle,-yf)
    luly.goto(angle,-yb)
wn.exitonclick()