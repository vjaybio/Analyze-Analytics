'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
'''
import time

class Time:
    def __init__(self):
        self.setTime(int(time.time()))

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second
    
    def setTime(self, elapsedTime): 
        self.__second = elapsedTime % 60            # Get the current second 
        
        totalMinutes = elapsedTime // 60            # Obtain the total minutes
        
        self.__minute = totalMinutes % 60           # Current minute in the hour
        
        totalHours = totalMinutes // 60             # Obtain the total hours

        self.__hour = totalHours % 24               # Compute the current hour
    
def main():
    currentTime = Time()
    print("Current time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))

    elapseTime = eval(input("Enter the elapse time  in seconds: "))
    currentTime.setTime(elapseTime)
    print("The hour:minute:second for elapse time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))

main()
