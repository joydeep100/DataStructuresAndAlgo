'''
This usually works with rotated sorted array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
153. Find Minimum in Rotated Sorted Array

Example 1:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Idea is simple

    if m > r:
        l = m + 1
    else:
        r = m
'''
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
        when l == r we know that we found the minumum so exit
        hence loop till l < r

        and we are guranteed to find min so no False
        we can just return True or False

        4,5,6,7,0,1,2
        l     m     r           

        if m > r:
            l = m + 1
        else:
            r = m

        coz we know if r is > m and we are looking for starting min value
        no point in looking for greater value
        '''

        l = 0
        r = len(nums) - 1

        while l < r:

            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]

'''Now building on this concept we have search in ratated search array
33. Search in Rotated Sorted Array

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

here using the above problem logic we find the pivot index (or min index)

Then there are three conditions
    - element is on rhs , so we trim lhs
    - element in on lsh, so we trim rhs
    - special case, array is sorted without any rotation then we consider full array

now after getting new l & r, we do a classic binary search 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        nums_len = len(nums)

        l = 0
        r = nums_len - 1

        # first find pivt index (where the min index starts)

        while l < r:

            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l


        if min_index == 0:
            l , r = 0, nums_len - 1
        elif nums[0] <= target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        else:
            l , r = min_index, nums_len - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1

        
