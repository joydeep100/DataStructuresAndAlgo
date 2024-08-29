def binary_search(nums, val):

    l, r = 0, len(nums) - 1 # mistake, r should be -1

    while l <= r:

        mid = (l + r) // 2
        if nums[mid] == val:
            return mid
        
        if val < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
            
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 2, 3, 4, 5], 2))

''' Small variation | 35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where 
it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
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

    # only difference from binary search is returning left
    # if not found
    return left