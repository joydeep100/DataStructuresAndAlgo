def rec(n):
    
    # base case
    if n == 0: return # or exit(0)

    print("Hello")

    # recursive case
    rec(n-1)

# rec(5)

# factorial
def fact(n):
    if n <= 0: return 1

    return n * fact(n-1)

print(fact(5))
