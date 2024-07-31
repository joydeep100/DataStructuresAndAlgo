'''238 Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0] '''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # populate prefix array
        mul = 1
        pref = [0] * n
        for i in range(len(nums)):
            mul *= nums[i]
            pref[i] = mul

        # populate postfix array
        mul = 1
        suff = [0] * n
        for i in range(len(nums) - 1, -1, -1):
            mul *= nums[i]
            suff[i] = mul

        res = [0] * n
        # so the res, would be lets take for first index value = 1, it would be
        ''' nums = [1, 2, 3, 4]
            pref = [1, 2, 6, 24]
            suff = [24, 24, 12, 4]
        lets consider index 0 = 1, its res should be rhs of suff
        and for index 1 = 2, its res should be lhs of pref (1) * rhs of suff (12) = 12
        '''
        for i in range(len(nums)):
            left, right = 1, 1
            if (i > 0 and i < len(nums)):
                left = pref[i-1]
            if (i >= 0 and i < len(nums) - 1):
                right = suff[i+1]
            res[i] = left*right
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1
        suff[n-1] = 1

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        ''' nums = [1, 2, 3, 4]
            pref = [1, 1, 2, 6] 
            suff = [24, 12, 4, 1]

            lets consider index 0 = 1, it does not have any left value so its prefix value is 1
            lets consider index 1 = 2, its prefix value is 1
            lets consider index 2 = 3, its prefix value is 2

            and for suff, we need to do from end, so for index 3 = 4 we do not have any right value so its suffix is 1
            and so on similarly
        '''
        for i in range(n):  
            nums[i] = pref[i] * suff[i]

        return nums

    def productExceptSelf2InPlace(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        curr = 1

        for i in range(n):
            res[i] *= curr
            curr *= nums[i]
        print(curr, res)
        ''' we do the exact same thing as done in productExceptSelf2, but we are using one less array. 
        observe how curr is set to 1 and on each iteration it holds the previous nums index value

        and then we just do compute the suffix part below
        '''
        curr = 1

        for i in range(n - 1, -1, -1):
            res[i] *= curr
            curr *= nums[i]

        return res


print(Solution().productExceptSelf2InPlace([1, 2, 3, 4]))
