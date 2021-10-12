def Prime(n):
	if n <= 1:
		return False

	# Check from 2 to n-1
	for i in range(2, n):
		if n % i == 0:
			return False;

	return True

n=input("Enter a number:")
print("Entered number is a prime number")
if Prime(int(n))
else print("Entered number is not a prime number")
