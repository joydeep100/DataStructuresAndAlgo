function binarySearch(arr, n) {
    /*
    S
    [1, 2, 3, 4, 5] , 3
        M        E
    */
    let start = 0
    let end = arr.length - 1
    let mid

    while (arr[mid] !== n && start <= end) {

        mid = Math.floor((start + end) / 2)

        if (n > arr[mid]) {
            start = mid + 1
        }
        else {
            end = mid - 1
        }
       
    }

    return (arr[mid] === n) ? mid : -1

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
// binarySearch([1,2,3,4,5],3) // 2
// binarySearch([1,2,3,4,5],5) // 4
// binarySearch([1,2,3,4,5],6) // -1
