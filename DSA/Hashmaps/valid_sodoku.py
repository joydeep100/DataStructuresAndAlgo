"""36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according 
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''
        https://www.youtube.com/watch?v=JFvG_VGZrGU

        to find which grid a num belongs based on i and j

        grid_index = (i//3) * 3 + (j // 3)
        '''

        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)] 
        grid = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                grid_index = (i // 3) * 3 + (j // 3)
                if num in rows[i] or num in cols[j] or num in grid[grid_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                grid[grid_index].add(num)
        
        return True
        