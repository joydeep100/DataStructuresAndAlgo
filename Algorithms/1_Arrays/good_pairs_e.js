/* Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed. */

/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairsBF = function(nums) {

    const n = nums.length
    let count = 0
    for(let i=0; i < n-1; i++){
        for(let j=i+1; j < n; j++){
            if (nums[i] === nums[j]){
                count++
            }
        }
    }
    return count
};

var numIdenticalPairs = function(nums) {

    //O(n) solution using a hashmap

    // build the map
    let tMap = {}
    for(let num of nums){
        tMap[num] = (tMap[num] || 0) + 1
    }

    //[1,2,3,1,1,3] now if we take this array we have 1 thrice
    // so good pairs with 1 are indexes (0,3), (0,4) and (3,4)
    // so ans = 3 when n = 3, which is n(n-1)/2

    let ans = 0
    for(let key in tMap){
        const n = tMap[key]
        ans += (n*(n-1))/2
    }

    return ans

};