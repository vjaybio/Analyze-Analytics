'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea

# Prompt the user to enter the number of students
numOfStudents = eval(input("Enter the number of students: "))

score1 = eval(input("Enter a student score: "))
score2 = eval(input("Enter a student score: "))

mx = max(score1, score2)
mn = min(score1, score2)

score1 = mx
score2 = mn

for i in range(numOfStudents - 2):
    t = eval(input("Enter a student score: "))
    mx=max(score1,t)
    mn=max(score2,t)
    score1=mx
    score2=mn

print("Top student " + "'s score is " + str(score1))
print("2nd Top student " + "'s score is " + str(score2))
'''

# Prompt the user to enter the number of students
numOfStudents = eval(input("Enter the number of students: "))
score1 = eval(input("Enter a student score: "))
score2 = eval(input("Enter a student score: "))
# calculate max and min
mx = max(score1, score2)
mn = min(score1, score2)
# assign max and min to score 1 and 2
score1 = mx
score2 = mn
# compare with 3rd value
for i in range(numOfStudents - 2):
    cscore = eval(input("Enter a student score: "))
    mx = max(score1, score2, cscore)
#calculate 2nd max
    if mx == score1:
        mn = max(score2, cscore)
    if mx == score2: 
        mn = max(score1, cscore)
    if mx == cscore:
        mn = max(score1, score2)
    score1 = mx
    score2 = mn
    print(mx,mn)
print("Top student " + "'s score is " + str(score1))
print("2nd Top student " + "'s score is " + str(score2))

