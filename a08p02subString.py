'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Chapter08: 2
'''

def main():
    # get input strings and strip extra spaces
    s1 = input("first string: ").strip()
    s2 = input("second string: ").strip()
    #Check in IF condition and give result
    fs = findString(s1, s2) 
    #print(fs)
    if (fs == -1):
        print(s1, "is a substring of", s2)
    else:
        print(s1, "is not a substring of", s2)
# Check if the first string is a substring of the second string
def findString(s1, s2):
    fs = (s2.find(s1))
    if fs == 0:
        return -1

main()
