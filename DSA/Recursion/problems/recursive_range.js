/*
recursiveRange
Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function 

// SAMPLE INPUT/OUTPUT
// recursiveRange(6) // 1 + 2 + 3 + 4 + 5 + 6 = 21
// recursiveRange(10) // 55 

*/

function recursiveRange(n){
   
    if (n === 1)
        return 1

    return n + recursiveRange(n-1)

}

console.log(recursiveRange(6))