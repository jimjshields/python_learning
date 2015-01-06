# in-text exercises

# 16.1
class Time(object):
	"""Represents the time of day.

	attributes: hour, minute, second
	"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

# ex 1
def print_time(time):
	"""prints stringified time"""
	print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

# ex 2
def is_after(t1, t2):
	"""returns True if t1 follows t2; False otherwise"""
	is_after_hour = t1.hour - t2.hour
	is_after_minute = t1.minute - t2.minute
	is_after_second = t1.second - t2.second
	return (is_after_hour > 0) or (is_after_hour == 0 and is_after_minute > 0) or (is_after_hour == 0 and is_after_minute == 0 and is_after_second > 0)

time2 = Time()
time2.hour = 12
time2.minute = 59
time2.second = 29

# print is_after(time, time2)

# 16.2
def add_time(t1, t2):
	time_sum = Time()
	time_sum.hour = t1.hour + t2.hour
	time_sum.minute = t1.minute + t2.minute
	time_sum.second = t1.second + t2.second

	# account for overrunning hours, minutes, seconds
	if time_sum.second >= 60:
		time_sum.second -= 60
		time_sum.minute += 1
	if time_sum.minute >= 60:
		time_sum.minute -= 60
		time_sum.hour += 1
	if time_sum.hour >= 24:
		time_sum.hour -= 24

	return time_sum

time_sum = add_time(time, time2)
# print_time(time_sum)

# 16.3
def increment(time, seconds):
	time.second += seconds

	if time.second >= 60:
		time.second -= 60
		time.minute += 1

	if time.minute >= 60:
		time.minute -= 60
		time.hour += 1

# ex 3
def increment_better(time, seconds):
	time.second += seconds

	if time.second >= 60:
		minutes = time.second / 60
		seconds = time.second % 60
		time.second = seconds
		time.minute += minutes

	if time.minute >= 60:
		hours = time.minute / 60
		minutes = time.minute % 60
		time.minute = minutes
		time.hour += hours

	if time.hour >= 24:
		hours = time.hour % 24
		time.hour = hours

# ex 4
def increment_functional(time, seconds):
	new_time = Time()
	new_time.second = time.second
	new_time.minute = time.minute
	new_time.hour = time.hour
	
	new_time.second += seconds

	if new_time.second >= 60:
		minutes = new_time.second / 60
		seconds = new_time.second % 60
		new_time.second = seconds
		new_time.minute += minutes

	if new_time.minute >= 60:
		hours = new_time.minute / 60
		minutes = new_time.minute % 60
		new_time.minute = minutes
		new_time.hour += hours

	if new_time.hour >= 24:
		hours = new_time.hour % 24
		new_time.hour = hours

	return new_time

# 16.4
# doesn't actually work if over 24 hours
def time_to_int(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds

def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	_x, time.hour = divmod(time.hour, 24)
	return time

def add_time_2(t1, t2):
	seconds = time_to_int(t1) + time_to_int(t2)
	return int_to_time(seconds)

# ex 5
def increment_2(time, seconds):
	time_seconds = time_to_int(time)
	time_seconds += seconds
	return int_to_time(time_seconds)

# ex 6
def mul_time(time, mul):
	seconds = time_to_int(time)
	seconds *= mul
	return int_to_time(seconds)

def div_time(time, div):
	seconds = time_to_int(time)
	seconds /= div
	return int_to_time(seconds)

def avg_pace(time, dist):
	"""inputs: finishing time (time obj), dist in miles (int)
	   output: pace per mile (time obj)"""
	return div_time(time, dist)

race_time = Time()
race_time.hour = 0
race_time.minute = 16
race_time.second = 40

# print_time(avg_pace(race_time, 3.1))

# ex 7
import datetime

def current_day():
	WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	return WEEKDAYS[datetime.date.today().weekday()]

def age_and_birthday(birthday):
	age = datetime.date.today().year - birthday.year

print age_and_birthday
