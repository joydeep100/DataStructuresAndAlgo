/*80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

l 
1 1 1 2 2 2 3
r

Logic the problem comes in thw way you are looking at how to solve it (was thinking in r=1, and nums[r-1] === nums[r] like so)
so what needs to be done is

we need to look if r === r+1, in this way we can avoid going to 2

l 
1 1 1 2 2 2 3
    r

now we have count as 3 (start with count =1)

we know only 2 items (max) can be what is r right now (last item of same type)

so lets take min(2, count) and insert r (last item of same type) and increment l each time by 1

    l 
1 1 1 2 2 2 3
    r

now we just increment r by 1 

    l 
1 1 1 2 2 2 3
      r

and continue the logic, keep the boudary conditions in check.
*/

var removeDuplicates = function(nums) {
/*
        l 
1 1 2 2 2 2 3
            r
*/
    let left = 0
    let right = 0
    let tmpCount

    while(right < nums.length){

        tmpCount = 1
        //see when r is at the end, see still tmpCount = 1 which is what is needed
        
        while(nums[right] === nums[right+1] && right < nums.length - 1){
            right++
            tmpCount++
        }

        // silly i < 2, will be 2 iterations right. 0, 1 will both be pass and not 0->1 & 1->2
        for(let i = 0; i < Math.min(2, tmpCount); i++){
            nums[left] = nums[right]
            left++
        }

        right++
    }
    // the last position of left is what needs to be returned
    return left
    
};

console.log(removeDuplicates([1,1,1,2,2,3]))