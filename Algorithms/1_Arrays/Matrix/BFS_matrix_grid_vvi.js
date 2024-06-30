/* https://www.youtube.com/watch?v=KiCBXu4P-2Y&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=6

   How to solve any shortest path / min count required to reach the fill the Matrix Grid 

   - We will use BFS

   - What we need
        
        - Directional values [[1, 0], [0, 1], [-1, 0], [0, -1]] - for 4 ways navigation 
                             [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1],[-1, -1]] - for 8 way navigation
        - A queue, each item will have 3 things, [row, col, path]
        - A visited Matrix of the same size as the original matrix

        - first we would need to find the start, if not row=0, col=0
        - put start element (0,0,1) to queue (note: sometimes path needs to be init to 0 / 1 depending on the output requirements)

        - while (queue) is not empty

            - const [row, col, path] = queue.shift() //dequeue

            - check for exit condition

            - for loop (to check all neighbours)
            
                - if any new postion is going out of bounds or if there is any obstacle or if we already visited - skip

                - else, add the neighbour into the queue ([row, col, path + 1]), increment the path

                - mark the position as visited

        - return -1 if not found
*/

// 1091. Shortest Path in Binary Matrix https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1304708264/
function shortestPathBinaryMatrix(grid) {
    // here we are allowed to check neighbors in 8 directions

    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    let queue = []
    queue.push([0, 0, 1]) // here the start is always 0,0 and path needs to be 1 as per the expected output
    // mistake missed []
    const N = grid.length

    let visited = []
    for (let i = 0; i < N; i++) {
        // we are creating an array of size N (for each column)
        visited.push(new Array(N).fill(false))
    }

    // incase the starting point itself is blocked
    if (grid[0][0] === 1) return -1

    while (queue.length) {

        const [row, col, path] = queue.shift()

        // exit condition, we know that we reached the end
        if (row === N - 1 && col === N - 1) return path // mistake forgot -1

        // check neighbors
        for (const [dx, dy] of directions) {

            x = row + dx
            y = col + dy

            if (x < 0 || x >= N) continue
            if (y < 0 || y >= N) continue
            if (grid[x][y] === 1) continue
            if (visited[x][y]) continue

            queue.push([x, y, path + 1]) // mistake missed []
            visited[x][y] = true
        }

    }

    return -1

}

// 1730. Shortest Path to Get Food https://leetcode.com/problems/shortest-path-to-get-food/description/
// console.log(shortestPathBinaryMatrix([[[0, 1], [1, 0]]]))

var getFood = function (grid) {

    // here we are allowed to move about in 4 ways so
    const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    const M = grid.length  // grid is having size of M*N
    const N = grid[0].length // see its not a square :P

    let queue = []

    // update visited to false
    let visited = []
    for (let i = 0; i < M; i++) {
        visited.push(new Array(N).fill(false)) 
    }

    // find starting position
    for (let i = 0; i < M; i++) {
        for (let j = 0; j < N; j++) {
            if (grid[i][j] === '*') {
                queue.push([i, j, 0])
                visited[i][j] = true
                break
                // here we have requirement to init the path to 0 instead of 1 as per requirement of the answer :P
            }
        }
    }

    while (queue.length) {

        const [row, col, path] = queue.shift()

        // if we find food we need to return the path value (no of min steps taken to reach food)
        if (grid[row][col] === '#') return path

        for (const [dx, dy] of directions) {

            let x = row + dx
            let y = col + dy

            if (x < 0 || x >= M) continue
            if (y < 0 || y >= N) continue //mistake, used M here as well. Took a long time to figure it out. due to bad variable naming.
            if (grid[x][y] === 'X') continue
            if (visited[x][y]) continue

            queue.push([x, y, path + 1])
            visited[x][y] = true
        }
    }

    return -1
};

console.log(getFood([["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]))