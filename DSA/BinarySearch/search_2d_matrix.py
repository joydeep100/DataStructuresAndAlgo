'''74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

* Clue is m * n is essentially rows*cols and doing in log time needs binary search

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = (m*n) - 1

        while l <= r:

            # refer DSA/ArraysStrings/matrix_traversal.py for matrix traversal
            
            mid = (l+r) // 2
            r_cord, c_cord = mid // n, mid % n

            if matrix[r_cord][c_cord] == target:
                return True
            elif target > matrix[r_cord][c_cord]: # mistake was checking against mid
                l = mid + 1
            else:
                r = mid - 1

        return False