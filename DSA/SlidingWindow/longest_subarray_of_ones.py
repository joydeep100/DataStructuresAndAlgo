from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zeros = 0
        left = 0
        right = 0

        res = float("-inf")
        while right < len(nums):

            if nums[right] == 0:
                zeros += 1

            while left < len(nums) and zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ''' This problem i was struggling quite a lot because i was using logic 
            till the window is valid as below

            while right < len(nums) - 1 and no_of_zeros <= 1:
                if nums[right] == 0:
                    no_of_zeros += 1
                right += 1

            i could only solve it when i changed the approach to, if invalid try to make it valid 
            by incrementing left and only then go to next iteration to increment right
            '''
            res = max(res, right - left + 1 - zeros)
            right += 1

        return res - 1 if res == len(nums) else res

res = Solution()
# print(res.longestSubarray([1,1,0,1]))
print(res.longestSubarray([0,1,1,1,0,1,1,0,1]))

