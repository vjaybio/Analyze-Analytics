#Name: Vijay Paul Singh Naik Zarapala, Class section: Section 3, Instructor: Aria Andrea
def main():
    number = eval(input("Enter credit card CC number: "))
    if isValid(number): 
        print("CC number", number, "is valid")
    else: 
        print("CC number", number, "is invalid")
def isValid(number):            # Return 1 or 0 - CC no is valid or not
    return getSize(number) >= 13 and getSize(number) <= 16 and \
        (prefixMatched(number, 4) or prefixMatched(number, 5) or \
         prefixMatched(number, 6) or prefixMatched(number, 37)) and \
         (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0
def sumOfDoubleEvenPlace(number): # called from isValid ()
    result = 0
    number = number // 10 # starts from 2nd digit from left
    while number != 0:
        result += getDigit((number % 10) * 2) #call getDigit()
        print(result)
        number = number // 100 # next even place
    return result                  #(sum)
def getDigit(number):       # Return single digit or sum of the two digits 
    return number % 10 + (number // 10)
def sumOfOddPlace(number):      # Return sum of odd place digits in number 
    result = 0
    while number != 0:
        result += number % 10
        number = number // 100  # Move to left by two positions
    return result
def prefixMatched(number, d):   # Return boolean TRUE if the prefix matches
    return getPrefix(number, getSize(d)) == d
def getSize(d): # Return the number of digits in d 
    numberOfDigits = 0    
    while d != 0:
        numberOfDigits += 1
        d = d // 10
    return numberOfDigits  
def getPrefix(number, k):       # Gives first digit or return number. 
    result = number
    for i in range(getSize(number) - k): result //= 10
    return result
main()

