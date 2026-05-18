"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Intuition
let arr = [1,2,3,4,5]

now if we rotate array, arr = [5,1,2,3,4]
again if er rotate array, arr = [4,5,1,2,3]

also note if k (times to rotate) is more than n=len(arr) we can mod it
reason is if we rotate arr n times we get the same array so we can just do k = k % n
note 1 % 5 is 1 itself

now assume k=2, final array we should get is [4,5,1,2,3]

notice this
- reverse the entire original arr [5,4,3,2,1]
- now reverse first k elements [4,5 -- 3,2,1]
- now reverse last n-k elements [4,5 -- 1,2,3] --> that's our required solution!
"""

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def _rotate_sub_arr(self, start, end):
        # self.nums[start:end:-1] won't work because it creates a replica array

        # how to reverse an array in=place efficiently
        while start < end:
            self.nums[start], self.nums[end] = self.nums[end], self.nums[start]
            start += 1
            end -= 1

    def rotate(self, k) :
        n = len(self.nums)

        # mod k if k is greater than n , mod will give same value of k if its less
        k = k % n

        # rotate the full array, make n-1 since you are using indexes
        self._rotate_sub_arr(0, n-1)

        # rotate the first k elements
        self._rotate_sub_arr(0, k-1)

        # rotate the remaining elements
        self._rotate_sub_arr(k, n-1)

        return self.nums

sol = Solution(nums = [1,2,3,4,5])
print(sol.rotate(k = 2)) # [4, 5, 1, 2, 3]