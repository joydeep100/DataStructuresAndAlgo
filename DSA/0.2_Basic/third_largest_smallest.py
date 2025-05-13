def third_largest(nums):
    """
    Time complexity:
    O(n) - to convert list into set 
    O(nlogn) - to sort
    Overall - nlogn

    Space - 
    O(n) - to convert into set
    O(n) - store sorted items
    Overall - O(2n)

    will be a problem when data is huge.
    """
    return sorted(set(nums))[-3]

def third_largest_iter(nums):
    first = second = third = float('-inf') #another way
    for num in nums:
        if num in (first, second, third):
            continue
        if num > first:
            first, second, third = num, first, second
        elif num > second:
            second, third = num, second
        elif num > third:
            third = num
    return third if third != float('-inf') else None

print(third_largest([4, 1, 7, 2, 9, 7]))  # Output: 4
print(third_largest_iter([4, 1, 7, 2, 9, 7]))  # Output: 4

def third_smallest_iter(nums):
    first = second = third = float('inf')
    for num in nums:
        if num in (first, second, third):
            continue
        if num < first:
            first, second, third = num, first, second
        elif num < second:
            second, third = num, second
        elif num < third:
            third = num
    return third if third != float('inf') else None

print(third_smallest_iter([4, 1, 7, 2, 9, 7]))  # Output: 4