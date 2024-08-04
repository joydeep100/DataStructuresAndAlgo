/* s = String, m = len of s
   p = Pattern, n = len of p
*/
function strStrP1(s, m, p, n) {

    // my first solution
    for (let i = 0; i <= m - n; i++) {
        // (i <= m - n) === (i < m -n +1)

        count = 0
        for (let j = 0; j < n; j++) {
            if (s[i + j] === p[j]) {
                count++
            }
        }
        if (count === n) return i
    }

    return -1

}

function strStr(s, m, p, n) {

    for (let i = 0; i < m - n + 1; i++) {
        // O(m - n + 1) 

        let j = 0 // here we can learn how to use a while loop for condition checking
        while (j < n && p[j] === s[i + j]) {
            j++
            // O(n)
        }

        if (j === n) return i
    }

    return -1
    // O((m-n+1) * n) = O (m*n) = O(n^2)
}


console.log(strStr('aabcde', 6, 'cd', 2)) // 3

// for string match O (m*n) is good enough
// Algorithms/Patterns/two_pointers_pattern/find_index_of_first_occurance.js can also be referred
// if we want it to be O(m + n) then we can look at the complex KMP algorithm

