/*1052. Grumpy Bookstore Owner

There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.
 
Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
*/
var maxSatisfied = function (customers, grumpy, minutes) {
    let right = 0
    let baseSatisfied = 0
    let additionalSatisfied
    let maxSatisfied = 0


    /* so basically, this is the magic
       customers = [1,0,1,2,1,1,7,5]
       grumpy =    [0,1,0,1,0,1,0,1]

       minutes = 3 ,means for any consecutive seconds we can make the owner non grumpy. 
    */

    // get the regular score (without using k extra minutes of non grumpiness)
    for (let i = 0; i < customers.length; i++) {
        if (grumpy[i] === 0) 
            baseSatisfied += customers[i]
    }
    
    while (right <= customers.length - minutes) {
        // [M] missed <=, had use <
        additionalSatisfied = 0
        for(i=0; i < minutes; i++){
            if (grumpy[right + i] === 1) {
                additionalSatisfied += customers[right + i]
            }
        }

        maxSatisfied = Math.max(maxSatisfied, baseSatisfied + additionalSatisfied)
        // [M] this part need to be super careful

        right++
    }

    return maxSatisfied
};

console.log(maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
// console.log(maxSatisfied([4,10,10], [1,1,0], 2))