function secondLargest(arr){

    if (arr.length < 2) return -1

    let largest = -Infinity
    let secondLargest = -Infinity

    for(item of arr){
        if (item > largest){
            secondLargest = largest
            largest = item
        } else if (item > secondLargest && item < largest){
            secondLargest = item
        }
    }

    return secondLargest != -Infinity ? secondLargest : -1
}

console.log(secondLargest([9,9]))