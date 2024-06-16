/* 
Find the longest subarray where sum <= k
*/

function longest(arr, k) {

    let l = 0
    let r = 1
    let maxLen = 0
    let sum = 0

    while (r < arr.length) {

        sum += arr[r]

        if (sum <= k){
            
        }



    }

    return maxLen

}

console.log(longest([2, 3, 1, 22, 100, 2, 10], 14))