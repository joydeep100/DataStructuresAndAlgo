* need not be sorted

So sliding window works in something like this, like to slide a window

[1,3,2,5,77,6,7,8,9,9,1]  // let us say we want maxSubArraySum of size 4

so we need to slide through the entire array once to make it O(n)

so to start, we would take the sum of starting 4 items [1,3,2,5]

now the magic is lets remove 1 and add 77, keep it in some variable called maxSum.

and once the slide through happens, we would have the highest value in maxSum

