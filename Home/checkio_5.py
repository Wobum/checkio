#checkio_5.py

def checkio(s):
	for row in s:
		if row[0] == row[1] == row[2] and row[0] != '.':
			return row[0]
			break
	a = zip(*s)
	for row in a:
		if row[0] == row[1] == row[2] and row[0] != '.':
			return row[0]
			break
	if s[0][0] == s[1][1] == s[2][2]:
			return s[0][0]
			break
	elif s[0][2] == s[1][1] == s[2][0]:		
		return s[0][2]
		break
	return 'D'
def checkio(s):
	for row in s:
		if row[0] == row[1] == row[2] and row[0] != '.':
			return row[0]
	a = zip(*s)
	for row in a:
		if row[0] == row[1] == row[2] and row[0] != '.':
			return row[0]
	if s[0][0] == s[1][1] == s[2][2] and s[0][0] != '.':
		    return s[0][0]
	elif s[0][2] == s[1][1] == s[2][0] and s[0][2] != '.':		
		return s[0][2]
	else:
		return 'D'

