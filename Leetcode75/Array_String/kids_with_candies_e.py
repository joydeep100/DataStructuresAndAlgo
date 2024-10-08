''' There are n kids with candies. You are given an integer array candies, where each candies[i] represents 
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies 
that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all 
the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
'''
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        top = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= top:
                candies[i] = True  # not using extra memory O(1)
            else:
                candies[i] = False
        return candies


res = Solution()
print(res.kidsWithCandies([2, 3, 5, 1, 3], 3))
