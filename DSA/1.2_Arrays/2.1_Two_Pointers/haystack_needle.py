def strStr(haystack, needle):

    # Find index of first occurance of substring in string

    j = 0
    count = 0
    for i in range(len(haystack) - len(needle)):

        if haystack[i] == needle[j]:
            count += 1
            j += 1
        else:
            j = 0

        # now we also want to return the starting index where we find the match

        if j == len(needle):
            return True

    return False

print(strStr('oyesadbutsad', 'sad'))
print(strStr('sadbutsad', 'sad'))
print(strStr('sadzebutsad', 'sade'))
