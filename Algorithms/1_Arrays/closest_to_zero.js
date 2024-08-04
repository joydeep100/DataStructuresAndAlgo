function closestToZero(nums, target=0){

    let closest = Infinity
    let closest_value

    for(let num of nums){

        if (Math.abs(target-num) < closest){
            closest = Math.abs(target-num)
            closest_value = num
        } 
    }
    return closest_value

}

console.log(closestToZero([-4,9])) // -4