#checkio_4.py

def checkio(date1,date2):
	s = ''
	for i in  range(len(date1)):
		for j in range(len(date1[i])):
			if date1[i][j] == 'X':
				s += date2[i][j]
	return s

def Rotate(matrix):
	l = []
	l1 = []
	for i in range(len(matrix)):
		list1 = list(matrix[i])
		l.append(list1)
	l2 = zip(*l[::-1])
	for i in l3:
		f = ''.join(i)
		l1.append(f)
	return tuple(l1)

def main(a,b):
	date1 = a
	date2 = b
	result = ''
	for i in range(4):
		s = ''
		s = checkio(date1,date2)
		date1 = Rotate(date1)
		result += s
	return result