/*

    Palindromes have 2 cases
                         i
    odd palindrome - a b a b a //single center

                       i i+1
    even palindrom - a b b   a //center is 2 digits or characters
        a b a b d
        l       r
        j
*/

var longestPalindrome = function (s) {

    let maxLen = 0
    let maxStr = ''

    // we are considering i as the center, and trying to expand it to the left and to the right
    for (let i = 0; i < s.length; i++) {

        // for odd substring we consider i to be center
        l = i, r = i
        while (l >= 0 && r < s.length && s[l] === s[r]) {

            if ((r - l + 1) > maxLen) {
                maxLen = (r - l + 1)
                maxStr = s.slice(l, r+1)
            }
            l--
            r++
        }

        // for even substring center would be i and i+1 right 
        // ex. 'abba' when i = 'b' and i+1 which is the second 'b' 
        l = i, r = i + 1
        while (l >= 0 && r < s.length && s[l] === s[r]) {

            if ((r - l + 1) > maxLen) {
                maxLen = (r - l + 1)
                maxStr = s.slice(l, r+1)
            }
            l--
            r++
        }

    }
    return maxStr
};


console.log(longestPalindrome('abab'))