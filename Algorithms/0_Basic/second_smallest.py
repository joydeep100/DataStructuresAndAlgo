
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