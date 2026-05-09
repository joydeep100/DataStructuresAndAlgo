''' 739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

'''
from typing import List

# Brute force

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        l = len(temperatures)

        for i in range(l):

            found = False
            for j in range(i+1, l):
                if temperatures[j] > temperatures[i]:
                    found = True

                if found:
                    res.append(j-i)
                    break
                    
            if not found: res.append(0)
                
        return res

'''
Option 2: Pre-filling the List
Instead of starting with an empty list and appending, you can initialize your result list with 0. This way, you only need to update the value if you actually find a warmer day.

res = [0] * l # Pre-fill everything with 0
for i in range(l):
    for j in range(i + 1, l):
        if temperatures[j] > temperatures[i]:
            res[i] = j - i
            break
            
'''

# Using a monotonic stack
# Its called monotonic stack because the value will wither increase or decrease in same direction
# here in stack at any given time, temp values will be in decreasing order only

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        l = len(temperatures)

        mon_stk = []
        res = [0] * l

        for i, t in enumerate(temperatures):

            while mon_stk and mon_stk[-1][0] < t:
                stk_val, stk_i = mon_stk.pop()
                res[stk_i] = i - stk_i

            mon_stk.append((t,i)) 
            # once we have some index, if we get a greater value we will update it

        return res
    
# more problems on monotonic stack
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# https://leetcode.com/problems/next-greater-element-i