"""3120. Count the Number of Special Characters I

You are given a string word. A letter is called special if it appears both in lowercase and uppercase 
in word.

Return the number of special letters in word.

Example 1:
    Input: word = "aaAbcBC"
    Output: 3
    Explanation:
    The special characters in word are 'a', 'b', and 'c'.

Example 2:
    Input: word = "abc"
    Output: 0
    Explanation:
    No character in word appears in uppercase.
"""
from collections import Counter

class Solution:
    def numberOfSpecialCharsBF(self, word: str) -> int:

        wordC = Counter(word)
        # using a set could have been considered, its better as well as counts is irrelavent here

        count = 0
        for ch in wordC:
            if ch.lower() in wordC and ch.upper() in wordC:
                count += 1
        
        return count // 2

    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        count = 0

        # Trick is here 
        # Iterate only through lowercase letters a-z
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)

            # If both are in the set, it's a special character
            if lower in chars and upper in chars:
                count += 1
        return count
 
        