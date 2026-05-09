from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        length = len(nums)

        pref, suff = [0] * length, [0] * length

        # construct prefix array
        prev = 0
        for i in range(length):
            pref[i] = nums[i] + prev
            prev += nums[i]

        # construct suffix array
        prev = 0
        for i in range(length-1, -1, -1):
            suff[i] = nums[i] + prev
            prev += nums[i]

        for i in range(length):
            # incase left and right are going out of bounds we should handle it here
            left, right = 0, 0
            if i > 0 and i < length:
                left = pref[i-1]
            if i >= 0 and i < (length - 1):
                right = suff[i+1]
            if left == right:
                return i

        return -1


res = Solution()
# print(res.pivotIndex([1, 7, 3, 6, 5, 6]))
# print(res.pivotIndex([2,1,-1]))
print(res.pivotIndex([1, 2, 3]))

'''
[1,  7,  3,  6,  5,  6]
[1,  8,  11, 17, 22, 28]
[28, 27, 20, 17, 11, 6]
'''
# Another easy way which does not use this pattern but its pretty efficient and clean

class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1


res2 = Solution2()
print(res2.pivotIndex([1, 2, 3]))
print(res2.pivotIndex([2, 1,-1]))
