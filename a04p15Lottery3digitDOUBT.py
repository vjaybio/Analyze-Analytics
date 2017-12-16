'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 4
Instructor: Aria Andrea
Date: September 15th 2017
'''
import random
# Generate a lottery number 99 for two digit, 999 for three digit
lottery = random.randint(100, 999)
# Prompt the user to enter a guess
print(lottery)
guess = eval(input("Enter your lottery pick (three digits): "))
# Get digits from lottery
lotteryDigit1 = lottery // 100
remainder1 = lottery - (lotteryDigit1 * 100)
print(remainder1)
lotteryDigit2 = remainder1 // 10
lotteryDigit3 = lottery % 10
print (lotteryDigit1, lotteryDigit2, lotteryDigit3)
# Get digits from guess
guessDigit1 = guess // 100
remainder2 = guess - (guessDigit1 * 100)
print(remainder2)
guessDigit2 = remainder2 // 10
guessDigit3 = guess % 10
print (guessDigit1, guessDigit2, guessDigit3)
print("The lottery number is", lottery)
# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit1 == lotteryDigit3 
      and guessDigit2 == lotteryDigit3 or guessDigit2 == lotteryDigit2 or guessDigit2 == lotteryDigit1 
      and guessDigit3 == lotteryDigit1 or guessDigit3 == lotteryDigit2 or guessDigit3 == lotteryDigit3):
    print("Matched all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1 
      or guessDigit1 == lotteryDigit2 
      or guessDigit1 == lotteryDigit3 
      or guessDigit2 == lotteryDigit1 
      or guessDigit2 == lotteryDigit2 
      or guessDigit2 == lotteryDigit3 
      or guessDigit3 == lotteryDigit1 
      or guessDigit3 == lotteryDigit2
      or guessDigit3 == lotteryDigit3) :
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")

'''
526
Enter your lottery pick (three digits): 562
26
5 2 6
62
5 6 2
The lottery number is 526
Match one digit: you win $1,000

'''