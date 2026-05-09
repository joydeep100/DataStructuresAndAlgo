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
    def productExceptSelfBF(self, nums: List[int]) -> List[int]:
        
        # brute force - Run two loops with i and j starting at 0th index
        # then when both pointers are not in same place, multiply everything

        l = len(nums)
        res = [0] * l
        
        for i in range(l):
            val = 1
            for j in range(l):
                if i != j:
                    val *= nums[j]
            res[i] = val

        return res 

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # https://www.youtube.com/watch?v=yKZFurr4GQA&t=426s

        l = len(nums)
        l_mult = 1
        r_mult = 1

        l_arr = [0] * l
        r_arr = [0] * l

        for i in range(l):
            l_arr[i] = l_mult
            l_mult *= nums[i]

            # trick to get index from last is to use (-i -1)
            j = -i -1

            r_arr[j] = r_mult
            r_mult *= nums[j]

        
        return [l*r for l,r in zip(l_arr, r_arr)]

s = Solution()
print(s.productExceptSelf([1,2,3,4]))