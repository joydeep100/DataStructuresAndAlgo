# remove duplicates from sorted array
def removeDuplicates(nums):

    i, j = 0, 0
    n = len(nums)
    pos = 0

    while i < n:
        # don't get compelled to add check for j here

        nums[pos] = nums[i]
        pos += 1

        while j < n and nums[i] == nums[j]:
            # boundary should be checked first
            j += 1

        # at this point j-i would give frequency of each item which in itself is very useful
        i = j

    return pos

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))