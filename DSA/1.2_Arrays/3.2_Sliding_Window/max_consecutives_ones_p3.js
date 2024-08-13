/* 1004. Max Consecutive Ones III Medium
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
*/

var longestOnes = function(nums, k) {

    // [1, 1, 1, 0, 0, 0 ,1, 1, 1, 1, 0]
    //  0  1  2  3  4  5  6  7  8  9  10


    let left = 0
    let right = 0
    let countOfZeros = 0
    let max = 0
    while(right < nums.length){

        if (nums[right] === 0){
            countOfZeros++
        }

        /*max = Math.max(max, right - left + 1)
        my mistake, tried to put the above line here
        when countOfZeros > k which is invalid and should not be updated

        so we need to put it after the while condition
        a. incase its valid it wont even go inside while and gets updated
        b. incase its invalid then it tried to make it valid, if it fails then do no update right?
        */
        while(countOfZeros > k){ // i think putting an if condition here also might work
            if (nums[left] === 0) countOfZeros--
            left++
        }

        max = Math.max(max, right - left + 1)

        right++
    }

    return max
    
};

console.log(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))