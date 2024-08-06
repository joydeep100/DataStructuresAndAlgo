def binary_search_recursive(data, target, low, high):

    if (low > high):
        return -1
    mid = (high + low)//2   # made a mistake of taking high - low
    if (target > data[mid]):  # should not be target > mid
        return binary_search_recursive(data, target, mid+1, high)
    elif (target < data[mid]):
        return binary_search_recursive(data, target, 0, mid)
    else:
        return mid

# binary search iterative


def binary_search(arr, n):

    left = 0
    right = len(arr) - 1

    while (left <= right):

        mid = (left + right)//2  # mistake did len(arr)//2

        if n > arr[mid]:
            left = mid + 1  # just one side we need to update
        elif n < arr[mid]:
            right = mid
        else:
            return mid

    return -1


print(binary_search([1, 2, 3], 3))
