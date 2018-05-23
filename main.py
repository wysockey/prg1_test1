import math
def is_square(number):
	'''problem 1)
	write a function that tells you if a number is a perfect square
	return True when the variable number is a perfect square
	return False when the variable called number is not a perfect square
	e.g. 
		number=16 -> True 
		number =15 -> False
	'''
	if(number <0):
		 return False
	return math.sqrt(number)== int(math.sqrt(number))


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

def cycle(n):
	strn = str(n)
	sum = 0
	for sdigit in str(n):
		digit = int(sdigit)
		sum = sum + (digit * digit)
	return sum

def is_happy(n):
	''' Extra credit
	A happy number is a number defined by the following process: Starting with any positive integer,
	replace the number by the sum of the squares of its digits,
	and repeat the process until the number equals 1 (where it will stay), 
	or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

	Write a function that tells you if n is a happy number
'''
	found = []
	while(n != 1):
		n = cycle(n)
		if(n in found):
			return False
		found.append(n)
	return True
	
	
	

	return True
































'''
if __name__ == "__main__":
	print("running problem 1")
	print(filter(lambda x: is_square(x),range(1,10000)))
	raw_input("press enter to run second problem")
	print("running  problem 2")
	print(filter(lambda x: is_factorion(x),range(1,10000)))
	#print("running extra credit")
	#print(filter(lambda x: is_happy(x),range(1,10000))
'''






