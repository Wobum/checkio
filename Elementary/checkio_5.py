#checkio_5.py

def checkio(string):
	a = string.split()
	b = 0
	for i in a:
		if b <= len(a) - 2:
			if str.isalpha(i):
				if str.isalpha(a[b+1]):
					if str.isalpha(a[b+2]):
						return True
		b += 1
	else:
		return False
'''
def checkio(words):
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
        else:
            count = 0
        if count >= 3 :
            return True
    else:
        return False
'''