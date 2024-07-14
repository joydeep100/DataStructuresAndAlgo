def validPalindrome(chars):

    l = len(chars)
    left = 0
    right = l - 1

    while(left < right):

        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1

    return True

print(validPalindrome('abba'))

# try using recusrsion

def validPalindromeR(chars):

    if len(chars) <= 0: return True
    if (chars[0] != chars[-1]): return False

    return validPalindromeR(chars[1:-2])

# print(validPalindromeR('abxba'))


