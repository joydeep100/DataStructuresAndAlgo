function minSubArrayLen(arr, n) {

    if (!arr.length) return undefined

    let i=0
    let j=0
    let tmpSum = arr[i]
    let minLen = Infinity
    
/*
i
[9,3,2,2,5,2,1,1,1], 9
j
*/

    while(i < arr.length && j < arr.length){
        if (i === j){
            if (tmpSum >= n){
                minLen = Math.min(minLen, (j-i)+1)
                tmpSum-= arr[i]
                i++
                j++
                tmpSum+= arr[j]
                continue
            }

            if (tmpSum < n){
                j++
                tmpSum+= arr[j]
                continue
            }
        }

        if (tmpSum >= n){
            minLen = Math.min(minLen, (j-i)+1)
            tmpSum-= arr[i]
            i++
            continue
        }

        if (tmpSum < n){
            j++
            tmpSum+= arr[j]
            continue
        }

    }
    return minLen === Infinity ? 0 : minLen;
}
                
console.log(minSubArrayLen([2,3,1,2,4,3], 7)) // 2 -> because [4,3] is the smallest subarray
// minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the smallest subarray
// minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> because [62] is greater than 52
// minSubArrayLen([1,4,16,22,5,7,8,9,10],39) // 3
// minSubArrayLen([1,4,16,22,5,7,8,9,10],55) // 5
// minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2
// minSubArrayLen([1,4,16,22,5,7,8,9,10],95) // 0