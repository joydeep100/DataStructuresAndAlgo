function SecondLargest(arr){

    if (arr.length < 2) return -1

    let largest = -Infinity
    let SecondLargest = -Infinity

    for(item of arr){
        if (item > largest){
            SecondLargest = largest
            largest = item
        }
    }

    return SecondLargest
}

console.log(SecondLargest([1,2,3,4,5]))