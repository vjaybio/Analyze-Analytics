'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 2.14 from Python Book
'''
# prompt user to enter the three coordinates
x1, y1, x2, y2, x3, y3 = eval(input("Enter x1, y1, x2, y2, x3, y3 coordinates of a triangle: "))
# compute the sides 
side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 
side2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
# print (side1, side2 , side3)
s = (side1 + side2 + side3) / 2
# print(s)
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print (int(area * 100) / 100.0)
#sample:  1.5, -3.4, 4.6, 5, 9.5, -3.4