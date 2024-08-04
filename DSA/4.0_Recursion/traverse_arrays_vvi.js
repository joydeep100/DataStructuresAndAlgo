function collectOddValues(arr) {
    let newArr = [];

    if (arr.length === 0) {
        return newArr;
    }

    if (arr[0] % 2 !== 0) {
        newArr.push(arr[0]);
    }

    newArr = [...newArr, ...collectOddValues(arr.slice(1))];
    // newArr = newArr.concat(collectOddValues(arr.slice(1)) also works
    return newArr;
}

// console.log(collectOddValues([1, 2, 3, 4, 5]))

// Another classic problem by william fiset (sum all the odd numbers in an array)
// In this way we are also able to traverse the entire list using recursion as well

function sumOdds(i, nums) {

    if (i === nums.length) return 0
    let res = 0
    if (nums[i] % 2 === 1) {
        res = nums[i]
    }

    return res + sumOdds(i + 1, nums)
}

console.log(sumOdds(0, [2, 5, 4, 7, 3])) //mistake, i was not passing the i=0 :P

function productOfEvenNos(i, nums) {

    if (i === nums.length) return 1
    let res = 1
    if (nums[i] % 2 === 0) {
        if (nums[i] === 0){ // we know once we hit zero answer would be always zero, so better to terminate here itself!
            return 0
        }
        res = nums[i]
    }
    return res * productOfEvenNos(i + 1, nums)
}

console.log(productOfEvenNos(0, [2, 5, -4, 7, 3]))