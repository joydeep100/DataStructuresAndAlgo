// find a number in ones, tens, hundreads place etc


function extractDigitsToArray(number) {
    let digits = [];

    while (number > 0) {
        digits.push(number % 10); // Add the ones place digit to the front of the array
        number = Math.floor(number / 10); // Remove the ones place digit
    }

    return digits.reverse();
}

// Example usage:
let number = 153;
let extractedDigits = extractDigitsToArray(number);
console.log("Extracted digits:", extractedDigits); // Output: [1, 5, 3]
