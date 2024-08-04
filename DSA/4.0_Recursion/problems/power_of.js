/* power
Write a function called power which accepts a base and an exponent. 
The function should return the power of the base to the exponent. 
This function should mimic the functionality of Math.pow()  - do not 
worry about negative bases and exponents.
*/

function power(base, exponent){
    
    if (exponent === 0)
        return 1
    // i did,  exponent === 1 return base which i guess failed some test case
    // so remember exit condition need not always be === 1

    return base * power(base, exponent-1)
}

console.log(power(2,4)) // o/p 16

