# 2d arrays shold not be created like this
arr = [[0] * 2] * 4
print(arr) # [[0, 0], [0, 0], [0, 0], [0, 0]]

# because of shallow copy problem
arr[0][0] = 1
print(arr) # [[1, 0], [1, 0], [1, 0], [1, 0]]

# this is the correct way to initiaize 2d array
arr2 =  [[0] * 2 for i in range(4)]
print(arr2) # [[0, 0], [0, 0], [0, 0], [0, 0]]

# Array Concatenation
print([0] + [1]) # [0, 1]