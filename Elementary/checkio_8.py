#def checkio_8.py

def checkio(integer):
	s = str(integer)
	mul = 1
	for i in s:
		if  i == '0':
			continue #也可以是pass
		else:
			mul = mul * int(i)
	return mul