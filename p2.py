
def is_factorion(n):
	'''problem 2)
	A factorion is a number that is equal to the sum of its factorials.
	so for example, n= 145 is a factorion. 
	1! = 1
	4! = 4 * 3 * 2 * 1 = 24
	5! = 5 * 4 * 3 * 2 * 1 = 120
	1 + 24 + 120 = 145

	Write a function that returns True if n is a factorion
	'''
	sn = str(n)
	sum = 0
	for digit in sn:
		factorial = 1
		for x in range(1,int(digit)+1):
			factorial *= x
		sum += factorial
	#print(sum,n)
	return sum == n 