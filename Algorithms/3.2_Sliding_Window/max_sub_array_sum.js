// We need to find largest sum of n (number) items in a given array
// sub array is a contiguous data
// ex maxSubArray([1,2,3,4], 2) returns 7 (sum of largest 2 congruent items)

function maxSubArray(arr, number) {

    let max = 0
    let tmpMax = 0
    if (arr.length < number) return null
    for (let i = 0; i < number; i++) {
        max += arr[i]
    }

    tmpMax = max // place where i missed to define
    for (let i = number; i < arr.length; i++) {
        tmpMax = tmpMax + arr[i] - arr[i - number] //i missed here as well, use max instead of tmpMax
        // max is init, then offcourse the iterative checking must be done using tmpMax right.
        max = Math.max(tmpMax, max)
    }

    return max
}



console.log(maxSubArray([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))

