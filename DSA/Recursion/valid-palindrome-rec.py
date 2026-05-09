""" 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initial call to the recursive helper
        return self.check_palindrome(s, 0, len(s) - 1)

    def check_palindrome(self, s: str, left: int, right: int) -> bool:
        # Base Case: If pointers cross, we've checked everything
        if left >= right:
            return True

        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            return self.check_palindrome(s, left + 1, right)

        # Skip non-alphanumeric characters from the right
        if not s[right].isalnum():
            return self.check_palindrome(s, left, right - 1)

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        # Recursive step: Move both pointers inward
        return self.check_palindrome(s, left + 1, right - 1)
    
    # 2 pointer approach

    def isPalindrome2p(self, s: str) -> bool:
    
        left, right = 0 , len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1


        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome2p("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome2p("race a car"))   
print(s.isPalindrome(" "))
