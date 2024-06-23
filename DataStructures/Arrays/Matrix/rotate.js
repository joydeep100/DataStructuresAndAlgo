/* 
Matrix =  a00 a01 a02
          a10 a11 a12
          a20 a21 a22

when we rotate it by 90 degree
then matrix is
Matrix = a02 a12 a22
         a01 a11 a21
         a00 a10 a20
  
when we rotate it by again 90 
degree then matrix is 
Matrix = a22 a21 a20
         a12 a11 a10
         a02 a01 a00 

*/

function rotate(matrix) {

    for (i = matrix.length - 1; i >= 0; i--) {
        // just making matrix[0].length to matrix[i].length works for varied length of inner arrays (column arrays)
        for (j = matrix[i].length - 1; j >= 0; j--) {
            console.log(matrix[i][j])
        }
        console.log('----')
    }


}
var matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9, 11]];

rotate(matrix)


