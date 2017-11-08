#checkio_2.py
from datetime import date,timedelta
def checkio(date1,date2):
	a = date(*date1)
	b = date(*date2)
	return abs((a-b).days)