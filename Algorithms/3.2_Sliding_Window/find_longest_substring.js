/*
3. Longest Substring ***Without Repeating*** Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

https://www.youtube.com/watch?v=GS9TyovoU4c // best, check the optimum solution. great video!
*/

function lengthOfLongestSubstringBF(str) {

    // Brute force solution
    let tmpArr
    let maxLen = 0
    /* let i = each char, and j will be all possible substrings from i'th char
    we just use a simple list, to check if char is already in it. when we find a duplicate char we just simply break if not
    because when we get to lets say 'abca'bcbb we break, dont worry about rhs part it will anyways get covered as i moves rightIndex in subsequent iterations
    */
    for (let i = 0; i < str.length; i++) {

        tmpArr = []

        for (let j = i; j < str.length; j++) {

            if (tmpArr.indexOf(str[j]) === -1) {
                tmpArr.push(str[j])
            } else break
        }
        maxLen = Math.max(maxLen, tmpArr.length)
    }

    return maxLen

}

function lengthOfLongestSubstring(str) {

    // optimum solution
    /*    l
        a b c a b c b b
              r
    */

    let leftIndex = 0
    let rightIndex = 0
    let tmpMap = {}
    let maxLen = 0

    // O(hasOwnProperty) = 1 
    // ways to look up Obj. Obj.hasOwnProperty() / 'key1' in obj / Object.keys(obj).includes('key1')

    while (rightIndex < str.length) {

        let currentChar = str[rightIndex]
        if (tmpMap.hasOwnProperty(currentChar) && tmpMap[currentChar] >= leftIndex){
            // it means we do have a repeating character and the repeating character is within the current window that we are looking
            // tmpMap[currentChar] >= leftIndex because we want to ignore the part before leffIndex which we have left out
            
            // leftIndex should be next index where we had seen the char, other approach would have been to loop until we make sure 
            // the Map is valid, but this is a better approach
            leftIndex = tmpMap[currentChar] + 1

            // we also need to update the index of the charcter with the current index
            tmpMap[currentChar] = rightIndex
        }

        maxLen = Math.max(maxLen, rightIndex - leftIndex +1)
        tmpMap[str[rightIndex]] = rightIndex  // since we are using Object and not Map.
        rightIndex++

    }

    return maxLen

}



// lengthOfLongestSubstring('') // 0
// console.log(lengthOfLongestSubstring('rithmschool')) // 7
// console.log(lengthOfLongestSubstring('thisisawesome')) // 6
// lengthOfLongestSubstring('thecatinthehat') // 7
// lengthOfLongestSubstring('bbbbbb') // 1
// lengthOfLongestSubstring('longestsubstring') // 8
console.log(lengthOfLongestSubstring('thisishowwedoit')) // 6
// console.log(lengthOfLongestSubstring(' ')) // 1 this test case failed in leet code