/* 167. Two Sum II - Input Array Is Sorted
Medium
Topics
Companies
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
*/

var twoSum = function(nums, target) {

    let left = 0
    let right = nums.length - 1
    while (left < right){

        if (nums[left] + nums[right] > target){
            right--
        } else if (nums[left] + nums[right] < target){
            left++
        } else return [++left, ++right] 
        
        //mistake i did left++, right++ it gave the original values
        // because the output needed is index+1 as per question

    }
    
};

console.log(twoSum([2,7,11,15], 9))