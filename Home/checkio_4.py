#checkio_4.py

def count_words(t,w):
	n = 0
	for i in w:
		if i in t.lower():
			n += 1
	return n

	