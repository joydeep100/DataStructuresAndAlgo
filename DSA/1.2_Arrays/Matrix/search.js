function searchInMatrix(arr, x) {
    let m = arr.length, n = arr[0].length;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (arr[i][j] == x)
                return true;
        }
    }
    return false;
}

// Driver program to test above

let x = 8;
let arr
    = [[0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]];

console.log(searchInMatrix(arr, x))
