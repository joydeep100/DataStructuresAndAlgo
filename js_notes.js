// Convert a atring into an array

let str1 = 'abcde'

str1.split() // first way
arr1 = [...str1] // second way

// slice

arr.slice(start_index, end_index__optional__)

// splice

array.splice(start_index, no_of_items_to_remove, new_items_to_add__optional__)

// note that there is no -1 in js
let str2 = 'hello'
// str2[0] === str2.slice(-1) would give the first and last character
// and we can also do str2.slice(0,1) to get the first character