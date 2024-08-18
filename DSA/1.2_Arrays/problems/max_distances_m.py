''' 624. Maximum Distance in Arrays
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and 
calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first 
or third array and pick 5 in the second array. '''

def maxDistance(arrays):

    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    res = 0

    for i in range(1, len(arrays)):

        curr_max = arrays[i][-1]
        curr_min = arrays[i][0]

        # it is also possible that max diff is in reverse way, i.e. max_val - curr_min
        # just imagine 2 sub-arrays for easier understanding
        res = max(res, curr_max - min_val, max_val - curr_min)

        max_val = max(max_val, curr_max)
        min_val = min(min_val, curr_min)

    return res

print(maxDistance([[1,2,3],[4,5],[1,2,3]])) #4
print(maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]])) #14
print(maxDistance([[1,4],[0,5]])) #4