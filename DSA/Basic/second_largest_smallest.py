def sec_largest(list):

    if len(list) < 1: return -1

    largest, s_largest = float('-inf'), float('-inf')

    for number in list:

        if number > largest:
            s_largest = largest
            largest = number
        elif number > s_largest and number < largest:
            s_largest = number

    return s_largest if s_largest != float('-inf') else -1

print(sec_largest([1,2,3,4,-1]))

def sec_smallest(list):

    smallest, sec_smallest = float('inf'), float('inf')

    for number in list:

        if number < smallest:
            sec_smallest = smallest
            smallest = number
        elif number < sec_smallest and number > smallest:
            sec_smallest = number

    return sec_smallest if smallest != float('inf') else -1

print(sec_smallest([1,2,3,4,-1]))


def third_largest_iter(nums):
    if len(nums) < 3:
        return None

    first = second = third = float('-inf')
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


def third_smallest_iter(nums):
    if len(nums) < 3:
        return None

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


print(third_largest_iter([4, 1, 7, 2, 9, 7]))   # 4
print(third_smallest_iter([4, 1, 7, 2, 9, 7]))  # 4


# Using set + sort - O(n log n) time, O(n) space
def third_largest_set(nums):
    unique = sorted(set(nums))
    return unique[-3] if len(unique) >= 3 else None


def third_smallest_set(nums):
    unique = sorted(set(nums))
    return unique[2] if len(unique) >= 3 else None


print(third_largest_set([4, 1, 7, 2, 9, 7]))   # 4
print(third_smallest_set([4, 1, 7, 2, 9, 7]))  # 4