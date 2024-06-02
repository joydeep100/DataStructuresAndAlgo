function isPalindrome(str){
    
    // this takes care of in 2 ways, a. when there is only one char passed
    // b. when a string of odd lenght is passed so the median char does not matter
    if(str.length === 1) return true;

    if(str.length === 2) return str[0] === str[1];

    if(str[0] === str.slice(-1)) return isPalindrome(str.slice(1,-1))
        
    return false;
}


console.log(isPalindrome('awesome')) // false
// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true
// isPalindrome('amanaplanacanalpanama') // true
// isPalindrome('amanaplanacanalpandemonium') // false
