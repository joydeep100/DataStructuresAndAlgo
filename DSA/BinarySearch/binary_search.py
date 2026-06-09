#  Needs a sorted array, can have duplicates. returns on log(n) base 2 time
'''
https://leetcode.com/problems/binary-search/
- Needs input to be sorted
- conversely if input is sorted t becomes very good candiddate for Binary Search
- Or some problem specifies that it has to be done in log(n) time

Blueprint is simple

l, r = 0, n-1

while l <= r: 

# when we have to find a value
# when we are trying to esacpe when both l and r becomes equal then we need to use l < r

    find mid
    
    if we found answer return

    else, increase l or reduce r based on condition

'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l+r) // 2  # better to use l + (r-l)//2 to avoid int overflow

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                '''
                l = mid
                if we make this mistake consider for a small window [3,4] and say target is 9
                mid = 0+1 // 2 = 0
                it will end up in a dead loop, hence excluding mid is important
                after all we did not find target in mid postition, so why include that
                '''
                l = mid + 1
            else:
                r = mid - 1

        return -1


''' Small variation | 35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where 
it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 2
Output: 1
'''
def searchInsert(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 

        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid

    # trick we could have simply returned left here
    if target > nums[mid]:
        return mid + 1
    else:
        return mid
        
    '''
    say 
    1,3,5,6
    1,3
    1      l=0, r=0 hence m=0
    now if target is larger then obviously + 1 
    but if target is smaller then it should be place in mid and existin value should be pushed on rhs
    '''

print(searchInsert([1,3,5,6], 2)) # 1

'''367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the 
product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 l=1 r=16 m=8 m_sq=64 num=16 (target)

if you take 

16 > 8 it would suggest to look in the rhs but we need to look at lhs
16 > 64 would be false, hence we need to comapre m_sq in all three conditions, not just target matching
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l = 1
        r = num

        while l <= r:
            m = (l+r) // 2
            m_sq = m * m
            ''' mistake i did was comparing m instead of m_sq for elif / else parts
            also check Ln[80-81]
            '''
            if m_sq == num:
                return True
            elif num < m: # [tip] never compare with l and r
                r = m - 1
            else:
                l = m + 1

        return False
