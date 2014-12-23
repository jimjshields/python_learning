# first 1000-digit fibonacci number

def fibonacci(num):
	fib = []
	for i in range(num):
		if i == 0:
			fib.append(1)
		elif i == 1:
			fib.append(1)
		else:
			fib.append(fib[i - 1] + fib[i - 2])
	return fib

fib = fibonacci(4785)
# one_thous_digits = [x for x in fib if len(str(x)) >= 1000]
for x in range(len(fib)):
	if len(str(fib[x])) >= 1000:
		print "%s" % (x)