''' 605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
'''
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1): # since its index

            if f[i] == 0 and f[i - 1] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return True if n <= 0 else False
    
print(Solution().canPlaceFlowers([1,0,0,0,1], 1))

''' There are lot of edge case, easy trick to smash this problem would be to add a 0 on left and right side.
'''