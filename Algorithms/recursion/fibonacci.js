/*
fib
Write a recursive function called fib which accepts a number and returns the nth number
in the Fibonacci sequence. Recall that the Fibonacci sequence is the sequence of 
whole numbers 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ... which starts with 1 and 1, and where every number 
thereafter is equal to the sum of the previous two numbers.

note:- a=0 b=1 can be helpful tip for fibo series

// fib(6) // 8
// fib(7) // 13

Solution fib(n) = fib(n-1) + fib(n-2)
base condition => fib(0) = 0 & fib(1) = 1 as these are the starting point
*/

function fib(n){

    if (n < 2) // can also be put as (n === 0 || n ===1)
        return n

    // very tricky, see this satisfies the base condition
    // if fib(0) return 0 , if fib(1) return 1

    return fib(n-1) + fib(n-2)
}

console.log(fib(4))