''' 205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the 
order of characters. 
** No two characters may map to the same character **
but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false
'''
def isIsomorphic(s, t):

    if len(s) != len(t):
        return False

    map = {}
    uniq_t_vals = set()

    for i in range(len(s)):
        if s[i] not in map:
            map[s[i]] = t[i] # because of the order
            
            # To handle this condition - No two characters may map to the same character
            if t[i] in uniq_t_vals:
                return False
            else:
                uniq_t_vals.add(t[i])

    res = ''
    for ch in s:
        res += map[ch]

    return res == t

print(isIsomorphic('egg', 'foo'))