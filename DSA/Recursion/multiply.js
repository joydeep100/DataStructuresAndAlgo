function mul(a, b) {

    /*   
       Complexity is O(n) / O(n) for worst case
       and O(1) / O(1) for the best case
   */

    if (a === 0) return 0
    return mul(a-1, b) + b // we could also do (a, b-1) + a  which is initially did but think what would happen if we did 1000*3 ?
}

// console.log(mul(3, 4))

// now we need to update the method to be able to handle negative numbers as well so that mul(5, -6) = -30 and mul(-2,-5) = 10
// Naive way
function mulNegHlpr(a, b) {
    if (b === 0) return 0
    return a + mulNegHlpr(a, b - 1)
}

function mulNeg(a, b) {
    const res = mulNegHlpr(Math.abs(a), Math.abs(b))
    if (a < 0 && b < 0)
        return res //never forget the returns
    else if (a < 0 || b < 0)
        return -1 * res //never forget the returns
    else
        return res
}

// console.log(mulNeg(5, -6))

// optimized solution - my attempt
function mulNegOpt(a, b) {

    if (b === 0) return 0 //since we are decrmenting always the b-part

    // lets assure a < 0, only a is negative (-5, 6)
    if (a < 0 && b > 0) return a + mulNegOpt(a, b - 1)

    // lets assure a < 0, only a is negative (5, -6)
    if (b < 0 && a > 0) return b + mulNegOpt(b, a - 1)

    // when both a and b are negative (-5, -2)
    if (a < 0 && b < 0) return b + mulNegOpt(b, a + 1) // but there is a bug, we are still getting -10 as result for (-5, -2)

    /* 
    -5 + mulNegOpt(-5, -1)
    -5 + mulNegOpt(-5, 0)
    */
}
console.log(mulNegOpt(-5, -2)) // also think of (-5, 6)

// lets try to fix the bug, below is a working solution

function mulNegOpt2(a, b) {
    /*
    possiblities are -5, 2 / 5, -2 / -5, -2

    so the key is if you swap a / b, then you will run into problems
    */
    if (a === 0) return 0 

    if (a < 0) return mulNegOpt2(a + 1, b) - b // [1]

    else return mulNegOpt2(a - 1, b) + b // [2]

    /* walk thru both negative case (-5, -2) which will take path [1]
    
    -2 + mul(-4, -2)
    -2 + mul(-3, -2)
    -2 + mul(-2, -2)
    -2 + mul(-1, -2)
    -2 + mul(0, -2)
    */
}
console.log(mulNegOpt2(-5, -2))