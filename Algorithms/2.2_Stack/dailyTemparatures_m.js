/* 739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the 
number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is 
possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

so we need to find for each day's temp, after how many more days we get a hotter day
so for first day : 73 we get a hotter day the very next day so we put 1

and for 75 we get a hotter day 76 which is after 4 days so we put 4
*/

var dailyTemperatures = function (temperatures) {

    let stack = []

    let res = new Array(temperatures.length).fill(0) // fill all the values of array with 0's

    for (let i = 0; i < temperatures.length; i++) {

        // if stack is empty we just push the current day's temp to stack
        // next iteration - now next day if we find day is hotter, we 
        const todaysTemp = temperatures[i]
        while (stack.length && todaysTemp > stack[stack.length-1][0]) {

            const [stackVal, stackIdx] = stack.pop() 
            /* or we could have done
            const stackItem = stack.pop() 
            res[stackItem[1]] = i - stackItem[1] // since we are storing the index like this [todaysTemp, i]
            */

            // now we just update the popped items corresponsing index in result array
            res[stackIdx] = i - stackIdx
        }

        // every day's temp has to be put on the stack, one by one
        // note we put both the value and index
        stack.push([todaysTemp, i]) 

    }

    return res
}

console.log(dailyTemperatures([73,74,75,71,69,72,76,73]))