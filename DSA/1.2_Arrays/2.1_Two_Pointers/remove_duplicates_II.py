# Remove duplicates such that each item can appear at most k times

def removeDuplicates(nums, k):

    i = 0
    write_idx = 0

    while(i < len(nums)):
        curr = nums[i]
        count = 0

        # count the number of current item
        while(i < len(nums) and nums[i] == curr):
            count += 1
            i += 1

        # write at most 2 items
        for _ in range(min(k, count)):
            nums[write_idx] = curr
            write_idx += 1

    return nums[:write_idx]

print(removeDuplicates([1,1,1,2,2,3], 2))

#  This is an even better approach

def removeDuplicates(nums, k):

    left, right = 0, 0

    while right < len(nums):

        count = 1
        # see here we are minimizing the number of checks
        # this is a better approach for two pointers, try checking i == i + 1 index if it works
        while right < len(nums) - 1 and nums[right] == nums[right+1]:
            count += 1
            right += 1

        for _ in range(min(count, k)):
            nums[left] = nums[right]
            left += 1
        
        right += 1

    return nums[:left]

print(removeDuplicates([1,1,1,2,2,3], 2))
print(removeDuplicates([1,1,1,2,2,3], 1))