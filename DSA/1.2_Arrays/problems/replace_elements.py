'''1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among
the elements to its right, and replace the last element with -1.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
'''

def replaceElementsBF(arr):

    for i in range(0, len(arr) - 1):
        arr[i] = max(arr[i + 1 :])

    arr[-1] = -1

    return arr

def replaceElements(arr):

    rightMax = -1
    for i in range(len(arr) - 1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax
        ''' Mistake

        arr[i] = rightMax
        rightMax = max(rightMax, arr[i])

        will give [-1, -1, -1, -1, -1, -1]
        '''

    return arr

print(replaceElements([17,18,5,4,6,1]))