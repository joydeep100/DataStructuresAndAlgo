''' Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
def removeDuplicates(nums):

    i = 0
    write_idx = 0 # for in-place updates alwyas use a write pointer

    while(i < len(nums)):
        curr = nums[i] # for every character, use a curr pointer
        while(i < len(nums) and nums[i] == curr): # note, if you put i < len(nums) as the second condition
            i += 1                                # then we will get array out of bounds error

        nums[write_idx] = curr
        write_idx += 1

    return nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) #o/p 5

''' So pattern is something like this

    - use an index i to traverse from left to right
    - use a write_idx pointer to store the next write position
    
    - first while to traverse the array
    - create a curr = nums[i] pointer to keep track of the current value
    
    - inner while till the both values are same or any other condition as per question
    - be mindful to check i < len(nums) before the other condition to avoid out of bounds check
'''