function findMax(nums, i, j) {

    if (i === j) return nums[i]

    const mid = Math.floor((i + j) / 2)

    return Math.max(findMax(nums, i, mid), findMax(nums, mid + 1, j))

}

function findMaxNum(nums) {
    if (nums.length === 0) return nums //this is handle passing (0-1) as j to the below function
    return findMax(nums, 0, nums.length - 1) // we are removing the 
}
console.log(findMaxNum([5, 1, 6, 2]))
