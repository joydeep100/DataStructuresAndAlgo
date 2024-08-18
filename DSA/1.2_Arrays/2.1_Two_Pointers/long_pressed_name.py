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

    i = 0
    k = 0

    while k < len(typed):
        if i < len(name) and name[i] == typed[k]:
            i += 1
            k += 1
        elif k > 0 and typed[k] == typed[k - 1]:
            k += 1
        else:
            return False

    return i == len(name)

def isLongPressedNameNW(name, typed):
    
    # My initial approach which did not work for all the tests
    curr_char_count = 1
    typing_char_count = 0

    i = 0
    k = 0
    
    while i < len(name) - 1 and k < len(typed):
        
        while i < len(name) - 1 and name[i] == name[i+1]:
            curr_char_count += 1
            i += 1

        while k < len(typed) and typed[k] == name[i]:
            typing_char_count += 1
            k += 1

        if typing_char_count < curr_char_count:
            return False
        
        curr_char_count = 1
        typing_char_count = 0

        i += 1

    return True

print(isLongPressedName("alex", "aaleex")) #True
print(isLongPressedName("saeed", "ssaaedd")) # False
print(isLongPressedName("leelee", "lleeelee")) # True
print(isLongPressedName("a", "b")) # False