def prefix_Suff_Sum(nums):
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

    return (pref, suff)

print(prefix_Suff_Sum([1, 7, 3, 6, 5, 6]))

def prefix_Suff_Mul(nums):
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

    return (pref, suff)

print(prefix_Suff_Mul([1, 4, 3, 6]))


