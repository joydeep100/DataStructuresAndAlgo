from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        count = 0

        for r in range(n):
            for c in range(n):

                # print(grid[i][j])
                match = True
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break

                if match:
                    count += 1
                    # print(grid[r][i], grid[i][c])

        return count

grid = [[3,2,1],[1,7,6],[2,7,7]]
res = Solution()
print(res.equalPairs(grid))