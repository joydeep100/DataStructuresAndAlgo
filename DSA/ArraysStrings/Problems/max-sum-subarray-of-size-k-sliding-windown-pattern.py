# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

"""
A sub array is contiguous smaller array. for ex. arr = [100, 200, 300, 400]
sub arrays are [100], [100, 200], [100,200,300] etc
"""
def maximumSumSubarray(arr, k):
    # SLIDING WINDOW
    subarray_sum = sum(arr[:k])
    max_sum = 0
    max_sum = max(subarray_sum, max_sum)

    i, j = 0, k
    n = len(arr)

    while j < n:
        subarray_sum -= arr[i]
        i += 1
        subarray_sum += arr[j]
        j += 1

        max_sum = max(subarray_sum, max_sum)

    return max_sum

def maximumSumSubarrayOpt(arr, k):
    # now we can do this using single pointer also
    subarray_sum = sum(arr[:k])

    max_sum = 0
    max_sum = max(subarray_sum, max_sum)

    i = k
    n = len(arr)

    while i < n:
        subarray_sum -= arr[i-k]
        subarray_sum += arr[i]
        i += 1
        max_sum = max(subarray_sum, max_sum)

    return max_sum

print(maximumSumSubarray([100, 200, 300, 400], 2)) # 700
print(maximumSumSubarrayOpt([100, 200, 300, 400], 2)) # 700
