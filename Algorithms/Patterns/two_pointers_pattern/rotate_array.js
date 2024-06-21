/*189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

*/

function rotate(nums, k) {

    /* First approach but we need a duplicate array so space complexity would be O(2n)
    [1,2,3,4,5,6,7] and say k = 3 Output: [5,6,7,1,2,3,4]

    first we fill from k to nums.length -1 
    [_,_,_,1,2,3,4,5]

    then we have to fill 5,6,7 in the intial part which can be done using mod
    so, 5 should go in 0'th index

    so formula is (i + k % nums.length)
    4 + 3 % 7 = 0

    */
    let modIndex
    let nums2 = [] // mistake, just defined let nums2 instead of let nums2 = [], an insert will fail!!
    for (let i = 0; i < nums.length; i++) {

        if (i < nums.length - k) {
            nums2[i + k] = nums[i]
        } else {
            // problem, be very careful will brackets in js. need to be extra careful
            modIndex = ((i + k) % nums.length)
            nums2[modIndex] = nums[i]
        }
    }

    // space complexity is O(2n)
    return nums2
}

function rotateOptimized(nums, k) {

    /* using this approach we can solve this problem in space complexity O(1) since it is inplace
    1, 2, 3, 4, 5, 6, 7 and k = 3 Output: [5,6,7,1,2,3,4]

    reverse it once
    7, 6, 5,  |   4, 3, 2, 1

    now reverse these individual slices
    5, 6, 7, | 1, 2, 3, 4 which gets us to the required output
    */

    k = (k % nums.length)

    if (k === 0) return nums //[1]
    /* 3 % 7 is 3
     VVI step to consider in case k > nums.length lets say nums.length = 4 and k = 4 
     then rotating a array of length 4, 4 times would result in the same array

     1,2,3,4

     4,1,2,3
     3,4,1,2
     2,3,4,1
     1,2,3,4

     so we need to mod it, and lets say nums.length = 4 and k = 5
     we can just rotate it once

     incase k === 0 then just return the array [1]
     */
    // rotate the entire array
    let left = 0
    let right = nums.length - 1
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]]
        left++
        right--
    }

    // rotate the first slice (0 -> k -1)
    left = 0
    right = k - 1
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]]
        left++
        right--
    }

    // rotate the first slice (k -> length of arr)
    left = k
    right = nums.length - 1
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]]
        left++
        right--
    }

    return nums
}

// console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3))
// console.log(rotateOptimized([1, 2, 3, 4, 5, 6, 7], 3))
console.log(rotateOptimized([-1], 2))


/* Also made the repeated part into a helper function

function rotateOptimized(nums, k) {

    function helper(left, right, arr){
        while (left < right) {
            [nums[left], nums[right]] = [nums[right], nums[left]]
            left++
            right--
        }
        return arr
    }
    
    // rotate the entire array
    nums = helper(0, nums.length -1, nums)

    // rotate the first slice (0 -> k -1)
    nums = helper(0, k -1, nums)

    // rotate the first slice (k -> length of arr)
    nums = helper(k, nums.length - 1, nums)

    return nums
}
*/

