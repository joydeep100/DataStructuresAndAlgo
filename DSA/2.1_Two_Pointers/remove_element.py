def removeElement(nums, val):

    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return nums[:j]

print(removeElement([3,2,2,3], 3)) # [2,2]
