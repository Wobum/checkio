#checkio_3.py

def checkio(pw):
	a = str(pw)
	b = 0
	c = 0
	d = 0
	if len(a) >= 10:
		for i in a :
			if str.isdigit(i):
				b += 1
			if str.islower(i):
				c += 1
			if str.isupper(i):
				d += 1
	else:
		return False
	if b and c and d :
		return True
	else:
		return False