def strStr(haystack, needle):
    
    j = 0
    for i in range(len(haystack)):

        if haystack[i] == needle[j]:
            j += 1
        else:
            j = 0

        if j == len(needle):
            return True

    return False

print(strStr('oyesadbutsad', 'sad'))
print(strStr('sadbutsad', 'sad'))
print(strStr('sadzebutsad', 'sade'))
