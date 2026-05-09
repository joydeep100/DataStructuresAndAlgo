"""
Difference array technique is used to do multiple range updates on array efficiently

concept is to create a difference array perform multiple updates on that
and then take a prefix_sum to of the diff_array to get the current snapshot

370. Range Addition
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
"""
from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # this can also be solved using segment trees which is much harder
        n = length

        # construct diff array
        diff_arr = [0] * n
        for update in updates:
            l, r, val = update
            diff_arr[l] += val
            # instead of creating an extra index, better to just skip it
            if r + 1 < n:
                diff_arr[r + 1] -= val

        # in the end we just need to take a prefix sum of the diff_array
        sum = 0
        pref_arr = [0] * n
        for i in range(n):
            sum += diff_arr[i]
            pref_arr[i] = sum

        return pref_arr

sol = Solution()
print(sol.getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]])) #[-2,0,3,5,3]