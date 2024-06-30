/* 1732. Find the Highest Altitude
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0. */
var largestAltitude = function (gain) {

    let altitudes = new Array(gain.length + 1).fill(0)
    let currAlt = 0
    let max = 0
    /* if we set max = -Infinity then since we are not checking  "max = Math.max(max, currAlt)" for the i'th altitude
    bcoz currAlt starts from i+1 index we will miss this.
    this is quite tricky and smart. Also we should note the biker always starts form altitude 0 so we are ensured that min altitude
    will always be at-least 0
    */
    for (let i = 0; i < gain.length; i++) {
        currAlt += gain[i]
        altitudes[i + 1] = currAlt
        max = Math.max(max, currAlt)
    }

    return max
};

console.log(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))