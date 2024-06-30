const threeSumClosest = function (nums, target) {

    // same logic as 3sum but we need to check closes logic, refer how_to_find_closest_number.js
    nums = nums.sort((a, b) => a - b)

    let closest = Infinity
    // always better to declare variables which we want to return here, and not inside for / while
    // declare here, but init can be inside np

    for (let i = 0; i < nums.length - 2; i++) {

        let left = i + 1
        let right = nums.length - 1

        while (left < right) {

            let sum = nums[i] + nums[left] + nums[right]

            if (sum === target) {
                return sum
            } else if (sum > target) {
                right--
            } else {
                left++
            }

            // this part i did mistake
            if (Math.abs(target - sum) < Math.abs(target - closest)) {
                // still only part unclear is Math.abs(target - closest) and why not (Math.abs(target - sum) < closest)
                // hmm makes sense i guess, all they need is sum and closest is also a sum only right
                closest = sum;
            }
        }

    }

    return closest


};

console.log(threeSumClosest([-1, 2, 1, -4], 1))