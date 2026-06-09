def isSubsequence(s, t):

    if not s:
        return True
        
    l = len(s)
    i = 0

    for ch in t:
        if ch == s[i]:
            i += 1

        # the moment you get solution return
        if i == l:
            return True

    return i == l


print(isSubsequence('abc', 'ahbgdc')); # true
print(isSubsequence('sing', 'sting')); # true
print(isSubsequence('abc', 'abracadabra')); # true
print(isSubsequence('abc', 'acb')); # false (order matters)