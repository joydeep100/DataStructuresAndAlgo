def binary_search_recursive(data, target, low, high):

    if (low > high):
        return -1
    mid = (high + low)//2   # made a mistake of taking high - low
    if (target > data[mid]):  # should not be target > mid
        return binary_search_recursive(data, target, mid + 1, high)
    elif (target < data[mid]):
        return binary_search_recursive(data, target, low, mid - 1)
    else:
        return mid

# print(binary_search_recursive([1, 2, 3], 3, 0, 2))

# binary search iterative


def binary_search(arr, n):

    left = 0
    right = len(arr) - 1

    while (left <= right):

        mid = (left + right)//2  # mistake did len(arr)//2

        if n > arr[mid]:  # compare against value not index
            left = mid + 1  # see since value is greater, obiously it will be at-least one index forward right!
        elif n < arr[mid]:
            right = mid - 1
        else:
            return mid

    return -1


print(binary_search([1, 2, 3], 3))
