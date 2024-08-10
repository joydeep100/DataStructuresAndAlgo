def slarge(list):

    if len(list) < 1: return -1

    largest, s_largest = float('-inf'), float('-inf')

    for number in list:

        if number > largest:
            s_largest = largest
            largest = number
        elif number > s_largest and number < largest:
            s_largest = number

    return s_largest if s_largest != float('-inf') else -1

print(slarge([1,2,3,4,-1]))

def sec_smallest(list):

    smallest = float('inf')
    sec_smallest = float('inf')

    for number in list:

        if number < smallest:
            sec_smallest = smallest
            smallest = number
        elif number < sec_smallest and number > smallest:
            sec_smallest = number

    return sec_smallest if smallest != float('inf') else -1

print(sec_smallest([1,2,3,4,-1]))