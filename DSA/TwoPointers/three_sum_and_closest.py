""" 15. 3Sum

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res= []

        target = 0 # given in the problem

        for i in range(n):

            # ignore duplicates here 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l , r = i + 1, n-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1

                    # part to avoid duplicates / ignore duplicates here 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res
    

"""16. 3Sum Closest

Given an integer array nums of length n and an integer target, 
find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # duplicates are not a big concern here
        nums.sort()

        closest = float('inf')
        closest_sum = 0

        len_nums = len(nums)

        # opt - for i in range(len_nums - 2)
        for i in range(len_nums):

            l, r = i + 1, len_nums - 1

            # other optimization to reduce cycle, but not mandatory
            if i != 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                diff = abs(target - three_sum)
                if diff < closest:
                    closest = diff
                    closest_sum = three_sum

                if three_sum > target:
                    r -= 1
                elif three_sum < target:
                    l += 1
                else:
                    return closest_sum

        return closest_sum
