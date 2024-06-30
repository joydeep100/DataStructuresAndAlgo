function divisibleSumPairs(ar, k) {

    /* count of pairs in array [1, 3, 2, 6, 1, 2] when divided by k is 0

    ex. (1,2), (1,2)
        (2,1)
        ()


    */
    let count = 0;
    for (let i = 0; i < ar.length; i++) {
        let sum = 0
        for (let j = i + 1; j < ar.length; j++) {
            sum = ar[i] + ar[j]
            if (sum % k == 0) count++
        }
    }
    return count
}

divisibleSumPairs([1, 3, 2, 6, 1, 2], 3)