'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Date: September 04th 2017
Description at the beginning of the program: Assignment: Problem 1.11 from textbook
1.11 (Population projection) The US Census Bureau projects population based on the
following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days. Hint: in Python, you
can use integer division operator // to perform division. The result is an integer. For
example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
'''

cp = 312032486                                              # cp is current population
seconds_in_year = 365 * 24 * 60 * 60                        # no. of seconds in one year
births_in_year = seconds_in_year // 7                       # no. of births in one year
#print(births_in_year)
deaths_in_year = seconds_in_year // 13                      # no. of deaths in one year
#print(deaths_in_year)
immigrants_in_year = seconds_in_year // 45                  # no. of immigrants in one year
#print(immigrants_in_year)
api = births_in_year + deaths_in_year - immigrants_in_year  # api is annual_population_increase 
#print (api)
print("Annual yearly population for the next 5 years is as below \n",
     "First Year is : ", cp + api, ", \n",
     "Second Year is : ", cp + 2 * api, ", \n",
     "Third Year is : ", cp + 3 * api, ", \n",
     "Fourth Year is : ", cp + 4 * api, "and \n",
     "Fifth Year is : ", cp + 5 * api, "\n")