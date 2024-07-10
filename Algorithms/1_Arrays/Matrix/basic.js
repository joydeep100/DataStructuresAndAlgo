// init an m * n array with a value

const intArr = function (m, n, val) {

    let arr = []

    for (let i = 0; i < m; i++) {
        let column = []
        for (let j = 0; j < n; j++) {
            column.push(val)
        }
        arr.push(column)
    }

    return arr

}

// same thing but using Array object
const intArrUsingArr = function (m, n, val) {

    let arr = new Array(m)

    // let arr = new Array(m).fill(0) , incase we want to pre-fill all the values with 0

    for (let i = 0; i < m; i++) {
        let column = new Array(n)
        for (let j = 0; j < n; j++) {
            column[j] = val
        }
        arr[i] = column
    }

    return arr

}

console.log(intArr(2, 3, 0))
console.log(intArrUsingArr(2, 3, 0))

