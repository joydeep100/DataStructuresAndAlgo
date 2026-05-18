''' 153. Find Minimum in Rotated Sorted Array
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
'''

# we can do this in O(n)
def findMinBF(nums):
    # just find the pivot point
    for i in range(0, len(nums)-1):
        if nums[i] > nums[i+1]:
            return nums[i+1], i+1
    return -1


print(findMinBF([3, 4, 5, 1, 2]))

# Using binary search in O(logn)

def findMin(nums):

    res = nums[0]

    l, r = 0, len(nums)-1

    while l <= r:

        # if this is the case we surely know we are in one of the sorted arrays 
        if nums[l] <= nums[r]:
            return min(res, nums[l])

        mid = (l + r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return res


print(findMin([3, 4, 5, 1, 2]))
