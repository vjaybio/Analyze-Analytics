'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 4
Instructor: Aria Andrea
Date: September 15th 2017
'''
dayNumber = eval(input("Enter today's day - Sunday as 0, Monday as 1 ... : "))
gapFutureNumber = eval(input("Enter the number of days elapsed since today:"))
#toDay Assignment
if dayNumber == 0:    toDay = 'Sunday'
elif dayNumber == 1:    toDay = 'Monday'
elif dayNumber == 2:    toDay = 'Tuesday'
elif dayNumber == 3:    toDay = 'Wednesday'
elif dayNumber == 4:    toDay = 'Thursday'
elif dayNumber == 5:    toDay = 'Friday'
elif dayNumber == 6:    toDay = 'Saturday'
#future Day Calculation
futureDayNumber = dayNumber + gapFutureNumber
if futureDayNumber > 6:
    futureDayNumber = futureDayNumber % 7
#future Day Assignment
if futureDayNumber == 0:
    futureDay = 'Sunday'
elif futureDayNumber == 1:
    futureDay = 'Monday'
elif futureDayNumber == 2:
    futureDay = 'Tuesday'
elif futureDayNumber == 3:
    futureDay = 'Wednesday'
elif futureDayNumber == 4:
    futureDay = 'Thursday'
elif futureDayNumber == 5:
    futureDay = 'Friday'
elif futureDayNumber == 6:
    futureDay = 'Saturday'
print("Today is", str(toDay), "and the future day is", str(futureDay))