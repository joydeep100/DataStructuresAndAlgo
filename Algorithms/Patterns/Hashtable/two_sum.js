/* 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/

var twoSum = function (nums, target) {

    /* Approach is to make a hashmap and iterate throught the list, if the diff is in the map then we break
    but this would result in O(n + n), once for making the map and once for iterating

    instead we can first check if the diff is there in map, else insert the current item
    which will make it O(n)
    */

    let tmpMap = {}
    let diff
    for (let i = 0; i < nums.length; i++) {
        diff = target - nums[i]
        if (diff in tmpMap) { //can also use tmpMap.hasOwnProperty(diff)
            return [tmpMap[diff], i]
        } else {
            tmpMap[nums[i]] = i
        }

    }

};

/* Here i tried the two pointer approach, for that it works but we first need to sort the input array
that would change the indexes, which does not satisty the condition of this problem
*/

console.log(twoSum([2, 7, 11, 15], 9))