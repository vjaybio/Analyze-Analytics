'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Problem 2.7 from Python Book
'''
minutes = eval(input("enter the number of minutes: "))
years = minutes / (24 * 60 * 365)
#print(years)
remyears = years % 1
#print(remyears)
days = remyears * 365
print (minutes, "minutes is approximately", int(years), "years and", int(days),"days") 
# sample 1000000000