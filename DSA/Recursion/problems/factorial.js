function factorial(n) {

    if (n < 1) return undefined
    // the code fails if we try with negative n

    if (n === 1) {
        return 1
        // return 1 instead of just return, because it may return undefined otherwise
    }
    return n * factorial(n - 1)
}

console.log(factorial(-21))