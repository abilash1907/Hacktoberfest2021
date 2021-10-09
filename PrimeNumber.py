def isPrime(n):
	if n <= 1:
		return False

	# Check from 2 to n-1
	for i in range(2, n):
		if n % i == 0:
			return False;

	return True

n=input("enter a number:")
print("prime") if isPrime(int(n)) else print("not prime")
