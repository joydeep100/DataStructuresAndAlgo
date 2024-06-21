/* 209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
*/

var minSubArrayLen = function(target, nums) {

    let left = 0
    let right = 0
    let minLength = Infinity //very nice that you have used Infinity, just make sure you handle this in the return stmt
    let sum = 0

    while(right < nums.length){

        sum+= nums[right]

        // first and second if could be clubbed right and we ideally do not need the if condition
        // if (sum === target){
        //     minLength = Math.min(minLength, right - left + 1)
        // }
        // if (sum > target){

        while (sum >= target){
            minLength = Math.min(minLength, right - left + 1)
            sum-= nums[left]
            left++
        }

        // min length should be in correct place
        // minLength = Math.min(minLength, right - left + 1)
        // }

        right++

    }

    return minLength === Infinity ? 0 : minLength;

};