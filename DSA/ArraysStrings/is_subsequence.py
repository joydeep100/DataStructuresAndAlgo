def isSubsequence(needle, haystack):

    j = 0
    count = 0

    for i in range(len(haystack)):

        if haystack[i] == needle[j]:
            j += 1
            count += 1

        if count == len(needle): return True

    return False


print(isSubsequence('abc', 'ahbgdc')); # true
print(isSubsequence('sing', 'sting')); # true
print(isSubsequence('abc', 'abracadabra')); # true
print(isSubsequence('abc', 'acb')); # false (order matters)