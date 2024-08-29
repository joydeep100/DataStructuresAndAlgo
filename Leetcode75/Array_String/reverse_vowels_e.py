from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        # since str in immutable, converting it into a list
        s = list(s)

        while left < right:

            if s[left] not in vowels:
                left += 1
                
            if s[right] not in vowels:
                right -= 1

            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # converting back to str
        return "".join(s)

print(Solution().reverseVowels('hello')) # holle

