/* 
Find the longest subarray where sum <= k
*/

function longest(arr, k) {
    let left = 0;
    let right = 0;
    let maxLen = 0;
    let sum = 0;

    while (right < arr.length) {
        sum += arr[right];

        // Shrink the window from the left if the sum exceeds k
        while (sum > k && left <= right) {
            sum -= arr[left];
            left++;
        }

        // Update maxLen if the current window sum is less than or equal to k
        if (sum <= k) {
            maxLen = Math.max(maxLen, right - left + 1);
        }

        // Move right pointer to the next position
        right++;
    }

    return maxLen;
}


console.log(longest([2, 3, 1, 22, 100, 2, 10], 14))