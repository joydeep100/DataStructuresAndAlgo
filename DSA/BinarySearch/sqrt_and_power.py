'''
367. Valid Perfect Square

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l = 1
        r = num

        while l <= r:
            m = (l+r) // 2

            m_sq = m * m

            if m_sq == num:
                return True
            elif num < m_sq:
                r = m - 1
            else:
                l = m + 1

        return False
        

'''69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 
2 is returned.

same logic as previous but since nearest is expected, we need to keep a variable for inbound case.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0 # just in case x was 0, then sqrt of x will also be 0 right
        r = x # x// 2 fails

        res = 0

        while l <= r:
            
            m = (l+r) // 2
            m_sq = m * m

            if m_sq > x:
                r = m - 1
            elif m_sq > x:
                l = m + 1
                res = m
                # if m is not bigger then this might be nearest
            else:
                return m

        return res