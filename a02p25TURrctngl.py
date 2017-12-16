'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 2.25 from Python Book
'''
#import turtle module
import turtle
# Take user-inputs
x, y, w, h= eval(input("Enter the center coordinates as x, y for the rectangle of width w, and height h: "))
# set cursor to center
turtle.showturtle()

turtle.penup()
turtle.goto(x, y) # Moves cursor to center of rectangle
#turtle.write("c")
turtle.forward (w/2)
#turtle.write("h")
turtle.pendown()

turtle.right(90)
turtle.forward(h/2)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)
turtle.hideturtle()
turtle.done()

