#checkio_2.py
from collections import Counter

def checkio_2(l):
	a = Counter(l)
	for k,v in a.items():
		if v == 1:
			l.remove(k)
	print(l)

def main():
	list1 = input("请输入数列：")
	checkio_2(list1)
if __name__ == '__main__':
	main()