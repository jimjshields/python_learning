# 17.2
class Time(object):
	"""Represents the time of day."""

	def print_time(self):
		print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

time = Time()
time.hour = 12
time.minute = 30
time.second = 30
# time.print_time()

# ex 1
class Time(object):
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

# have to either redefine the object or consolidate the class above the first definition
time = Time()
time.hour = 12
time.minute = 30
time.second = 30

# print time.time_to_int()

# 17.3
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	_x, time.hour = divmod(time.hour, 24)
	return time

class Time(object):
	"""Represents the time of day."""

	def print_time(self):
		print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

start = Time()
start.hour = 12
start.minute = 30
start.second = 30

# start.print_time()
end = start.increment(1000)
# end.print_time()

# 17.4
class Time(object):
	"""Represents the time of day."""

	def print_time(self):
		print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

start = Time()
start.hour = 12
start.minute = 30
start.second = 30

end = start.increment(1000)

# print end.is_after(start)

# 17.5
class Time(object):
	"""Represents the time of day."""

	def __init__(self, hour=0, minute=0, second=0):
		# initialization - defaults to 0 for all; if it's passed arguments will assign those to the object's attributes
		self.hour = hour
		self.minute = minute
		self.second = second

	def print_time(self):
		print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

# ex 2
class Point(object):
	"""represents a point in 2d space"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

point = Point(1, 0)

# 17.6
class Time(object):
	"""Represents the time of day."""

	def __init__(self, hour=0, minute=0, second=0):
		# initialization - defaults to 0 for all; if it's passed arguments will assign those to the object's attributes
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

	# can remove print_time

	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

time = Time(9, 45)
# print time # 09:45:00

# ex 3
class Point(object):
	"""represents a point in 2d space"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)

point = Point(10, 3)

# 17.7
class Time(object):
	"""Represents the time of day."""

	def __init__(self, hour=0, minute=0, second=0):
		# initialization - defaults to 0 for all; if it's passed arguments will assign those to the object's attributes
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

	def __add__(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)

	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

start = Time(9, 45)
duration = Time(1, 35)
# print start + duration

# ex 4
class Point(object):
	"""represents a point in 2d space"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)

	def __add__(self, other):
		new = Point(self.x + other.x, self.y + other.y)
		return new

# 17.8
class Time(object):
	"""Represents the time of day."""

	def __init__(self, hour=0, minute=0, second=0):
		# initialization - defaults to 0 for all; if it's passed arguments will assign those to the object's attributes
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def __radd__(self, other):
		return self.__add__(other)
	
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def add_time(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

# ex 5
class Point(object):
	"""represents a point in 2d space"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)

	def __add__(self, other):
		if isinstance(other, Point):
			return Point(self.x + other.x, self.y + other.y)
		else:
			return Point(self.x + other[0], self.y + other[1])

	def __radd__(self, other):
		return self.__add__(other)

pointa = Point(1, 2)
pointb = Point(3, 4)
# print pointa + pointb

pointc = (10, 15)
# print pointa + pointc
# print pointc + pointa

# 17.10
def print_attributes(obj):
	for attr in obj.__dict__:
		print "%s: %s" % (attr, getattr(obj, attr))

# ex 7
class Kangaroo(object):
	"""represents a kangaroo"""

	def __init__(self):
		self.pouch_contents = []

	def __str__(self):
		return "Objects in pouch: %s" % (self.pouch_contents)

	def put_in_pouch(self, obj):
		self.pouch_contents.append(obj)

# ex 8
