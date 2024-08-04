function reverse(i, chars) {
    if (i < 0) return ''
    return chars[i] + reverse(i - 1, chars)

    /* o + reverse(3, chars)
       l + reverse(2, chars)       
       l + reverse(1, chars)       
       e + reverse(0, chars)         
    */
}

console.log(reverse(4, 'hello'))

// There is also another smarter way

function reverseSmart(chars) {
    /* swap the two ends of the string and repeat the same for the inner slice
    Ex. for 'hello' , o + slice('ell') + h
                      o + l + slice('l') + e + h 

    */
    const n = chars.length

    if (n <= 1) return chars  // n<=1 is required to handle even / odd cases both.
    
    const left = chars[0]
    const right = chars[n - 1] // if you must use a single line then you will have to do const [left, right] = [chars[0], chars[n - 1]];
    const subStr = chars.slice(1, n -1)
    return right + reverseSmart(subStr) + left
}

console.log(reverseSmart('dragon'))