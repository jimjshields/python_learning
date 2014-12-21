# https://projecteuler.net/problem=2
fib_start = [0, 1]

while fib_start[-1] + fib_start[-2] <= 4000000:
	fib_start.append(fib_start[-1] + fib_start[-2])

total = 0
for i in fib_start:
	if i % 2 == 0:
		print i
		total += i

print total