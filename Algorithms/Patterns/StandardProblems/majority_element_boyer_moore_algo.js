/* 169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

so element should appear more than n/2 times where n is the length of the array.
*/

function majorityElementBF(nums) {
    // Brute force

    let maxFreq = 0
    let maxFreqEle = -1
    let tmpCount

    // O(n^2) & space is O(1)
    for (let i = 0; i < nums.length; i++) {
        tmpCount = 0
        for (let j = 0; j < nums.length; j++) {
            if (nums[j] === nums[i]) {
                tmpCount++
            }
        }
        if (tmpCount > maxFreq) {
            maxFreq = tmpCount
            maxFreqEle = nums[i]
        }
    }
    return maxFreqEle
}

function majorityElementHM(nums) {
    // Using Hash Maps

    // O(2n) but space wise this is O(n)  

    tmpMap = {}
    for (let i = 0; i < nums.length; i++) {
        tmpMap[nums[i]] = (tmpMap[nums[i]] || 0) + 1
    }

    for (let key in tmpMap) {
        if (tmpMap[key] > Math.floor(nums.length / 2)) {
            return key
        }
    }
    return -1

}

function majorityElementBM(nums) {
    // Using Boyer Moore Voting Algo

    // O(2n) but space wise it is O(1)
    let vote = 0
    let element
    for (let i = 0; i < nums.length; i++) {
        if (vote === 0) {
            // means either first item or vote has be nullified so new element needs to be considered
            element = nums[i]
            vote++
        } else if (nums[i] === element) {
            vote++
        } else {
            vote--
        }
    }

    // if we are sure that a majority element exists then we can just return element here

    // else we just need to do one more check to find it the element is having value > n/2 where n=length of array
    let count = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === element) {
            count++
        }
        if (count > Math.floor(nums.length / 2)) {
            return element
        }
    }
    return -1
}

// console.log(majorityElementBF([2, 2, 1, 1, 1, 2, 2]))
// console.log(majorityElementHM([2, 2, 1, 1, 1, 2, 2]))
console.log(majorityElementBM([2, 2, 1, 1, 1, 2, 2]))