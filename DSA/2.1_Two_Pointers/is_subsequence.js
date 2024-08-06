/*
i
ahbgdc

abc
j
*/

function isSubsequence(s, t) { // non-congruent

  let count = 0
  let j = 0
  for (let i = 0; i < t.length; i++) {
    if (t[i] === s[j]) {
      count++
      j++
    }
  }

  if (count === s.length) return true
  else return false

  // or can do return (j === s.length) ? true : false
  // but (j === s.length) ? return true : return false is wrong
}

console.log(isSubsequence('abc', 'ahbgdc')); // true
isSubsequence('sing', 'sting'); // true
isSubsequence('abc', 'abracadabra'); // true
console.log(isSubsequence('abc', 'acb')); // false (order matters)

/*
Logic is keep looping on string and after each char is matched on the substring, increment count
when count === length of the substring, then a subsequence exists
*/