'''Smallest prime divisor of a number

Input: 25 
Output: 5

Input: 31 
Output: 31 
'''

def smallestDivisor(n):

    # if divisible by 2
    if (n % 2 == 0):
        return 2

    # iterate from 3 to sqrt(n), 
    # as per property of prime numbers its divisor can go only upto sqrt(n)
    i = 3
    while (i ** 2 <= n):
        if (n % i == 0):
            return i
        
    # even-numbers other than 2 cannot be the smallest divisor
    i += 2

    # If no divisors are found in the previous steps, the function returns n itself. 
    return n

print(smallestDivisor(31))