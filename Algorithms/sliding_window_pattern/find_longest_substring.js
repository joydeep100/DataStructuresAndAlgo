function findLongestSubstring(str) {

    if (!str.length) return 0
    let i=0
    let j=1
    let arr = [...str]

    /*
      i
    r r t r m s
          j                       
    */
    let tmpDistinct = {}

    let maxLen = -Infinity

    tmpDistinct[arr[i]] = 1

    while (j < arr.length) {

        if (tmpDistinct[arr[j]] === 1) {
            // not needed to put it here, let it update at the end of each iteration 
            // maxLen = Math.max(maxLen, Object.keys(tmpDistinct).map(v => v === 1).length)            
            tmpDistinct = {}
            i++
            tmpDistinct[arr[i]] = 1
            j = i + 1
        }

        else {

            tmpDistinct[arr[j]] = 1
            j++
        }
        // mistake was in the very last iteration, if we do not add this line here
        // then the last element would be skipped
        maxLen = Math.max(maxLen, Object.keys(tmpDistinct).map(v => v === 1).length)
    }

    return maxLen

}


// findLongestSubstring('') // 0
// console.log(findLongestSubstring('rithmschool')) // 7
// console.log(findLongestSubstring('thisisawesome')) // 6
// findLongestSubstring('thecatinthehat') // 7
// findLongestSubstring('bbbbbb') // 1
// findLongestSubstring('longestsubstring') // 8
console.log(findLongestSubstring('thisishowwedoit')) // 6