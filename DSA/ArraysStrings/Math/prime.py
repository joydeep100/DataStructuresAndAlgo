"""
A prime number has only two factors, 1 and itself.

A composite number which has three factors, 1 , 2 and itself.

1 is neither prime nor composite.

prime numbers = 2,3,5,7,11,13.....
"""

def prime_basic(n):

    if n == 0 or n == 1: return False

    for i in range(2, n):
        # since for prime number there is no divisor between 2 and n-1
        # as you know range(2,n) will go only from 2 to n-1
        if n % i == 0:
            return False

    return True

print(prime_basic(8))

"""
Now lets optimize it, take any number say 36

1 * 36
2 * 18
3 * 12
4 * 9
6 * 6 or square root of 36

[1 2 3 4 6 | 6 9 12 18 36]

so idea is if a number is not prime then from 2 to sqrt(n) there would be a number which is a divisor of n
so we can go just loop until sqrt(n) instead of n-1
"""
import math
def prime_opt(n):

    if n == 0 or n == 1: return False

    sqrt_n = int(math.sqrt(n))

    # mistake should be sqrt_n + 1 else it would end in sqrt_n - 1 right
    # ex: 8 would fail... since in range(2,2) would go only until 1
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False

    return True

print(prime_opt(8))

"""
Now again if 
"""