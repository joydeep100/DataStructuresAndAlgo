/* Two sum, given an array we need to find a pair that matches the given target

Input: nums = [2,7,11,15], target = 9
Output: [0,1] indexes of the matching elements

You may assume that each input would have exactly one solution.
*/

// trying a brute force solution

var twoSum = function (nums, target) {

    let n = nums.length
    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] === target)
                return [i, j]
        }
    }
}

console.log(twoSum([2, 7, 11, 15], 9))

/* can we do it using a 2 pointer approach lets think
This is a better example, but problem is if we alter the original array the original indexes also are lost. 
but its okay we can understand the concept
const nums = [1, 2, 5, 3, 3, 4, 8, 10];
const target = 12;
*/

function twoSum2p(nums, target) {

    let n = nums.length
    nums = nums.sort((a, b) => a - b) // we lost the original indexes, so lets return the pair value instead which sums to target

    let left = 0
    let right = n - 1

    while (left < right) {

        if (nums[left] + nums[right] < target) {
            left++
        } else if (nums[left] + nums[right] < target) {
            right--
        } else { // when equal
            return [nums[left], nums[right]]
        }
    }

    return [-1, -1]

}

console.log(twoSum2p([1, 2, 2, 5, 3, 4, 8, 10], 12))

// now let us try to retain the indexes and return the correct and original indexes

function twoSum2pOrgIdx(nums, target) {

    let n = nums.length
    let numsWithIndices = []
    // Use a for loop to populate the numsWithIndices array
    for (let i = 0; i < nums.length; i++) {
        numsWithIndices.push({ num: nums[i], index: i }); 
        // ***this is just creating another list, in which we also retain the original index***
    }

    numsWithIndices = numsWithIndices.sort((a, b) => a.num - b.num) 
    // we lost the original indexes, so lets return the pair value instead which sums to target

    let left = 0
    let right = n - 1

    while (left < right) {

        if (numsWithIndices[left].num + numsWithIndices[right].num < target) {
            left++
        } else if (numsWithIndices[left].num + numsWithIndices[right].num < target) {
            right--
        } else { // when equal
            return [numsWithIndices[left].index, numsWithIndices[right].index]
        }
    }

    return [-1, -1] //not needed actually since one solution is guaranteed

}

console.log(twoSum2pOrgIdx([1, 2, 2, 5, 3, 4, 8, 10], 12))

// now lets try doing this using a hashmap

var twoSumHM = function (nums, target) {

    let tMap = {}

    let n = nums.length

    for (let i = 0; i < n; i++) {
        let diff = target - nums[i]
        if (diff in tMap) {
            return [tMap[diff], i]
        } else {
            tMap[nums[i]] = i // we can update hash map as we go, no need to update initially
        }
    }
    /* we might get a doubt what if there are duplicates like nums = [1, 2,2,2] so it okay
    because it will simply update the new index value */
}

console.log(twoSumHM([2, 7, 11, 15], 9))