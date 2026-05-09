function binarySearch(arr, n) {

    let left = 0
    let right = arr.length - 1

    while (left <= right) {

        const mid = Math.floor((left + right) / 2)

        if (n > arr[mid]) left = mid + 1
        else if (n < arr[mid]) right = mid - 1
        else return mid // Element found, return its index (n === arr[mid])

    }
    return -1
}

/*
Big(O) 
Best Case = O(1) if we found the element in the very first try
Worst Case = O(log(n)) , not n since we are dividing the array each time

The same code also works for characters, and 'b' > 'a' returns true in js

and interestingly also works on an array of sorted words
*/

console.log(binarySearch([1, 2, 3, 4, 5], 2)) // 1
// console.log(binarySearch(['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi'], 'grape')) //5

// can we do a recursive funciton for this, lets try, almost got it correct

function binarySearchRecursive(arr, n, i, j) {

    if (i > j) {
        return -1; // Base case: element not found, missed to add this as well
    }

    let mid = Math.floor((i + j) / 2) // mistake did i + j / 2

    if (arr[mid] < n) {
        return binarySearchRecursive(arr, n, mid + 1, j) // forgot to add return here
    } else if (arr[mid] > n) {
        return binarySearchRecursive(arr, n, i, mid - 1)
    } else {
        return mid
    }
    
}

function binarySearchRecursiveWrapper(arr, n) {
    if (arr.length < 1) return -1
    return binarySearchRecursive(arr, n, 0, arr.length - 1)
}

console.log(binarySearchRecursiveWrapper([1, 2, 3, 4, 5], 2))
// console.log(binarySearchRecursiveWrapper([2], 2))