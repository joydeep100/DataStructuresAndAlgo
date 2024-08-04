// ARRAYS
let arr = [1, 2, 3]

// add from end O(1)
arr.push(4)
// remove from end O(1)
arr.pop(4)

// add from beginning O(n)
arr.unshift(1)
// remove from beginning O(n)
arr.shift(1)

console.log(arr)
// [1,2,3]

//*** IMP ***/
[1, 2, 3, 4, 5].slice(-1) // gives us [5]
arr[arr.length - 1];  // This gives you '5' directly, not '[5]'


// SLICE (start_index, end_index (optional))
console.log(arr.slice(0, 1))
console.log(arr.slice(0)) // prints full array

// SPLICE (start_index, no of items to remove at index, no of item/s to add at index)
console.log(['a', 'b', 'c'].splice(0, 1, 99, 100))
// will return the deleted items, 'a' and at index 0, would add 99 & 100 [99, 100, 'b', 'c']

/* 
STACKS AND QUEUES
STACK - We can simulate stack using push / pop or unshift / shift to achieve LIFO.
notice that using unshift / shift will make this very inefficient.

QUEUE - We can simulate queue using push / shift to achieve FIFO.
or we can also do unshit / pop for the other way around.
*/ 