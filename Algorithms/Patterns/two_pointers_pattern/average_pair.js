function averagePairImproved(arr, avg_input) {

    if (!arr.length) return false

    let avg = 0
    let i = 0
    let j = 1

    // by using while loop we can also check for the secondary exit condition 
    // once that hits no need to further continue the loop
    while (i < arr.length || arr[i] < avg_input) {
        avg = (arr[i] + arr[j]) / 2
        if (avg.toFixed(2) === avg_input.toFixed(2))
            return true
        j++
        i++
    }

    return false
}

// The average of 2 adjacent elements in an array should be eq to the value passed
// has to be a sorted array

// console.log(averagePairImproved([1, 2, 3, 4, 5, 6, 7], 3.50)) // true
console.log(averagePairImproved([1, 3, 3, 5, 6, 7, 10, 12, 19], 8)) // false
averagePair([-1, 0, 3, 4, 5, 6], 4.1) // false
averagePair([], 4) // false