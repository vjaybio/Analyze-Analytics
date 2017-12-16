'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
'''
import random

def main():
    num = eval(input("Enter n: "))
    printMatrix(num) # calls function printMatrix

def printMatrix(n):
    for i in range(1, n + 1):       # repeats loop by n times
        for j in range(1, n + 1):   # prints n times horizontally
            print(random.randint(0, 1), end = " ")
        print()                     # next line
        
main()