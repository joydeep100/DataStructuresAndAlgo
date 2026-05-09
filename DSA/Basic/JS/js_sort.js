// sort() = method used to sort elements of an array in place.
//               Sorts elements as strings in lexicographic order, not alphabetical
//               lexicographic = (alphabet + numbers + symbols) as strings

console.log(['a', 'd', 'c', 'b'].sort())
// ['a', 'b', 'c', 'd']

console.log([1,2,3,10].sort())
// [1, 10, 2, 3] because it sorts lexicographicly and items are treated as strings

// ---------- EXAMPLE 1 ----------
const numbers = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6];

console.log(numbers.sort((a, b) => a - b)); //FORWARD
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.sort((a, b) => b - a)); //REVERSE
// [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

// ---------- EXAMPLE 2 ----------
const people = [{name: "Spongebob", age: 30, gpa: 3.0},
                {name: "Patrick", age: 37, gpa: 1.5},
                {name: "Squidward", age: 51, gpa: 2.5},
                {name: "Sandy", age: 27, gpa: 4.0}]

console.log(people.sort((a, b) => a.age - b.age)); //FORWARD
/*[
    { name: 'Sandy', age: 27, gpa: 4 },
    { name: 'Spongebob', age: 30, gpa: 3 },
    { name: 'Patrick', age: 37, gpa: 1.5 },
    { name: 'Squidward', age: 51, gpa: 2.5 }
]*/

console.log(people.sort((a, b) => b.age - a.age)); //REVERSE

/*[
    { name: 'Squidward', age: 51, gpa: 2.5 },
    { name: 'Patrick', age: 37, gpa: 1.5 },
    { name: 'Spongebob', age: 30, gpa: 3 },
    { name: 'Sandy', age: 27, gpa: 4 }
]*/