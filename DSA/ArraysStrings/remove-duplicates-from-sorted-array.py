def removeDuplicatesSortedArray(nums):
    """
    Set pos pointer at beginning
    Iterate through array with i pointer barring first element
    the moment array element at i is not equal to element at pos
    increment pos and copy element at i to pos
    """
    pos = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[pos]:
            pos += 1
            nums[pos] = nums[i]

    return nums[:pos+1]
    
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicatesSortedArray(nums))

# can also be done like this
def removeDuplicatesSortedArray2(nums):
    # since first element is always unique
    """
    Array look back approach
    """
    pos = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[pos] = nums[i]
            pos += 1

    return nums[:pos]
    
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicatesSortedArray2(nums))

# remove duplicates from sorted array
def removeDuplicatesSortedArray3(nums):
    # Two pointers approach
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
print(removeDuplicatesSortedArray3(nums))

def removeDuplicatesUnsorted(nums):
    seen = set()
    pos = 0

    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[pos] = nums[i]
            pos += 1

    return nums[:pos]

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicatesUnsorted(nums))