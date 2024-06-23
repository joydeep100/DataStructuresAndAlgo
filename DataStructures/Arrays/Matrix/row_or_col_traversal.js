function rowWiseTraversal(matrix) {
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            console.log(matrix[i][j]);
        }
    }
}


function columnWiseTraversal(matrix) {

    for (let j = 0; j < matrix[0].length; j++) { // Outer loop iterates over columns
        for (let i = 0; i < matrix.length; i++) { // Inner loop iterates over rows
            console.log(matrix[i][j]); // Access elements in column-wise order
        }
    }
}

// Test the function with the given matrix
let matrix = [
    [0, 6, 8],
    [20, 22, 27, 8],
    [36, 38, 50],
];


console.log(rowWiseTraversal(matrix))
console.log(columnWiseTraversal(matrix))
