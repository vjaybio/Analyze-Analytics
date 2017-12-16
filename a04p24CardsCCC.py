'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 4
Instructor: Aria Andrea
Date: September 15th 2017
'''    
import random
NUMBER_OF_CARDS = 52
# Pick a card- limits are 0 and 51 
number = random.randint(0, NUMBER_OF_CARDS - 1)

print("The card you picked is", end = " ")
if number % 13 == 0:
    print("Ace of ", end = "")
elif number % 13 == 10:
    print("Jack of ", end = "")
elif number % 13 == 11:
    print("Queen of ", end = "")
elif number % 13 == 12:
    print("King of ", end = "")
else:
    print(number % 13, "of ", end = "")

if number // 13 == 0:
    print("Clubs")
elif number // 13 == 1:
    print("Diamonds")
elif number // 13 == 2:
    print("Hearts")
elif number // 13 == 3:
    print("Spades")
