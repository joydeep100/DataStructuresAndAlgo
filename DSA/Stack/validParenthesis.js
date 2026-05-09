/* 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()" // we can solve these using hashmap by Example 2 we cannot solve using hashmap
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false */

var isValid = function (s) {

    let stack = []

    // stack = [ '(' , '[' ]

    let bracketMap = { ")": "(", "}": "{", "]": "[" }

    for (let char of s) {

        if (!(char in bracketMap)) {
            stack.push(char)
        } else if (stack.length && stack.slice(-1)[0] === bracketMap[char]) {
            // stack.slice(-1) on an array would give us the o/p like [5]
            stack.pop()
        } else {
            return false
        }

    }

    return stack.length ? false : true

};

console.log(isValid("([]){"))


