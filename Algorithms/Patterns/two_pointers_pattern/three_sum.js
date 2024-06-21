/** 15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

[-1, 0, 1, 2, -1, -4]

     i
-4, -1, -1, 0, 1, 2
         l            
                  r
*/
var threeSum = function (nums) {

    nums = nums.sort((a, b) => a - b)

    let left
    let right
    let res = []
    for (i = 0; i < nums.length - 2; i++) {

        // we just need to skip this check for the very first item for rest just increment i
        // in two parts of this array we can step into duplicacy, first is when i + 1 = i from second item onwards which is handled here [1]
        if (i >= 0 && nums[i] === nums[i - 1]) {
            continue
        }

        left = i + 1
        right = nums.length - 1

        while (left < right) {
            tmpSum = nums[i] + nums[left] + nums[right]
            if (tmpSum > 0) {
                right--
            } else if (tmpSum < 0) {
                left++
            } else {
                res.push([nums[i], nums[left], nums[right]])
                left++ 

                // this part is just so we can avoid duplicates (within the 2sum array slice) and is quite tricky [2]
                // [-2, -2, 0, 0, 2, 2] assume this is the 2sums slice and i = 0
                // https://youtu.be/jzZsG8n2R9A?t=622 to understand this part watch this section, many times :P

                while (nums[left] === nums[left - 1] && left < right) {
                    left++
                }

            }

        }

    }
    return res
};


console.log(threeSum([-1, 0, 1, 2, -1, -4]))