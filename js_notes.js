// Convert a atring into an array

let str1 = 'abcde'

str1.split() // first way
arr1 = [...str1] // second way

// slice

arr.slice(start_index, end_index__optional__)
'ababa'.slice(0,5) // would give 'ababa', same as a python slice.
// remember array methods also mostly work on string as well like indexing etc

// splice

array.splice(start_index, no_of_items_to_remove, new_items_to_add__optional__)

// note that there is no -1 in js
let str2 = 'hello'
// str2[0] === str2.slice(-1) would give the first and last character
// and we can also do str2.slice(0,1) to get the first character

// Array swap (only - *dont use for variable swap*) [a,b] = [b,a] or use the above thing
[nums1[i], nums2[j]] = [nums2[j], nums1[i]]

function isAlphanumeric(code) {
    // digits: 48-57
    // lowercase letters: 97-122 
    return ((code >= 48 && code <= 57) || (code >= 97 && code <= 122)) 
}

// to get length of an object
const obj = { a: 1, b: 2, c: 3 };
const length = Object.keys(obj).length;
console.log(length); // Output: 3
