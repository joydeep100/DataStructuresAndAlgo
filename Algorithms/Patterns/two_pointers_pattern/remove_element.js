/*
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
*/

/*
i points to the point till job id done
j will be the iterator

j === val nothing to do 
else in i the position put j and increment i & j

  i
 [3,2,2,3]
  j

  i
 [3,2,2,3]  
    j

    i
 [2,2,2,3]  
      j

      i
 [2,2,2,3]  so till i, i.e. i-1 is the final arr  
        j
 */

var removeElement = function(nums, val) {

    let i = 0    

    for(let j=0; j< nums.length; j++){

        if (nums[j] !== val){
            nums[i] = nums[j]
            i++
        } 

    }

    return i
};

console.log(removeElement([3,2,2,3], 3)) // o/p 2 since final array would be [2,2]