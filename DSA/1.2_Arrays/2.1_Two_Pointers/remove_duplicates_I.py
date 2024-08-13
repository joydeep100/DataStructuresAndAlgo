def removeDuplicates(nums):
    left, right = 0, 0    
    # My solution
    while right < len(nums):
        if nums[right] != nums[left]:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
        right += 1
    
    return nums[:left+1] # kind of jugaad for +1

# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# Better solution
def removeDuplicatesB(nums):
    '''
       i 
    [0,0,1,1,1,2,2,3,3,4]
       j
       i 
    [0,0,1,1,1,2,2,3,3,4]
         j
         i 
    [0,1,1,1,1,2,2,3,3,4]
               j
    '''
    left = 1

    for right in range(1, len(nums)):

        if nums[right] != nums[right-1]:
            nums[left] = nums[right]  
            # so the trick is that we do not swap but we assign it to nums[left] so nums[right]
            # does not change.. hmm!
            left += 1

    return nums[:left]


print(removeDuplicatesB([0,0,1,1,1,2,2,3,3,4]))
