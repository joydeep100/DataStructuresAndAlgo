/*
https://leetcode.com/problems/container-with-most-water/description/
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
*/

var maxArea = function (height) {

    let l = 0
    let r = height.length - 1
    let maxArea = 0
    let area
    while (1 <= r) {
        area = Math.min(height[l], height[r]) * (r - l)
        // console.log(l,r, area)
        if (area > maxArea) maxArea = area

        // Move the pointer that points to the shorter line
        if (height[l] < height[r]) {
            l++
        } else {
            r--
        }

        // mistake i did was to increment / decrement l & r in an alternate manner where as we need to do it 
        // based on "Move the pointer that points to the shorter line"
        // if (l%2 === 0) l++
        // else r--


    }
    return maxArea
};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

