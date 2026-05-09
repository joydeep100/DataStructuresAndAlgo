/* https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
           columns
         0  1  2  3
        ----------- 
      0 | 9  9  8  1 
rows  1 | 5  6  2  6
      2 | 8  2  6  4 
      3 | 6  2  2  2
*/

function findLargestInSubGrid(grid, row, col, row_start = 0, col_start = 0) {
    let largest = -Infinity
    for (let i = row_start; i < row; i++) {
        for (let j = col_start; j < col; j++) {
            // console.log(grid[i][j])
            if (grid[i][j] > largest) largest = grid[i][j]
        }
    }
    return largest  
}

// console.log(findLargestInSubGrid(grid, 3, 3, 0, 0)) // prints top left 3*3 grid and return's the largest in that grid
// console.log(findLargestInSubGrid(grid, 3, 4, 0, 1)) // prints top right                   ''
// console.log(findLargestInSubGrid(grid, 4, 3, 1, 0)) // prints bottom left                 ''
// console.log(findLargestInSubGrid(grid, 4, 4, 1, 1)) // prints bottom left                 ''

var largestLocal = function (grid) {
    const subMatSize = 3 // constant, given in problem
    const resMatSize = grid.length - 2
    let res = []

    for (let i = 0; i < resMatSize; i++) {
        const resRow = []
        for (let j = 0; j < resMatSize; j++) {
            const ans = findLargestInSubGrid(grid, subMatSize + i, subMatSize + j, 0 + i, 0 + j)
            resRow.push(ans)
        }
        res.push(resRow)
    }
    return res
};

const grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
const grid2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

console.log(largestLocal(grid))

// O(N^2) & O(1) yay!! Neetcode's solution was O(N^4) he used four nested loops.