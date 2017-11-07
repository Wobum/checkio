#checkio_11.py
from collections import Counter
def checkio(data):
	a = Counter(data)
	max = 0
	for i in a.values():
		if i > max: 
			max = i
	for k,v in a.items():
		if v == max:
			return k
'''def most_frequent(data):
	c = Counter(data)
    return c.most_common()[0][0]
