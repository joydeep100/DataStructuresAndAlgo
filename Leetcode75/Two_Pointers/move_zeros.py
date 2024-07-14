''' Move zero's to the right.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''


class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        # my naive and very inefficient solution, because it took 2s to run
        length = len(nums)

        for i in range(length):
            if (nums[i]) == 0:
                j = i
                while j < length - 1 and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]

        return nums

    def moveZeroes(self, nums: List[int]) -> None:
        # very efficient and clever, keep a write_idx pointer,
        # if number != 0 move it in write_idx pointer position and increment
        length = len(nums)
        write_idx = 0

        for i in range(length):
            if (nums[i]) != 0:
                nums[i], nums[write_idx] = nums[write_idx], nums[i]
                write_idx += 1

        return nums
