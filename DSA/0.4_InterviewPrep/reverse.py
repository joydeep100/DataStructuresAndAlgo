def reverseList(arr):
    '''Reverse a list using recursion'''
    if not arr: # handle boundary conditions
        return []
    if len(arr) == 1:
        return arr # we can also return [arr[0]] 

    return reverseList(arr[1:]) + [arr[0]] # note [arr[0]], otherwise it would be addition of list items right

# print(reverseList([]))
# print(reverseList([1]))
print(reverseList([1,2,3]))

def reverseStr(str):
    '''Reverse a list using recursion'''
    if not str: # handle boundary conditions
        return []
    if len(str) == 1:
        return str

    return str[-1] + reverseStr(str[:-1])

print(reverseStr('abc'))

def reverseListIter(arr):
    '''Reverse a list iteratively without using additional space'''

    j = 0
    for i in range(len(arr)-1,-1,-1):
        if j < i: # imp, it wont be j < len(arr)
            arr[i], arr[j] = arr[j], arr[i] # we can use tmp var as well
            j += 1
        else:
            break

    return arr

# print(reverseListIter([1,2,3,4]))
# print(reverseListIter([]))

def reverseList2p(arr):
    '''Reverse a list iteratively without using additional space, using 2 pointers'''

    left = 0
    right = len(arr) - 1

    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# print(reverseList2p([1,2,3]))
# print(reverseList2p([]))

def reverse(s):
    '''Reverse a string'''
    if not s:   # handle boundary conditions
        return ''
    if len(s) == 1:
        return s
        
    return s[-1] + reverse(s[:-1]) 
    
# print(reverse(''))
# print(reverse('a'))
# print(reverse('abcde'))
