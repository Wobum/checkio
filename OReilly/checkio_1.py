#def checkio_1.py

def checkio(data):
	data.sort()
	if len(data) %2 = 1:
		return data[len(data)//2]
	else:
		return (data[len(data)//2]+data[len(data)//2-1])/2