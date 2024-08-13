'''
 l
[1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6
 r

 left moves when r == 1  

    l
[1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6
    r   

    l
[1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6
       ......r 

       l
[1, 1, 3, 2, 2, 1, 3, 2, 4, 5, 6
        ........r 
'''
def shiftLeft(arr):
    '''Shift all ones left'''
    left = 0
    right = 0
    length = len(arr)

    while right < length:
        if arr[right] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        right += 1

    return arr

def shiftRight(arr):
    '''Shift all ones to Right'''
    length = len(arr)
    i = length - 1
    j = length - 1

    while j >= 0:
        if arr[j] == 1:
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1
        j -= 1

    return arr

print(shiftLeft([1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6]))
print(shiftRight([1, 2, 3, 2, 1, 1, 3, 2, 4, 5, 6]))
