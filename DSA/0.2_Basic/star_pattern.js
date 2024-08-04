function star(n) {
    /* 
        *
        **
        ***
        ****
        *****
    */
    let pattern = ''
    for (let i = 1; i <= n; i++) {
        console.log(pattern += '*')
    }
}

star(5)

function reverseStar(n) {
    /*
            * 4 space 1 star
           ** 3 space 2 start
          ***
         ****
        ***** 0 space 5 star
    */
    let ptrn = '     '
    for (let i = 1; i <= n; i++) {
        let ptrn2 = ptrn.slice(0, n - i)   // mistake, we cannot do ptrn[0] = 'x' because strings are immutable in js.
        for (let j = 0; j < i; j++) {
            ptrn2 += '*'
        }
        console.log(ptrn2)
    }
}

reverseStar(5)

function triangle(n) {
    /*
            *       4 space 1 star (star = 2 * 1 - 1 right)
           ***      3 space 3 star (star = 2 * 2 - 1)
          *****     2 space 5 star
         *******    1 space 7 star
        *********   0 space 9 star
    */
    for (let i = 1; i <= n; i++) {
        let spaces = ''; // Initialize spaces string
        let stars = '';  // Initialize stars string

        // Construct spaces string
        for (let j = 0; j < n - i; j++) {
            spaces += ' ';
        }

        // Construct stars string
        for (let k = 0; k < 2 * i - 1; k++) { // imp
            stars += '*';
        }

        // Print the combination of spaces and stars
        console.log(spaces + stars);
    }
}

triangle(5);
