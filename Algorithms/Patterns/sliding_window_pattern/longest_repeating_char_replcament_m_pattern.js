/* 424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
*/

/*
function maxFreq(map){ // O(26) since we have 26 Alphabets
    let max = 0
    for (let k in map){
        max = Math.max(max, map[k])
    return max 
    }
}*/

var characterReplacement = function(str, k) {
    
    let left = 0
    let right = 0
    let countCharsMap = {}
    let res = 0
    let maxFreq = 0

    while(right < str.length){

        countCharsMap[str[right]] = (countCharsMap[str[right]] || 0) + 1
        maxFreq = Math.max(maxFreq, countCharsMap[str[right]]) //like this [1]

        /* lets say the loop is somthing like this
            l
            A B A B B A
                r

            countCharsMap = {A: 2, B:1}

            so (r - l + 1) - maxFreq({A: 2, B:1}) > k
            3 - 2 > 2 (if this happens then we need to remove left most char and increment left pointer)

            basically if this condition happens we need to bring the window to valid condition
        */


        // if(((right - left + 1) - maxFreq(countCharsMap)) > k){   
        // we can know the maxFreq right so no need to compute for all 26 chars [1]
        while (((right - left + 1) - maxFreq) > k) {
            countCharsMap[str[left]] -= 1
            left++
        } 

        /* very imp pattern, run a for or a while for right till end
        then if invalid condition occurs run a while loop to make it proper

        */
        
        res = Math.max(res, right - left + 1)

        right++
    }
    return res


};

console.log(characterReplacement("ABAB", 2))