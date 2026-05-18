matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

"""
Matrix index positions:

[
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)]
]
"""

rows = len(matrix) # remember no -1
cols = len(matrix[0])

for i in range(rows * cols):
    r = i // cols
    c = i % cols

    print(
        f"i={i} -> matrix[{r}][{c}] = {matrix[r][c]}"
    )

''' Output, so idea is if you consider i as a flattened array then for each i 
we can compute both the coordinates using 

r = i // cols
c = i % cols

i=0 -> matrix[0][0] = 1
i=1 -> matrix[0][1] = 2
i=2 -> matrix[0][2] = 3
i=3 -> matrix[1][0] = 4
i=4 -> matrix[1][1] = 5
i=5 -> matrix[1][2] = 6
i=6 -> matrix[2][0] = 7
i=7 -> matrix[2][1] = 8
i=8 -> matrix[2][2] = 9
'''