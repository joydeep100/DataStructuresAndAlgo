/* 76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
*/

var minWindow = function (s, t) {

    /* what we do is

    - init left, right to 0
    - make a map of t (frequency counter), set the need variable to unique number of keys (do not take t.length) [1]

    - init a map called window_map, init have variable to 0

    - while left < right

        - start updating the window map, if the corresponding char value in t map is same, increment the have variable
          [1] because say for some char 'd' it frequency can be 2/3/4 etc

        - while (have === need)

            - firstly process the current window (store l, r) and length of the window

            - now attempt to remove the left 
            
        - increment right
    */
    // handle an edge case as per requirement
    if (!t) return ""

    let left = 0
    let right = 0

    let tMap = {}

    // construct tMap from t
    for (let i = 0; i < t.length; i++) {
        tMap[t[i]] = (tMap[t[i]] || 0) + 1
    }
    // unique keys count
    let need = Object.keys(tMap).length

    //  init required windowMap and have 
    let windowMap = {}
    let have = 0

    // needed to strore result
    let minLength = Infinity
    let minLengthPointers = [-1, -1]

    while (right < s.length) {

        // keep updating the window
        windowMap[s[right]] = (windowMap[s[right]] || 0) + 1
        // if value of a char exists in tMap and now its exactly same sam s[right] we know that one char (with req. freq.)
        // has been found

        if (s[right] in tMap && windowMap[s[right]] === tMap[s[right]]) {
            have++
        }

        // till this condition is met, attempt to shrik the window

        // note - usually if it a min problem, we try to check (while - valid) condition we try to optimize, 
        // if it a max problem we usually try (while - invalid) condition, kept incrementing left & try to make it valid condition
        
        // vvi : while the right pointer is fixed
        while (have === need) {
            
            // first process the current window
            if (right - left + 1 < minLength) {
                minLength = right - left + 1
                minLengthPointers = [left, right]
            }

            // if the left char is a useful char (this part is optional right)
            if (s[left] in tMap){
                windowMap[s[left]] -= 1

                /*this is where i did the mistake. did not consider this condition!
                The condition to reduce have when the left pointer moves should only decrement have 
                if windowMap[s[left]] becomes less than tMap[s[left]].
                */
                
                if (windowMap[s[left]] < tMap[s[left]]) {
                    have--;
                }
            }
            // this step is mandatory
            left++
        }
        right++
    }
    return minLength !== Infinity ? s.slice(minLengthPointers[0], minLengthPointers[1]+1) : ""

};

console.log(minWindow("ADOBECODEBANC", "ABC"))

/* the two while loop do make this into O(n^2) because

Each character in s is processed at most twice:
    Once by the right pointer (when expanding the window).
    Once by the left pointer (when shrinking the window).

it is still O(n) which is linear time
*/