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
	l2 = [0,0,0,0]
	l3 = [l2.l2,l2,l2]
	for i in range(len(matrix)):
		list1 = list(matrix[i])
		l.append(list1)
	for i in range(len(l)):	
		for j in range(len(l[i])):
			l3[i][j] = l[j][len(l[i])-i]
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