''' 925. Long Pressed Name
Your friend is typing his name into a keyboard. Sometimes, 
when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. 
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
'''
def isLongPressedName(name, typed):

    i = 0 # pointer for name
    k = 0 # pointer for typed

    while k < len(typed):
        # if both are same its great
        if i < len(name) and name[i] == typed[k]:
            i += 1
            k += 1
        # if current in typed is same as prev its fine
        elif k > 0 and typed[k] == typed[k - 1]:
            k += 1
        else:
            return False

    return i == len(name)

print(isLongPressedName("alex", "aaleex")) #True
print(isLongPressedName("saeed", "ssaaedd")) # False
print(isLongPressedName("leelee", "lleeelee")) # True
print(isLongPressedName("a", "b")) # False