def prefixSum(nums):
    length = len(nums)

    pref, suff = [0] * length, [0] * length

    prev = 0
    for i in range(length):
        pref[i] = nums[i] + prev
        prev += nums[i]

    prev = 0
    for i in range(length-1, -1, -1):
        suff[i] = nums[i] + prev
        prev += nums[i]

    return nums, pref, suff

print(prefixSum([1, 7, 3, 6, 5, 6]))

def prefixMul(nums):
    length = len(nums)

    pref, suff = [0] * length, [0] * length

    prev = 1
    for i in range(length):
        pref[i] = nums[i] * prev
        prev *= nums[i]

    prev = 1
    for i in range(length-1, -1, -1):
        suff[i] = nums[i] * prev
        prev *= nums[i]

    return nums, pref, suff

print(prefixMul([1, 4, 3, 6]))


