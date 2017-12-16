'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 5
Instructor: Aria Andrea
Date: September 18th 2017
'''
'''
tution = 10000
annualIncrease = 0.05
year = 1
print(format("Year", "<10s"), format("Tution", "<10s"))
print("--------------------")
#i=0
for i in range(10): 
    tution = tution + (tution * 0.05)
    print(format(year, "<10d"), format(tution, "<10.2f"))
    year = year +1 
    i = i+1
#cost of 4years tution after 10years
#print(tution)
tutionfy= tution
for j in range(3):
    tutionfy = tutionfy + (tutionfy * 0.05)
    #print(tutionfy)
    tution = tution + tutionfy
 #   print(tutionfy)    

print("fourYearsTution: ", format(tution, "<10.2f" ))
'''
tution = 10000
year = 1
while year <=11:
    print("year", year, format(tution, "<10.2f"))
    tution = tution + (tution * 0.05)
    year += 1
    itution = tution
    while (year >= 11) and (year <14):
        tution = tution + (tution * 0.05)
        itution = tution + itution
        year += 1
print("Four Year Tution is :", format(itution, "<10.2f"))

    
        
    