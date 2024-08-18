function areThereDuplicates(...arr) {

    if (!arr.length) return undefined

    arr.sort() 

    let i = 0
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] === arr[i+1]) {
            return true
        }
    }

    return false

    // we can also use a hashmap to do this in O(n)

}

console.log(areThereDuplicates(1, 2, 3))
console.log(areThereDuplicates(1, 2, 3, 3))