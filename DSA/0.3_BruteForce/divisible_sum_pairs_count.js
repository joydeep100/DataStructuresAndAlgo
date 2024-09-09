function divisibleSumPairs(arr, k) {

    /* count of pairs in array [1, 3, 2, 6, 1, 2] when divided by k is 0

    ex. (1,2), (3,6), (2,1), (1,2), 5
    */
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if ((arr[i] + arr[j]) % k == 0) count++
        }
    }
    return count
}

console.log(divisibleSumPairs([1, 3, 2, 6, 1, 2], 3))