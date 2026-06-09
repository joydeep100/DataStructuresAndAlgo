'''162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is 
outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.
'''
from typing import List

class Solution:
    def findPeakElementBF(self, nums: List[int]) -> int:
        len_n = len(nums)

        for i in range(len_n):

            if i > 0 and i < len_n -1 and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            elif len_n == 1:
                return i
            elif i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == len_n -1 and nums[i] > nums[i-1]:
                return i

    # https://www.youtube.com/watch?v=zOPlx3ppyWU
    # neetcode / striver dont have the best approach here
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]: 
                l = m + 1
            else: 
                r = m
        return l

'''
The hiddent contraint in this question is no two adjacent numbers can be same [1]
so how did this work

 0 1 2 3 4 5 6
[1,2,1,3,5,6,4]
 l     m     r

 if we side right to mid, we can see it increases. so we are guaranteed a peak on right
 say 3,4,5,6,7 then peak is 7. 
 
 3,4,4,4,4 cant be because of [1]

 else, there must be a peak on the left. we close in when l = r and can return any one of them

 lets dry run

 0 1 2 3 4 5 6
[1,2,1,3,5,6,4]
 l     m     r

 
 5,6,4
 l m r

 5,6
 l r
 m

 actually before this point we will exit because while l < r, so they cannot be same
 6
 l
 r

'''