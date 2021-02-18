# Write your program below:
import turtle
import math

shape = turtle.Turtle()

def drawFractalLine(level, distance):
    if level == 0:
        shape.pendown()
        shape.forward(distance)
    else: 
        drawFractalLine(level-1, distance/3)
        shape.left(60)
        drawFractalLine(level-1, distance/3) 
        shape.right(120)
        drawFractalLine(level-1, distance/3) 
        shape.left(60)
        drawFractalLine(level-1, distance/3)
        
for i in range(6):
    drawFractalLine(3, 55)       
    shape.left(60)
