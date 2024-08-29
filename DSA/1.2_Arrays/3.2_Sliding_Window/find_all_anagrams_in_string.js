/* 438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
*/

function eqs(map1, map2) {
    if (Object.keys(map1).length !== Object.keys(map2).length) return false;
    for (let key in map1) {
        if (map2[key] !== map1[key]) return false;
    }
    return true;
}

var findAnagrams = function(s, p) {

    if (p.length > s.length) return []

    let sMap = {}
    let pMap = {}

    let results = []

    // check if intial p items form an anagram
    for(let i=0; i < p.length ; i++){
        sMap[s[i]] = (sMap[s[i]] || 0) + 1
        pMap[p[i]] = (pMap[p[i]] || 0) + 1
    }

    results = eqs(sMap, pMap) ? [0] : []
    
    let left = 0

    // now from p + 1 (index) till end
    for(let right=p.length ; right < s.length; right++){

        // we just remove one from left, add one to right
        // (EC) now in case after removing left one we have a {a: 0} in sMap 
        // then it wont be there in ther pMap so we delete the key
        sMap[s[left]] -= 1
        if (sMap[s[left]] === 0) delete sMap[s[left]]
        left++

        sMap[s[right]] = (sMap[s[right]] || 0) + 1
        
        if (eqs(sMap, pMap)){
            results.push(left)
        }

    }
    return results
   
};

console.log(findAnagrams('baa', 'aa'))