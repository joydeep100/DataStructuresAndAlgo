"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one = 0, 0
        # two will be len(nums) - (zero + one)

        # compute zero and ones
        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1

        # update zeros
        pos = 0
        for i in range(zero):
            nums[pos] = 0
            pos += 1

        # update ones
        for i in range(one):
            nums[pos] = 1
            pos += 1

        # update the rest with twos
        for i in range(len(nums) - (zero + one)):
            nums[pos] = 2
            pos += 1

        return nums
