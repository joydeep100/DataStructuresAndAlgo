function isPalindrome(str) {
    // this takes care of in 2 ways, a. when there is only one char passed
    // b. when a string of odd lenght is passed so the median char does not matter
    if (str.length === 1) return true;

    if (str.length === 2) return str[0] === str[1];

    if (str[0] === str.slice(-1)) return isPalindrome(str.slice(1, -1))

    return false;
}

console.log(isPalindrome('abba'))

// lets make this better

function isPalindrome2(str) {

    const n = str.length

    if (n <= 1) return true // handles both odd / even length strings

    if (str[0] === str[n - 1]) {
        return isPalindrome2(str.slice(1, n - 1))
    }
    return false;
}

console.log(isPalindrome2('abba'))
