function findMax(i, nums, max=-Infinity){

    // we can go either from 0 to n-1 or reverse, going from 0 - n is better if possible.
    const n = nums.length

    if (i === n) return max
    max = Math.max(max, nums[i])

    return findMax(i+1, nums, max) //see, we need to keep referencing max as well
}

// console.log(findMax(0,[2,1,3,-4,2]))

// we also need to keep track of maxIndex,
// we can also create helper method to reduce setting of max=-Infinity, maxIndex = -1 in the main function
function findMaxI(i, nums, max=-Infinity, maxIndex = -1){ // [1]

    // let  max=-Infinity, maxIndex = -1 if we use it like this it wont work, but have to use like [1]
    // we can go either from 0 to n-1 or reverse, going from 0 - n is better if possible.
    const n = nums.length

    if (i === n) return [max, maxIndex]
    if (nums[i] > max){
        max = nums[i]
        maxIndex = i
    }

    return findMaxI(i+1, nums, max, maxIndex) //see, we need to keep referencing max as well
}

// console.log(findMaxI(0,[2,1,3,-4,2]))

//try using a helper function as shown by william fiset using a helper function
function findMaximumElement(nums){
    return findMaxFiset(0, nums)
}

function findMaxFiset(i, nums){
    if (i === nums.length)
        return [null, null]

    let [bestMax, bestIndex] = findMaxFiset(i+1, nums)

    if (bestMax === null || nums[i] > bestMax){ 
        // when bestMax is null i.e. we are checking i = n-1 case

        // also works without bestMax === null part, i think this is to handle edges cases
        bestMax = nums[i]
        bestIndex = i
    }

    return [bestMax, bestIndex]
    /* call stack
    i   best max, best index  ...
    0   2, 0 
    1   2, 0
    2   3, 2
    3   3, 2
    4   3, 2
    5   null, null 
    here the magic is in the reverse order, first it would go till i=n and once it hits null
    it would compute max in the reverse order
    */
}

console.log(findMaximumElement([2,1,3,-4,2]))

