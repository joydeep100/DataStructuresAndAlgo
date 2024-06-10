function areThereDuplicates(...arr) {
    // using ... spread i can convert the args into an array

    // its very simple to use a frequency counter here
    // but let us try to use 
    if (!arr.length) return undefined

    arr.sort() //making sure that the arr is sorted

    let i = 0
    for (let j = 1; j < arr.length; j++) {
        if (arr[i] === arr[j]) {
            return true
        }
        i++
    }

    return false

}

console.log(areThereDuplicates(1, 2, 3))
console.log(areThereDuplicates())

/*
very imp concept
i
[1,2,3,4]
   j

now when i !== j, we can conviniently move both the pointers right
so as i = 2, j = 3
just moving j = 3 will make this into O(n^2) and it does not even require
because we established that i !== j
*/