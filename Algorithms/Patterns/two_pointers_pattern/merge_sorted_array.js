/*
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

            <-
p1          i              p2
[4,0,0,0,0,0], 1, [1,2,3,5,6], 5
*/

var merge = function(nums1, m, nums2, n) {

    let i = nums1.length - 1
    let p1 = m - 1
    let p2 = n - 1 
    while(p2 >= 0){

        if(p1 >= 0 && nums1[p1] > nums2[p2]){
            // so p1 >= 0 is just to avoid a special condition
            // code works perfectly well even without that
            // but if we put this condition in the while (p1 >=0 && p2 >= 0) it completely messes up the logic


            nums1[i--] = nums1[p1--] // we can also do like this--, post decrement
            // p1--
            
        } else {
            nums1[i--] = nums2[p2--]   
            // p2--
        }
        // i--
    }

    return nums1

}

// console.log(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
// console.log(merge([0], 0, [1], 1)) // good test case
console.log(merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)) // amazing test case

