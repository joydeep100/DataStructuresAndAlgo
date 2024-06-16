/*
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
*/

function isAlphanumeric(code) {
    // digits: 48-57
    // lowercase letters: 97-122 
    // uppercase letters: 65-90 (for reference)
    return ((code >= 48 && code <= 57) || (code >= 97 && code <= 122));
}

function isPalindrome(s) {
    s = s.toLowerCase();
    let i = 0; 
    let j = s.length - 1;
    while (i < j) {
        let iCode = s.charCodeAt(i);
        let jCode = s.charCodeAt(j);

        while (!isAlphanumeric(iCode)) {
            i++;
            if (i === j) return true;
            iCode = s.charCodeAt(i);
        }
        while (!isAlphanumeric(jCode)) {
            j--;
            if (i === j) return true;
            jCode = s.charCodeAt(j);
        }

        if (iCode !== jCode) return false;
        
        i++;
        j--;
    }

    return true;
}
