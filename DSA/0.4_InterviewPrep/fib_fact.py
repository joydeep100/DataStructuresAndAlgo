# Fibonacci series 0, 1, 1, 2, 3, 5, 8...
# basic approach
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# using memoization
def fibDp(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibDp(n-1, computed) + fibDp(n-2, computed)

    return computed[n]

print(fibDp(5))

# factorial 5! = 5*4*3*2*1 ; 0! = 1 , 1! = 1

def fact(n):
    if (n <= 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # 120

def factorialDp(n, computed={}):

    if n <= 1:
        return 1
    
    if n not in computed:
        computed[n] = n * factorialDp(n - 1, computed)
    
    return computed[n]

print(factorialDp(5))

# fact iterative
def fact(n):
    if (n == 0 or n == 1):
        return 1
    
    res = 1
    # since last index is 0 we go upto 0, which is only till first index
    for i in range(n, 0, -1):
        res = res * i
    return res
