/*
https://www.youtube.com/watch?v=Q_U71D3U23M
How it works [2, 1, 9, 76, 41]

i = 1 (since start index is 1 as we made a note in the code)

now left of 1 we need to sort it (swap in case lhs > rhs)

similary for lets say 76 (now arr would have been updated to [1, 2, 9, 76, 41] )
we would need to check 76 with lhs i.e. 1,2 & 9

O(n^2) works well when array is almost sorted, best case - O(n)
*/

function insertionSort(arr) {

    // no point in starting from 0, we can very well start form 1
    for (let i = 1; i < arr.length; i++) {

        for (let j=i-1; j >= 0; j--){

            if (arr[i] < arr[j])
                [arr[i], arr[j]] = [arr[j], arr[i]]
            
            // [optimization] if we find that the last element backwards if already sorted
            // we know the arr is sorted, so we can just break
            else
                break
        }

    }

    return arr
}


console.log(insertionSort([2, 1, 9, 76, 41]))