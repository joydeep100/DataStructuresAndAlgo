def closest_to_zero(arr):

    closest = float('inf')
    closest_idx = -1

    for i in range(len(arr)):

        computed_closest =  abs(arr[i] - 0) # can also be abs(arr[i]) 

        if computed_closest < closest:
            closest = computed_closest
            closest_idx = i

    return arr[closest_idx]

print(closest_to_zero([-10, -10, 11, 9, -8]))