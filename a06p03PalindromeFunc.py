'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
'''

def main():
    value = eval(input("Enter a positive integer: "))
    value1 = value    # storing it to compare later
    # compares return from function isPalindrome()
    if isPalindrome(value)== value1:
        if value == value1: 
            print("So", value, "is palindrome")
    else:
        print("So", value, "is not palindrome")

def isPalindrome(x):
    reverse = 0
    while x != 0:
        remainder = x % 10 # last digit
        #print("rem", remainder)
        reverse = reverse * 10 + remainder
        #print("rev is", reverse) # reverse numbers first digit
        x = x//10
        #print("x is:", x) # remaining digits
    print("Reverse of number is:", reverse)
    return reverse

main()
