'''
leetcode 33
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
def search(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        
        # to search in the left part of the sorted array
        # <= because array can be something like [5,5,5,5,1,2]
        
        # also only way our item belongs to the left sorted array if the below condition satisfies
        if  nums[mid] >= nums[l]:
            
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # to search in the right part of the sorted array
        # now its just the reverse
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1

print(search([4,5,6,7,0,1,2], 0))