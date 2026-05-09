''' 20. Valid Parentheses
Example 1
Input: s = "()" // we can solve these using hashmap by Example 2 we cannot solve using hashmap
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false */
'''

def isValid(str):

    stack = []

    parenMap = { ")": "(", "]": "[", "}": "{"}

    for ch in str:
        if ch not in parenMap:
            stack.append(ch)
        elif stack and stack[-1] == parenMap[ch]:
            stack.pop()
        else:
            return False
        
    return True if not stack else False

print(isValid("([]){"))
print(isValid("{([])}"))


