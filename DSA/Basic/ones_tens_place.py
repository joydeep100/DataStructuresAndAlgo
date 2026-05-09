def find_digits(number):

    digits = []
    while (number > 0):
        digits.append(number % 10)
        number = number // 10
    return digits[::-1]


print(find_digits(123))  # [1, 2, 3]


def find_digits_str(number):
    return [int(digit) for digit in str(number)]

    ''' if we need sum, sum(int(digit) for digit in str(number))
    we can also use [] instead of ()
    ''' 

print(find_digits_str(123))  # [1, 2, 3]
