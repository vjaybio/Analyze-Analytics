'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 08th 2017
Description at the beginning of the program: Problem 2.25 from Python Book
'''
# import math module to use the math functions
from math import *
x1, y1 = 33.74, -84.38 # atlanta
x2, y2 = 28.53, -81.37 # orlando
x3, y3 = 32.08, -81.09 # savannah
x4, y4 = 35.22, -80.84 # charlotte
radius = 6371.01
d1 = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2)) #a-o
d2 = radius * acos(sin(x2) * sin(x3) + cos(x2) * cos(x3) * cos(y2 - y3)) #o-s
d3 = radius * acos(sin(x3) * sin(x4) + cos(x3) * cos(x4) * cos(y3 - y4)) #s-c
d4 = radius * acos(sin(x4) * sin(x1) + cos(x4) * cos(x1) * cos(y4 - y1)) #c-a
d5 = radius * acos(sin(x1) * sin(x3) + cos(x1) * cos(x3) * cos(y1 - y3)) #a-s diagonal distance
#print( d1,"\n",d2,"\n",d3,"\n",d4,"\n",d5)
#area of Atlanta, Orlando, Savannah triangle 
aos = (d1 + d2 + d5) / 2
areaaos = (aos * (aos - d1) * (aos - d2) * (aos - d5)) ** 0.5
#area of Atlanta, Savannah, Charlotte triangle 
acs = (d3 + d4 + d5) / 2
areaacs = (acs * (acs - d3) * (acs - d4) * (acs - d5)) ** 0.5
#Total Area between Atlanta, Orlando, Savannah, Charlotte
Areaaosc = (areaaos+areaacs)
print ("the estimated area enclosed by these four cities Atlanta, Orlando, Savannah, Charlotte is", (int(Areaaosc * 100) / 100.0))