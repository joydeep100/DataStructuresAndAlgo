'''2657. Find the Prefix Common Array of Two Arrays

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers 
that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

Constraints:

1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
'''
from typing import List

class Solution:
    def findThePrefixCommonArrayBF(self, A: List[int], B: List[int]) -> List[int]:
        
        set_a , set_b = set(), set()
        res = []

        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])

            # the below step should be O(n), not very optimal
            res.append(len(set_a & set_b))

        return res

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        len_arr = len(A)
        '''create a freq. array
        This only works because we looked into the constraints
        
        1 <= A.length == B.length == n <= 50
        1 <= A[i], B[i] <= n <-- the same n as length
        It is guaranteed that A and B are both a permutation of n integers.

        so we are ensured that there wont be random numbers

        1 3 2 4
        3 1 2 4

        freq_arr 
        1 0 0 0   -> no common
        1 0 1 0   -> no common

        1 0 2 0   -> one common
        2 0 2 0   -> two common

        2 1 2 0   -> two common
        2 2 2 0   -> three common

        2 2 2 1   -> three common
        2 2 2 2   -> four common
        '''
        freq_arr = [0] * len_arr

        common_count = 0
        res = []

        for i in range(len_arr):
        
            freq_arr[A[i]-1] += 1
            # this part can be understood if we dry run
            if freq_arr[A[i]-1] == 2:
                common_count += 1

            freq_arr[B[i]-1] += 1
            if freq_arr[B[i]-1] == 2:
                common_count += 1

            res.append(common_count)

        return res
