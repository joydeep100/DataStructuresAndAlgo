num = 12345

def get_digits(n):
    # return [int(digit) for digit in str(number)]
    res = []
    while n > 0:
        res.append(n%10)
        n //= 10

    return res[::-1]

print(get_digits(num)) # [1, 2, 3, 4, 5]

def get_prefizes(n):
    # Ex. for 123 --> 1, 12, 123
    res = []
    while n > 0:
        res.append(n)
        n //= 10
    return res

print(get_prefizes(num)) # [12345, 1234, 123, 12, 1]

def get_length(n):
    n = abs(n) # need to handle negative numbers
    count = 0
    while n > 0:
        count += 1
        n//= 10

    return count

print(get_length(num))
print(get_length(10))
print(get_length(123))
