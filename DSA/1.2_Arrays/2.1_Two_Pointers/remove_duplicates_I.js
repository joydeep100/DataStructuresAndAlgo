let removeDuplicates = function (nums) {
    /* set left = 1, right = 1 since first element is always sorted in a sorted array
    now comaprision is right === right-1 (means its duplicate), if so right++
    else it means values are diff
    now swap left and right values and increment left
                   i
   [0, 1, 1, 1, 2, 0, 2, 3, 3, 4]
                      j
    */
    let left = 1
    for (let right = 1; right < nums.length; right++) {

        if (nums[right] !== nums[right - 1]) {
            nums[left] = nums[right]
            left++
        }
    }
    return nums.slice(0,left)
};

console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) // [0, 1, 2, 3, 4]