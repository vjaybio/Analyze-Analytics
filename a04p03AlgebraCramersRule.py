'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 4
Instructor: Aria Andrea
Date: September 15th 2017
'''

# Prompt user to enter values
a,b,c,d,e,f = eval(input("Enter a, b, c, d, e, f : "))
# Check determinant
check = (a * d)-( b * c) 
# If-else condition
if check == 0:
    print("The equation has no Solution")
else:
    print("x is", ((e * d)-(b * f))/check, "and y is", ((a * f)-(e * c))/check)

# 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
# 1, 2, 2, 4, 4, 5

'''
    x = ((e * d)-(b * f))/check
    y = ((a * f)-(e * c))/check 
    print("x is", x, "and y is", y)

a=1.0
b=2.0
c=3.0
d=4.0
e=5.0
f=6.0

det=a*d-b*c

if(det==0):
    print 'No sol'
else:
    print 'x is ',()/det
'''