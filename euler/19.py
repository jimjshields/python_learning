# how many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?

days = {
	1: 'sunday',
	2: 'monday',
	3: 'tuesday',
	4: 'wednesday',
	5: 'thursday',
	6: 'friday',
	7: 'saturday'
}

months_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

months = {
	'jan': 31,
	'feb': [28, 29],
	'mar': 31,
	'apr': 30,
	'may': 31,
	'jun': 30,
	'jul': 31,
	'aug': 31,
	'sep': 30,
	'oct': 31,
	'nov': 30,
	'dec': 31
}

def is_leap_year(year):
	if year % 100 == 0:
		if year % 400 == 0:
			return True
		else:
			return False
	elif year % 4 == 0:
		return True
	else:
		return False

def sundays(start_year, end_year):
	day = 3
	sundays = []
	for year in range(start_year, end_year + 1):
		for month in months_list:
			if is_leap_year(year):
				if month == 'feb':
					day += months[month][1]
				else:
					day += months[month]
			else:
				if month == 'feb':
					day += months[month][0]
				else:
					day += months[month]
			if day % 7 == 1:
				sundays.append((year))
	return sundays

print len(sundays(1901, 2000))