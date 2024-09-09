/*
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=1
         l
7 ,4 ,5 ,3 ,6  ,4
                r
*/

var maxProfit = function(prices) {

    let l = 0
    let r = 1
    let maxProfit = 0

    while (r < prices.length) {

        if (prices[r] < prices[l]) {
            l = r
        } else {
            maxProfit = Math.max(maxProfit, prices[r] - prices[l])
        }
        r++

    }

    return maxProfit

};

console.log(maxProfit([7,1,5,3,6,4]))
