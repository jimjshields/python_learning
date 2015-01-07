def countdown(n):
	print "Counting down!"
	while n > 0:
		yield n # generate a value (n)
		n -= 1

c = countdown(10)

for i in c:
	print i,