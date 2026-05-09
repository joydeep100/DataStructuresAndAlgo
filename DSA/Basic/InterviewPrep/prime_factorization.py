# https://www.youtube.com/watch?v=5gFC-ayyQMk

def primeFactorization(n):

    res = []

    divisor = 2
    while divisor ** 2 <= n: 
        while(n % divisor == 0):
            res.append(divisor)
            n = n // divisor
        divisor += 1
    
    # At last if n is not == 1, then that number is also a factor of n
    if n != 1:
        res.append(n)
    
    return res

# Find all prime factors
print(primeFactorization(120)) # [2, 2, 2, 3, 5]
print(primeFactorization(545341149)) # [3, 3, 60593461]