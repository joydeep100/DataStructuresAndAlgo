class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        #  similar to https://leetcode.com/problems/power-of-four/description/

        """
        True if

            2^0, 2^1 ....
            1, 2, 4, 8, 16

            base case - when n == 0

            recursion case n / 2

            now core logic, can you see 16 is True but 20 will be False

            now for 20

            20 n % 2 == 0
            10 n % 2 == 0
            5 n % 2 != 0 <--

        """
        #  Using recursion
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n / 2)

s = Solution()
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(20))
