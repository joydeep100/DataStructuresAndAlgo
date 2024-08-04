# Remove duplicates such that each item can appear at most twice, return k (index)

def removeDuplicates(nums):

    i = 0
    write_idx = 0

    while(i < len(nums)):
        curr = nums[i]
        count = 0
        while(i < len(nums) and nums[i] == curr):
            count += 1
            i += 1

        for _ in range(min(2, count)):
            nums[write_idx] = curr
            write_idx += 1

    return write_idx

print(removeDuplicates([1,1,1,2,2,3])) # 5