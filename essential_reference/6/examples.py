# functions as objects and closures

# function that accepts another function as an argument and calls it
def callf(func):
	return func()

# data - when the function is called it won't use this value of x
# but will use the value of x defined when func is defined
x = 42
def callf(func):
	return func()

# from http://www.shutupandship.com/2012/01/python-closures-explained.html
def generate_power_func(n):
	print "id(n): %X" % id(n)
	def nth_power(x):
		return x**n
	print "id(nth_power): %X" % id(nth_power)
	return nth_power

# decorators

# implementation of trace
enable_tracing = True
if enable_tracing:
	debug_log = open("debug.log", "w")

def trace(func):
	if enable_tracing:
		def callf(*args, **kwargs):
			debug_log.write("Calling %s: %s, %s\n" %
							(func.__name__, args, kwargs))
			r = func(*args, **kwargs)
			debug_log.write("%s returned %s\n" % (func.__name__, r))
			return r
		return callf
	else:
		return func

# using trace as a decorator
@trace
def square(x):
	return x*x

# preceding code is shorthand for the following:
def square(x):
	return x*x

square = trace(square)

# generators

# example
# if you call this function, none of its code will execute - it will return a generator object
def countdown(n):
	print "Counting down from %d" % (n)
	while n > 0:
		yield n
		n -= 1
	return # note: generators can only return None

# coroutines and yield expressions

# examples
def receiver():
	print "Ready to receive"
	while True:
		n = (yield)
		print "Got %s" % (n)

# typical coroutine decorator
def coroutine(func):
	def start(*args, **kwargs):
		# assign g to calling the function with all possible arguments
		g = func(*args, **kwargs)
		# perform the first step
		g.next()
		# only after doing this, return the function to the caller
		return g
	# return start to the coroutine
	return start

# using the decorator
@coroutine
def receiver():
	print "Ready to receive"
	while True:
		n = (yield)
		print "Got %s" % (n)

# using the coroutine
r = receiver()
r.send(1)
r.send(100)
r.close()

# generator exit
def receiver():
	print "Ready to receive"
	while True:
		n = (yield)
		print "Got %s" % (n)
	# except GeneratorExit: # (doesn't work in 2?)
	# 	print "Receiver done"

# simultaneously receive and emit values
def line_splitter(delimeter=None):
	print "Ready to split"
	result = None
	while True:
		line = (yield result)
		result = line.split(delimeter)

# using generators and coroutines

# example - processing pipeline - processes one by one, not creating temp lists/data structures that would consume memory
import os
import fmatch

def find_files(topdir, pattern):
	for path, dirname, filelist in os.walk(topdir):
		for name in filelist:
			if fmatch.fmatch(name, pattern):
				yield os.path.join(path, name)

import gzip, bz2
def opener(filenames):
	for name in filenames:
		if name.endswith(".gzip"): f = gzip.open(name)
		elif name.endswith(".bz2"): f = bz2.B2File(name)
		else: f = open(name)
		yield f

def cat(filelist):
	for f in filelist:
		for line in f:
			yield line

def grep(pattern, lines):
	for line in lines:
		if pattern in line:
			yield line

# using these functions for a processing pipeline
wwwlogs = find_files("www", "access-log")
files   = opener(wwwlogs)
lines   = cat(files)
pylines = grep("python", lines)
# for line in pyline:
# 	sys.stdout.write(line)

# list comprehensions
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]

# same as:
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
	squares.append(n * n)

# more examples
a = [-3, 5, 2, -10, 7, 8]
b = 'abc'

c = [2 * s for s in a]
d = [s for s in a if s >= 0] 
e = [(x, y) for x in a
			for y in b
			if x > 0]

f = [(1, 2), (3, 4), (5, 6)]
g = [math.sqrt(x * x + y * y) for x, y in f]

# lambda
a = lambda x, y : x + y
r = a(2, 3) # 5

names.sort(key = lambda n : n.lower())

# recursion
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

def flatten(lists):
	for s in lists:
		if isinstance(s, list):
			flatten(s)
		else:
			print s

items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# recursive generator
def genflatten(lists):
	for s in lists:
		if isinstance(s, list):
			for item in genflatten(s):
				yield item
		else:
			yield item