#checkio_3.py

def checkio(l):
	if len(l) == 0:
		return 0
	else:
		a = 0
		for i in range(len(l)):
			if i % 2 == 0:
				a = a + l[i]
		return a*l[-1]


