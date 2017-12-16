'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 2.21 from Python Book
'''
# prompt user to enter the monthly saving amount
p = eval(input("Enter the monthly saving amount: "))        # p= principal  
r = 0.05                                                    # r = annual_interest_rate = 5% = 0.05
n = 12                                                       # n = 12 as its annual = 12 months
mir = r/n 
#print (mir)
fmValue = p * (1 + mir)
#print (int(fmValue * 1000) / 1000.0)
smValue = (p + fmValue) * (1 + mir)
#print (int(smValue * 1000) / 1000.0)
tmValue = (p + smValue) * (1 + mir)
#print (int(tmValue * 1000) / 1000.0)
fmValue = (p + tmValue) * (1 + mir)
#print (int(fmValue * 1000) / 1000.0)
fimValue = (p + fmValue) * (1 + mir)
#print (int(fimValue * 1000) / 1000.0)
simValue = (p + fimValue) * (1 + mir)
print ("After the sixth month, the account value is", int(simValue * 100) / 100.0)
#sample 100

#t = 0.5                                                         # t = time (years) = 1
#CI = p * ( 1 + ( r / n )) ** ( n * t ) 