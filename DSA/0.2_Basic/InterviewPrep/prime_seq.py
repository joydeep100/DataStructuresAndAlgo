def isPrime(n): 
	
	if n <= 1 : 
		return False

	# check from 2 to n-1 
	for i in range(2, n): 
		if n % i == 0: 
			return False

	return True

def printPrime(n): 
	for i in range(2, n + 1): 
		if isPrime(i): 
			print(i, end = " ")

printPrime(10) 