'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea

(Compute the greatest common divisor) For Listing 5.8, 
another solution to find
the greatest common divisor of two integers n1 and n2 is as follows: 
First find d to be the minimum of n1 and n2, 
and then check whether d, d - 1, d - 2, ..., 2, or 1 is a divisor 
for both n1 and n2 in this order. 
The first such common divisor is the
greatest common divisor for n1 and n2.

'''
#Prompt the user to enter two integers
n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))
d = min (n1, n2)
# check if d can divide both n1 and n2 and it goes on down till 1
while d >= 1: 
    if n1 % d == 0 and n2 % d == 0:
        #gcd = d
        break
    d -= 1
print("The GCD for", n1, "and", n2, "is", d)
