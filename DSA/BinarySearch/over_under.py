''' Over Under Pattern
https://www.youtube.com/watch?v=9nmrkG6QtpQ

This is a second type of pattern where we have a sequence of something, say True or False 
and then the sequence changes

say arr = [False, False, False, True, True, True, True, True, True, True]

here we have to find out the first index when the array value changes

[False, False, False, True, True, True, True, True, True, True] l = 0, r=9, m=4

now we can see m is already True so on right side also it must be true so we can forget that part
hence we do, r=m and we have

[False, False, False, True, True] l=0, r=4

*** note: In reality l will be 5 and r will be 9, but assuming the left part of arr gone is also okay
for simplification.

now m=2 is False now we can do l = m+1 since we got False

[True, True] l=0 r=1 m=0, therefore r=m=0

[True] l=0, r=0
'''

def binary_search_condition(arr):
    l=0
    r=len(arr) - 1

    while l < r:
        # imp, if we make <= then see for the last leg when only one item [True] is left 
        # it will keep on looping and never exit

        # basically when they are equal our condition has been met, so exit

        mid = (l+r)//2
        if arr[mid] == True: 
            r = mid
        else:
            l = mid + 1

    return l # or r (both are okay)

arr = [False, False, False, True, True, True, True, True, True, True]
print(binary_search_condition(arr))

'''278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version,
 all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

example below
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 1
        r = n

        while l < r:

            m = (l+r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l

    # Explanation 4th is the first bad version

    '''If needed we can also return when l == r'''
    def firstBadVersion2(self, n: int) -> int:

        l = 1
        r = n

        while l <= r:

            m = (l+r) // 2
            if l == r:
                return l
            elif isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l