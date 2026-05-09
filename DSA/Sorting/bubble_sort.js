/* From left to right, in each iteration compare first 2 elements (if not sorted, swap them)
we need to repeat this process for n times.


*/

function bubbleSort(arr) {

    for (i = 0; i < arr.length; i++) {
        // this loop is just for the no of times (passes) we need to loop over 
        
        let swapped = false // [2]
        
                                   // [1]
        for (j = 0; j < arr.length -1; j++) {
            // we need to swap in this loop, hence we use j / j+1 to compare and not i

            // mistake, i was comparing for i=0 and for j=1, so what will happen is 
            // when we swap the values, i will still be pointing to swapped value and it messes up

            // [1 mandatory optimization] we can see that in each pass the rightmost item is the largest one
            // also when j === last item, then j+1 will be undefined (out of bouds)
            // so we must loop j only till arr.length - 1

            // [2 optional optimization]
            // when the array is nearly sorted say [8,1,2,3,4,5,6,7]
            // then in first pass only the entire array is sorted, rest of passes are unnecessary
            // so we can add that check as well ***
    
            if (arr[j] > arr[j+1]) {
                // to avoid confusion, take first one as tmp
                // then immidiately changes the first literal's value
                let tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swapped = true // [2] 
            }
        }
        if (!swapped) return arr
    }
    return arr
}

console.log(bubbleSort([37, 45, 29, 8, 2, 2]))

/*
Big O

Best case with optimization = O(n) lets say it was a nearly sorted array and it was done in a few passes so 5n = n
Worst case = O(n^2)
*/