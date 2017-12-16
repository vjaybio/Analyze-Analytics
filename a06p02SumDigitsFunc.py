'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
'''
# main function
def main():
    integer = eval(input("Enter an integer between 0 and 1000:"))
    print ("The sum of the digits is ", sumDigits(integer))
# sumDigits function
def sumDigits(n):
    sum = 0
    while (n != 0): 
        remainder = n % 10 # last digit
        sum += remainder # sum
        n = n // 10 # remaining digits
    return sum
# Call Main
main()
