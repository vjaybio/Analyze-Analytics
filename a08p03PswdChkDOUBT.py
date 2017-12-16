'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
Chapter08: 3
'''
def main():
    # get input strings and strip extra spaces
    pswd = input("Password String: ").strip()
    #Check in IF condition and give result
    #print(pswd.isalnum())
    cp = checkPswd(pswd) 
    if (cp == -1):
        print(pswd, "is valid Password")
    else:
        print(pswd, "is invalid Password") 
# Check if the first string is a substring of the second string
def checkPswd(pswd):
    count = 0
    #check alnum
    if pswd.isalnum():
        #check length == 8
        if len(pswd) == 8:
            #check number of digits = 2 or not
            for i in range (0, len(pswd), 1):
                if pswd[i].isdigit():
                    count = count + 1
                    if count == 2:
                        print (9)
                        return -1
                    else:
                        print(0)
        else:
            return 0
    return -1

main()
