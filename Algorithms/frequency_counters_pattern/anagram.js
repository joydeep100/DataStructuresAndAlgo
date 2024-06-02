// An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman

function validAnagram(str1, str2){

    if (str1.length !== str2.length)
        return false

    let frequencyCounter1 = {}
    let frequencyCounter2 = {}

    for(let char of str1){
        frequencyCounter1[char] = (frequencyCounter1[char] || 0) + 1
    }

    for(let char of str2){
        frequencyCounter2[char] = (frequencyCounter2[char] || 0) + 1
    }

    for(let key in frequencyCounter1){
        // this part is good to have, otherwise the code will break if key is not there in second counter
        // hasOwnProperty() can also be used alternatively
        if(!(key in frequencyCounter2))
            return false
        if(frequencyCounter2[key] !== frequencyCounter1[key])
            return false
    }
    return true
}

function validAnagramImproved(str1, str2){

    // we can also reduce one loop, so it would be 2n instead of 3n
    if (str1.length !== str2.length)
        return false

    let frequencyCounter1 = {}

    for(let char of str1){
        frequencyCounter1[char] = (frequencyCounter1[char] || 0) + 1
    }

    for(let char of str2){
        if (!frequencyCounter1.hasOwnProperty(char))
            return false
        else
            frequencyCounter1.char -= 1
    }
    return true
}


// {a: 2, z: 1}
// {z: 1, a: 2}

console.log(validAnagramImproved('aaza', 'azaa'))
// console.log(validAnagram('', 'a'))