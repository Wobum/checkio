#checkio_1.py

def checkio(s):
	a = int(s)
	if  a % 3 == 0:
		if a % 5 == 0:
			return "Fizz Buzz"
		else:
			return 'Fizz'
	elif a % 5 == 0:
		return 'Buzz'
	else:
		return a