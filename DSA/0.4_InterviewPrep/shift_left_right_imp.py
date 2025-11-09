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

def shit_right_multiple(input_arr, *shift_values):
    
    right = len(input_arr) - 1
    
    for shift_val in shift_values:
        
        left = 0 # because some items will be swapped on to left
        
        while left  <= right:
            
            if input_arr[right] == shift_val:
                right -= 1
            elif input_arr[left] != shift_val:
                left += 1
            else:
                # swap the values
                input_arr[left], input_arr[right] = input_arr[right], input_arr[left]
                left += 1
                right -= 1

    return input_arr
    
print(shit_right_multiple([0,1,1,0,3,4,5], 1, 0))
print(shit_right_multiple([3,0,1,1,0,3,4,5], 1, 0, 3))
print(shit_right_multiple([9,0,1,1,0,3,4,5,9], 1, 9, 3))