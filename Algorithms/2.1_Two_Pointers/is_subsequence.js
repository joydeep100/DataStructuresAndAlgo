/*
i
ahbgdc

abc
j
*/

function isSubsequence(s, t) {

  let count = 0
  let j = 0
  for (let i = 0; i < t.length; i++) {
    if (t[i] === s[j]) {
      count++
      j++
    }
    // smart to put the break here like this instead of at the end
    // if (count === s.length) return true
  }

  /* but smart technique has one major flaw, imageine s="" and t=""
  then it would never enter the for loop so it is best to take the if condition out of the loop

  */
  if (count === s.length) return true
  // mistake did t.length
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