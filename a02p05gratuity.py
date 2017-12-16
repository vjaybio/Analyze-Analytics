'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 2.5 from Python Book
'''
# Prompt user for inputting values for subtotal and gratuity
subtotal, gratuityrate = eval(input("Enter subtotal and gratuityrate seperated by a comma: "))
gratuity = subtotal * gratuityrate / 100
total = subtotal + gratuity  
print ("The gratuity is",  int(gratuity * 100) / 100.0, "and the total is", int(total * 100) / 100.0)
#sample values : 15.69, 15