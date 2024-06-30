var findAllTriplets = function(nums) {
    let res = [];

    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                res.push([nums[i], nums[j], nums[k]]);
            }
        }
    }

    return res;
};

// Example usage
const nums = [-1, 0, 1, 2, -1, -4];
console.log(findAllTriplets(nums));
// Output: [
//   [-1, 0, 1],
//   [-1, 0, 2],
//   [-1, 0, -1],
//   [-1, 0, -4],
//   [-1, 1, 2],
//   [-1, 1, -1],
//   [-1, 1, -4],
//   [-1, 2, -1],
//   [-1, 2, -4],
//   [-1, -1, -4],
//   [0, 1, 2],
//   [0, 1, -1],
//   [0, 1, -4],
//   [0, 2, -1],
//   [0, 2, -4],
//   [0, -1, -4],
//   [1, 2, -1],
//   [1, 2, -4],
//   [1, -1, -4],
//   [2, -1, -4]
// ]
