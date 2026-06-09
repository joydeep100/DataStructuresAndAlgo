'''3043. Find the Length of the Longest Common Prefix
Example 1:

Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.
Example 2:

Input: arr1 = [1,2,3], arr2 = [4,4,4]
Output: 0
Explanation: There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        ''' so idea is from arr1 make all possible prefixes set
        1, 10, 100
        from 100 itself we can get 1, 10 and 100 but since its set its ignored

        now in arr2 (for single or multple)
        split each into prefixes
        like 1000 --> 1000,100,10,1

        now whichever matched in set, convert into str and take its length.
        Also possible to get length using code, but it does not impact time complexity.
        '''
        arr1_pref = set()

        for num in arr1:

            val = num
            while val > 0 and val not in arr1_pref:
                arr1_pref.add(val)
                val //= 10

        # print(arr1_pref) {1, 10, 100}

        longest = 0
        for num in arr2:
            val = num
            while val > 0:
                if val in arr1_pref:
                    longest = max(longest, len(str(val)))
                val //= 10

        return longest


            