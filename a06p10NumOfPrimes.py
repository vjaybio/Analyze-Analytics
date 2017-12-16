'''
Name: Vijay Paul Singh Naik Zarapala
Class section: Section 3
Instructor: Aria Andrea
'''
def main():
    count = 0
    # starts from 2 
    for number in range(2, 10000):
        # Checks in prime function and returns count if prime
        if isPrime(number):
            count += 1
    print("The number of prime number <", 10000, "is", count)

# Check whether number is prime and returns boolean 1 or 0
def isPrime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime
    return True # number is prime

main()
