// -4 -3 -2 -1 0 1 2 3 4

function closestToZero(nums, target=0){

    let closest = Infinity
    for(let num of nums){

        if (Math.abs(target-num) < closest){
            closest = Math.abs(target-num)
        } 
    }
    return closest

}

console.log(closestToZero([-4,9])) //note we do not retain the -ve value here but we can get a general idea