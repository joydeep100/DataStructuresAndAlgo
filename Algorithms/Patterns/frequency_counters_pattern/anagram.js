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
// {a: 2, z: 1}
// {z: 1, a: 2}

console.log(validAnagram('aaza', 'azaa'))
// console.log(validAnagram('', 'a'))