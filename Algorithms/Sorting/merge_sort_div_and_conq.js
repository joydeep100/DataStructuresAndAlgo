/*
merge sort - It follows divide and conquer pattern
It's a very efficient and fast algorithm.
Best way is to wrie a merge() which takes in ***two sorted arrays***

then write a megreSort() which is recursive

time complexity
Best / Worst case - nlog(n)
log(n) because we jave to divide it (into half so its base 2) n times
and n * log(n) becauser we need to do n comparisions in each of the smaller halves 

space complexity - O(n)
*/

// lets us start by writing merge() of two sorted arrays

function merge(arr1, arr2){
    // merging two sorted arrays - this is the key

    mergedArr = []
    let i = 0
    let j = 0
    while (i < arr1.length && j < arr2.length) { //this would ensure the min one would be considered

        if (arr1[i] < arr2[j]){
            mergedArr.push(arr1[i])
            i++
        }
        else {
            mergedArr.push(arr2[j])
            j++
        }
    }
    
    // if we have arrays of different length then we need to just append the remaining items of the lerger array
    // by doing this

    while (i < arr1.length){
        mergedArr.push(arr1[i])
        i++
    }

    while (j < arr2.length){
        mergedArr.push(arr2[j])
        j++
    }

    return mergedArr

}

// purposefully we have choosen array of different sizes
// console.log(merge([1, 20, 21], [15, 16, 70, 80]))

// now let us define a recursive mergeSort()

function mergeSort(arr){

    if (arr.length <= 1) return arr
    let mid = Math.floor(arr.length / 2)
    let left = mergeSort(arr.slice(0, mid))   //vvi, in slice till mid means it does not include mid right.
    let right = mergeSort(arr.slice(mid))

    return merge(left, right)

}

console.log(mergeSort([1,10,3,2,7,8,6,1]))

/* implementation using queue

function mergeSortIterative(arr) {
    if (arr.length <= 1) return arr;

    // Create a queue where each element is an array containing a single element from the original array
    let queue = arr.map(item => [item]);

    while (queue.length > 1) {
        let left = queue.shift();
        let right = queue.shift();

        queue.push(merge(left, right));
    }

    return queue[0];
}

*/