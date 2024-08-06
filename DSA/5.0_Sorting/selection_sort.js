function selectionSort(arr){
/*
Selection sort is a simple sorting algorithm that repeatedly finds the minimum (or maximum)
element from the unsorted portion of the array and swaps it with the first unsorted element,
moving the boundary between sorted and unsorted parts one step forward until the entire array 
is sorted. 𝑂(n^2)

    i
    7, 2, 3, 10, -1, 0, 5
       j 
*/
    for(i=0; i< arr.length; i++){
        let min = i
        for (j = i+1; j < arr.length; j++){
            // mistake i was doing, if (arr[j] < arr[i])
            // it should not compare always with i=0, because if we find new min we should compare against that
            if (arr[j] < arr[min]){
                min = j
            }
        }
        [arr[i], arr[min]] = [arr[min], arr[i]]
        // arr[i], arr[min] = arr[min], arr[i] python equivalent

    }
    return arr
}

console.log(selectionSort([7,2,3,10,-1,0,5]))