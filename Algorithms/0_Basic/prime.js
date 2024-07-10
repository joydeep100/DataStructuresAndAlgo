function prime(n){

    if (n < 0){
        return -1  // -ve no's cannot be a prime number
    }
    if (n > 0 && n <= 1){
        return false // not a prime
    }
    for(let i=2; i<n; i++){
        if (n % i === 0) return false
    }

    return true
}

console.log(prime(5))