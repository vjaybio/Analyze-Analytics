'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Chapter08: 6
'''
def main():
    s1 = input("Enter a string: ").strip()
    print("The number of letters in", s1, "is", countLetters(s1))
   
def countLetters(s1):
    count = 0
    for i in s1:
        if i.isalpha():
            count += 1
    return count

main()
