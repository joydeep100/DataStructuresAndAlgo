var isPowerOfTwo = function (n) {
    if (n === 1) return true
    if (n <= 0) return false // chatGpt points that we need to hanle -ve nos as they cannot power up to 2
    if (n % 2 !== 0) return false

    return isPowerOfTwo(Math.floor(n / 2))
};

console.log(isPowerOfTwo(-12))


// This code is more readable!!
var isPowerOfTwoR = function (n) {
    if (n === 1) return true
    if (n <= 0) return false

    return ((n % 2 === 0) && isPowerOfTwoR(Math.floor(n / 2)))
}

console.log(isPowerOfTwoR(-12))

/* 8 
    8 / 2 = 4  |   9 / 2 = 4.5 is out of question | 10 / 2 = 5 
    4 / 2 = 2  |                                  |  5 / 2
    2 / 2 = 1  |                                  |

    12
    12/2 = 6
    6/2 = 3

    2 % 2 = 0

    i. first condition is n % k === 0 should be true
    ii. or we saw that at any point if n%k !== 0 then it cant be power
    iii. and we saw that for valid powers the end state is n reduces to 1 (like 8, but lets consider 12, 12/2=6 , 6/2=3 !!)

*/

// now lets try isPowerOfThree()

function isPowerOfThree(n) {

    if (n === 1) return true
    if (n <= 0) return false
    if (n % 3 !== 0) return false

    return isPowerOfThree(Math.floor(n / 3))
}

console.log(isPowerOfThree(12))

// now lets try power of k

// now lets try isPowerOfThree()

function isPowerOfK(n, k) {

    if (n === 1) return true
    if (n <= 0) return false
    if (n % k !== 0) return false

    return isPowerOfK(Math.floor(n / k), k)
}

console.log(isPowerOfK(16, 4))

// now lets do a medium problem
// https://leetcode.com/problems/powx-n/description/

var myPow = function (x, n) {

    if (n <= 1) {
        return x
    }

    return x * myPow(x, n - 1)
};

console.log(myPow(2, 3))

/*

2^3 = 2*2*2

2 * myPow(2,2)
2 * 2 * myPow(2,1)

so my solution works for n (+ve values) but fails when n is -ve like 2^-2 = 0.25 instead of
*/

var myPow2 = function (x, n) {
    if (n === 0) return 1
    if (n > 0) {
        if (n === 1) {
            return x
        }
        return x * myPow2(x, n - 1)
    } else {
        if (n === -1) { // should be -1
            return 1 / x
        }
        return (1 / x * myPow2(x, n + 1))
    }
};

console.log(myPow2(2, -2))

/* the above code worked for 200+ test cases but eventually failed with stackoverflow error
it fails for the following testcase where x=0.00001 and n=2147483647 (dealing with large exponents, 
the recursive approach with repeated multiplication can result in a stack overflow or significant performance issues)
below is chatGpt code with fixes, which is lil beyond my league :P:P */

var myPow3 = function (x, n) {
    if (n === 0) return 1;  // Base case: x^0 is always 1

    if (n < 0) {
        x = 1 / x;
        n = -n;
    }

    if (n === 1) return x;  // Base case for positive exponent

    // Exponentiation by squaring
    if (n % 2 === 0) {
        // If n is even, we use the property (x^2)^(n/2)
        return myPow3(x * x, n / 2);
    } else {
        // If n is odd, we use the property x * x^(n-1)
        return x * myPow3(x * x, (n - 1) / 2);
    }
};

// console.log(myPow3(2,-2))