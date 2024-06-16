/*
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

IMP - This can be done using O(m + n) using the KMP Algo, but it is complex and not worth.
It also will use space complexity O(m) instead of O(1) in case we go with below solution
*/

/**
    i
    sasbutsad
    sad
    j

 */
var strStr = function (haystack, needle) {

    if (!needle) return 0

    for (let i = 0; i < haystack.length - needle.length + 1; i++) {
        // i < haystack.length - needle.length + 1 because checking last part smaller than the needle is not required

        for (let j = 0; j < needle.length; j++) {
            // it should be i + j
            if (haystack[i + j] !== needle[j]) break
            if (j === needle.length - 1) return i
        }
    }
    return -1

}


var strStrFake = function (haystack, needle) {
    let j = 0;
    for (let i = 0; i < haystack.length; i++) {
        if (haystack[i] !== needle[j]) {
            // IMP Although this looks O(n) it is not it it still O(n * m), where n  and m are size of haystack and needle)
            // because of the line below
            i = i - j;
            j = 0;
        }
        else if (j === needle.length - 1) {
            return i - j;
        }
        else {
            j++;
        }
    }
    return -1;
};

strStr('sadbutsad', 'sad')