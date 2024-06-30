function traverseRow(matrix) {
    
    const len = matrix.length

    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            console.log(matrix[i][j]);
        }
    }
}


function traverseCol(matrix) {

    const len = matrix.length

    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            console.log(matrix[j][i]);
        }
    }
}

// Test the function with the given matrix
let matrix = [
    [0, 6, 8],
    [20, 22, 27],
    [36, 38, 50],
];


console.log(traverseRow(matrix))
console.log(traverseCol(matrix))
