'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 4, Instructor: Aria Andrea
Date: September 15th 2017
'''
# user inputs
from math import floor
year1 = eval(input("Enter year:"))
month1 = eval(input("Enter month:"))
day1 = eval(input("day of the month:"))
# convert months 1 and 2 to previous years
if month1 == 1:
    m = 13
    year1 = year1 - 1
    print(year1)
elif month1 == 2:
    m = 14
    year1 = year1 - 1
    print(year1)
elif (month1 >= 3 and month1 <= 12): 
    m = month1
# calculate century of year 
j = round(year1 / 100)
k = year1 % 100
q = day1
# calculate h
h = (q + (26 * (m + 1) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7
print(h)
# convert it to lower limit of float (for a whole day)
h = floor(h)
print(h)
# calculate and print the day
toDay = 'day'
if h == 0:    toDay = 'Saturday'
elif h == 1:    toDay = 'Sunday'
elif h == 2:    toDay = 'Monday'
elif h == 3:    toDay = 'Tuesday'
elif h == 4:    toDay = 'Wednesday'
elif h == 5:    toDay = 'Thursday'
elif h == 6:    toDay = 'Friday'
print("Day of the week is", str(toDay))
