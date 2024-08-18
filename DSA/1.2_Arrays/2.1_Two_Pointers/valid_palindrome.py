def validPalindrome(chars):

    l = len(chars)
    left = 0
    right = l - 1

    while (left <= right):

        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1

    return True


# print(validPalindrome('abba'))
# print(validPalindrome('abbac'))

# try using recursion


def validPalindromeR(chars):

    if len(chars) <= 0:
        return True
    if (chars[0] != chars[-1]):
        return False

    return validPalindromeR(chars[1:-1])

# print(validPalindromeR('abxba'))

# Slicing is not a very efficient approach, let try indexing

def validPalindromeRO(chars, i, j):
    if i >= j:
        return True
    if chars[i] != chars[j]:
        return False
    return validPalindromeRO(chars, i+1, j-1)

def validPalindromeRO_Wrapper(chars):
    if len(chars) <= 1: return True
    return validPalindromeRO(chars, 0, len(chars)-1)

print(validPalindromeRO_Wrapper('abxba'))
print(validPalindromeRO_Wrapper('abxcba'))
