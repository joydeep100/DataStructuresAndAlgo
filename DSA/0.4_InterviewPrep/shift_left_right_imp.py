def shiftLeft(arr):
    '''Shift all ones left'''
    left = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    return arr

def shiftRight(arr):
    '''Shift all ones to Right'''
    l = len(arr)
    right = l - 1

    for i in range(right, -1, -1):
        if arr[i] == 1:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1

    return arr

print(shiftLeft([1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6]))
print(shiftRight([1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6]))
