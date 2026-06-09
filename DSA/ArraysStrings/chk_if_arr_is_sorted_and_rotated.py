""" 1752. Check if Array Is Sorted and Rotated
Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length 
such that B[i] == A[(i+x) % A.length] for every valid index i.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Initiall i though to find pivot and then from 0 to pivot and pivot to end check sorted or not.
But the pivot finding (using binary search) works only for valid rotated sorted array

There is a beautiful way to find is by treating array as a circular array

when we are at the last index, we can compare it against the starting index using arr[i] > arr[(i+1)%n]
n = len of arr
"""
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        
        count = 0
        n = len(nums)
        for i in range(n):
            # for last index, just checking with starting
            # in-case there are more than one max, then surely its not a valid array
            if nums[i] > nums[(i+1) % n]:
                count += 1

        if count > 1:
            return False

        return True
