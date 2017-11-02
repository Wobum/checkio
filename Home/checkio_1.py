#checkio.py
import re
from collections import Counter

def checkio(text):
	a = str(text)
	b = re.findall('[a-zA-z]',a.lower())
	c = Counter(b)
	l = list(c.values())
	d = max(l)
	list1 = []
	for k,v in c.items():
		if v == d :
			list1.append(k)
	list1 = sorted(list1)
	return list1[0]
def main():
        for i in range(5):
                a = input ('输入字符串：')
                print(checkio(a))
main()
        

