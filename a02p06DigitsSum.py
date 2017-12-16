'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 2.6 from Python Book
'''
integer = eval(input("Enter an integer between 0 and 1000:"))
d1 = integer % 10
#print (d1)
r1 = integer // 10
d2 = r1 % 10
#print (d2)
r2 = r1 // 10
d3 = r2 % 10
#print (d3)
r3 = r2 // 10
d4 = r3 % 10
#print (d4)
total = d1+d2+d3+d4
print ("The sum of the digits is ", total)
# Sample value 999