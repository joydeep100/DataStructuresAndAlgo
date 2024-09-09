''' 58. Length of Last Word
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
'''
def lengthOfLastWordIB(s):
    # using inbuilt methods
    return len(s.split()[-1])

def lengthOfLastWord(s):
    # using logic
    i = len(s) - 1
    count = 0

    # find the first char (from the end)
    while i >= 0 and s[i] == " ":
        i -= 1

    # find the last char
    while i >= 0 and s[i] != " ":
        count += 1
        i -= 1

    return count

print(lengthOfLastWord('   fly me   to   the moon  '))
