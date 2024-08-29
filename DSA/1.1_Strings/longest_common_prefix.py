''' 14. Longest Common Prefix
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    # O(n) Best case
    
    res = ''
    for i in range(len(strs[0])):
        # loop through the first list item

        for str in strs:
            # if i is the end of the current list item or if it does not match the return
            # so instead of looping till the boundary condition we can check when it crosses the boundary
            if i == len(str) or str[i] != strs[0][i]:
                return res
            
        res += strs[0][i]

    return res

print(longestCommonPrefix(["flower","flow","flight"]))