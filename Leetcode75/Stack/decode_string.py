''' 
Example 1:
Input: str = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: str = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: str = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''

def decodeString(str):
    stack = []

    for ch in str:
        if ch != "]":
            stack.append(ch)
        else:
            ch = ""
            while stack and stack[-1] != "[":
                ch = stack.pop() + ch # prefix add

            # at-least one bracket will be there for sure, rigth
            # so no need to check if stack is not empty

            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            if k:
                stack.append(int(k) * ch)
            else:
                stack.append(ch)

    return "".join(stack)

print(decodeString('3[a][bc]'))