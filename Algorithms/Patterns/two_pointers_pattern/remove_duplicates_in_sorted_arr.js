/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
*/

let removeDuplicates = function(nums) {

    /*
    set i = 1, j = 1 since first element is alwways sorted in a sorted array
    now comaprision is j === j-1, if so j++
    else it means values are diff
    now swap i and j values and increment i

       i
    [0,0,1,1,1,2,2,3,3,4]
       j
    */
    let i = 1
    for(let j=1;j < nums.length;j++){

        if (nums[j] !== nums[j-1]){
            nums[i] = nums[j]
            i++
        } 
    }
    return i
};

removeDuplicates([0,0,1,1,1,2,2,3,3,4]) //o/p 5