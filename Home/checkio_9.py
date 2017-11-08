#checkio_9.py

def checkio(s):
	if len(s) == 0:
		return 0
	else:
		a = s + ' '
		repeat = 1
		i = 0
		l = []
		while i < len(s):
			if a[i] == a[i+1]:
				repeat += 1
			else:
				l.append(repeat)
				repeat = 1
			i += 1
		return max(l)
'''
def long_repeat(line):
    count = 1
    maxi = 1
    if line != "":
        for i in range(1,len(line)):
            if line[i] == line[i-1]:///如果这里换成line[i] == line[i+1]的话，字符串索引会超出范围
                count+=1
                if count > maxi:
                    maxi = count
            else:
                count = 1
        return maxi
    else:
        return 0