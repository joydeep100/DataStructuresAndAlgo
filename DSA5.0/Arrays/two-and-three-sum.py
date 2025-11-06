from typing import List

class Solution:
    """ Two Sum part 1
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    You may assume that each input would have exactly one solution
    """
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {num: i for i, num in enumerate(nums)}

        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in nums_map and nums_map[diff] != i:
                return [i, nums_map[diff]]

sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) # [0,1]
print(sol.twoSumBruteForce([2,7,11,15], 9)) # [0,1]

class Solution:
    """ Two Sum II - Input Array Is Sorted
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    You may assume that each input would have exactly one solution
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        i, j = 0, n - 1

        # useful pattern (2 pointers) also used within 3 sum
        while i < j:
            if numbers[i] + numbers[j] == target:
                # very peculiar, per question index should start from 1
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) # [1,2] p.s. - Expected index starting from 1

class Solution:
    """
    15. 3Sum

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
    and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # we need to sort to handle duplicates
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # take one element and then do 2 sum for the rest

            # for second element onward, if it was same as first on then skip (for the outer loop)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # this part is 2 sum
            l, r = i + 1, n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # here is the tricky part https://youtu.be/jzZsG8n2R9A?t=607
                    # for second element onward, if it was same as first on then skip (for the inner loop)
                    # since we need unique triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res

sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))  # [[-1, -1, 2], [-1, 0, 1]]

