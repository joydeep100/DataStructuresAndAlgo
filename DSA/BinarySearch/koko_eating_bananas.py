''' 875. Koko Eating Bananas
https://www.youtube.com/watch?v=ceYZ5RgwQwQ

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, 
she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas 
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''
import math
from typing import List

class Solution:
    def minEatingSpeedBF(self, piles: List[int], h: int) -> int:
        # brute force

        # till max(piles) because with max eating speed all other piles would be over in 1 hr each 
        # and if we see the constraint piles.length <= h, we are guaranteed that at-least 
        # len(piles) hrs would be provided
        
        for k in range(1, max(piles) + 1):

            hrs_left = h

            for pile in piles:
                time_needed = math.ceil(pile / k)
                hrs_left -= time_needed

            if hrs_left >= 0:
                return k

    def minEatingSpeedSorted(self, piles: List[int], h: int) -> int:

        piles.sort()
        # this will need input array to be sorted

        l = 1
        r = piles[-1]

        def _min_condition(piles, h, k):
            for pile in piles:
                time_needed = math.ceil(pile / k)
                h -= time_needed

            return h >= 0

        while l < r:

            k = (l + r) // 2

            if _min_condition(piles, h, k):
                r = k
            else:
                l = k + 1

        return l

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles) # best aproach

        # why this works without sorting the input array is because we are looping over l -> r or 1 -> max(piles) which is naturally sorted

        def _min_condition(piles, h, k):
            for pile in piles:
                time_needed = math.ceil(pile / k)
                h -= time_needed

            return h >= 0

        while l < r:

            k = (l + r) // 2

            if _min_condition(piles, h, k):
                r = k
            else:
                l = k + 1

        return l