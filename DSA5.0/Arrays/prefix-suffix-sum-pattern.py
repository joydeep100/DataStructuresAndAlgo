"""
if arr = [1,2,3,4]

prefix_sum = [1,3,6,10] and
suffix_sum = [10,9,7,4]

there are many approaches, if we use an empty array for this and do append it is fine but for suffix_array we need to do insert(0)
or reverse the final array. So this is the best approach
"""

def prefix_suff_sum(arr):

    n = len(arr)
    # best to initialize empty list
    pref, suff = [0] * n, [0] * n

    # construct prefix_array
    sum = 0
    for i in range(n):
        sum += arr[i]
        pref[i] = sum

    # construct suffix array
    sum = 0
    for i in range(n-1,-1,-1):
        sum += arr[i]
        suff[i] = sum

    return pref, suff

print(prefix_suff_sum([1,2,3,4]))


"""
https://leetcode.com/problems/range-sum-query-immutable/description/
303. Range Sum Query - Immutable

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

so basically they want first init the class, meaning create the prefix array 
so that multiple queries can access them
"""

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):

        n = len(nums)
        self.pref = [0] * n

        sum = 0
        for i in range(n):
            sum += nums[i]
            self.pref[i] = sum

    def sumRange(self, left: int, right: int) -> int:
        # not checking invalid ranges for now
        if left == 0:
            return self.pref[right]
        else:
            return self.pref[right] - self.pref[left - 1]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # 1
print(numArray.sumRange(2, 5)) # -1
print(numArray.sumRange(0, 5)) # 3