'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Chapter10: 2
'''

def main():
    # Ask user to input, extract items from the string
    string = input("enter numbers separated by space").split()
    # convert string items to number
    numbers = [ eval(x) for x in string ]
    # First we need to Reverse the list
    numbers.reverse()
    # only after reverse, we can print the reversed list
    print(numbers)
    
main()
