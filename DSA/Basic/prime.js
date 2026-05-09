function prime(n){

    if (n < 2){ // since negative nos or 0 , 1 are not prime.
        return false
    }
    for(let i=2; i<n; i++){
        if (n % i === 0) return false
    }

    return true
}

console.log(prime(5))