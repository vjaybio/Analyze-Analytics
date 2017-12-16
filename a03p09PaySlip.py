'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 08th 2017
Description at the beginning of the program: Problem 3.09 from Python Book
'''
# prompt user to enter the details
name = eval(input("Enter name in quotes"))
hours = eval(input("Number of hours worked in a week:"))
hourlyrate = eval(input("hourly pay rate:"))
federaltax= eval(input("Federal tax withholding rate:"))
statetax = eval(input("State tax withholding rate :"))
print("Employee Name: ", name)
print("Hours worked:",hours)
print("Hourly Rate: $",hourlyrate)
grosspay = hours * hourlyrate 
print("Gross Pay: $", format(grosspay))
print("Deductions:")
ftax = grosspay * federaltax
stax = statetax * grosspay
print("\t Federal Tax (20.0%):  $", format(ftax, "0.2f"))
print("\t State Tax (9.0%):  $", format(stax, "0.2f"))
print("\t Total Tax deduction:  $", format(stax + ftax, "0.2f"))
print("Net Pay:$", grosspay - (stax + ftax))