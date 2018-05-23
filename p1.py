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
 
