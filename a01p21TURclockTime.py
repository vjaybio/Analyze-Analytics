'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 1.18 from Python Book
'''
#import turtle module
import turtle
#drawing circle at the center of screen
turtle.showturtle()
turtle.color("red")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)
#Write time as 9:15:00 - we are hard-coding it as the time function is unavailable
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.write("9:15:00")
turtle.left(180)
turtle.forward(20)
#writing number 6 and 12
turtle.color("blue")
turtle.write(6)
turtle.penup()
turtle.forward(186)
turtle.write(12)
#drawing Minutes Dial
turtle.color("Green")
turtle.right(180)
turtle.pendown()
turtle.forward(86)
turtle.right(90)
#drawing hours dial and write 9
turtle.color("blue")
turtle.forward (66)
turtle.penup()
turtle.forward (30)
turtle.pendown()
turtle.write(9)
#drawing seconds dial and write 15
turtle.color("brown")
turtle.right(180)
turtle.penup()
turtle.forward (96)
turtle.pendown()
turtle.forward (70)
turtle.penup()
turtle.forward (15)
turtle.pendown()
turtle.write(15)
#hide cursor
turtle.hideturtle()
turtle.done()
