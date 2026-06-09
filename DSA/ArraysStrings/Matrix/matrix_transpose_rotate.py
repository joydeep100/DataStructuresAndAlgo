matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix)
"""
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
"""

m = len(matrix)
n = len(matrix[0]) # standard way

"""
Transpose of a matrix (ros becomes cols and vice versa)
"""
for i in range(m):
    for j in range(i+1, m):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
"""
[
[1, 5, 9, 13], 
[2, 6, 10, 14], 
[3, 7, 11, 15], 
[4, 8, 12, 16]]
"""

"""
Now to rotate 90 degrees we can just see to reverse aroound the center
"""

for i in range(m):
    matrix[i].reverse()   # because this is inplace right

""" now if reverse() is not allowed we can do manually as well
for i in range(m):
    for j in range(m//2):
        matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
    
just need to figure out indexes for one index, say (0,0)
"""

print(matrix)

