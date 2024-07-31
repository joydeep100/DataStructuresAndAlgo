from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        right = k - 1    # mistake, used 3 which was specific to one test case :P
        window = sum(nums[:k])
        max_window = window
        while right < len(nums) - 1:

            window -= nums[left]
            left += 1
            right += 1
            window += nums[right]

            if window > max_window:
                max_window = window

        return max_window / k


res = Solution()
# print(res.findMaxAverage([1,12,-5,-6,50,3], 4))
print(res.findMaxAverage([0, 0, 3, 2, 4], 5))
