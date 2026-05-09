class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)

        l, r = 0, n - 1
        delete_char = 0
        while l <= r:
            print(l, r, s[l], s[r], delete_char)
            if s[l] != s[r]:
                delete_char += 1
                l += 1
            else:
                l += 1
                r -= 1

        return True if delete_char <= 1 else False


    # def validPalindrome(self, s: str) -> bool:
    #
    #     n = len(s)
    #
    #     mid = n//2
    #
    #     if n % 2 == 0:
    #         l_mid, r_mid = mid -1, mid
    #     else:
    #         l_mid = r_mid = mid
    #
    #     invalid_count = 0
    #     while l_mid >= 0 and r_mid < n:
    #         print(l_mid, r_mid, s[l_mid] != s[r_mid], invalid_count)
    #         if s[l_mid] != s[r_mid]:
    #             invalid_count += 1
    #         l_mid -= 1
    #         r_mid += 1
    #     print(invalid_count)
    #     return True if invalid_count <= 1 else False

sol = Solution()
print(sol.validPalindrome("aba")) # true
# print(sol.validPalindrome("abc")) # false
