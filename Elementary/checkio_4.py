#checkio_4.py

def checkio(s):
	result = ''
	for i in s:
		if str.isupper(i):
			result += i
	return result