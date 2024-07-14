from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        s = list(s)

        while left < right:

            while s[left] not in vowels and left < right:  # mistake, did not add (left < righ)t here
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)

print(Solution().reverseVowels('hello')) # holle

