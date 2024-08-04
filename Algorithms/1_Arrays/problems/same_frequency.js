function sameFrequency(m, n){

    let m_s = m.toString() 
    // mistake, missed to use let and one of the test cases failed, 
    // since the test add "use strict"; at the top
    let n_s = n.toString()

    if (m_s.length !== n_s.length) return false

    let c1 = {}
    let c2 = {}

    for (let char of m_s)
        c1[char] = (c1[char] || 0) + 1
    

    for (let char of n_s)
        c2[char] = (c2[char] || 0) + 1
    

    console.log(m_s, n_s, c1, c2)

    for(let key in c1){
        if(!(key in c2))   //mistake made was using (!key in c2) instead of (!(key in c2))
            return false
        if (c1[key] !== c2[key])
            return false
    }
    return true
}
  

console.log(sameFrequency(182,281)) // true
// sameFrequency(34,14) // false