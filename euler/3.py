# https://projecteuler.net/problem=3

import math

num = 600851475143
primes = []

def all_divisors(num):
	divisors = []
	sqr = int(math.sqrt(num))
	for i in range(2, sqr + 1):
		if i not in divisors:
			if num % i == 0:
				divisors.append(i)
				divisors.append(num/i)
	return sorted(divisors)

def check_if_prime(num):
	sqr = int(math.sqrt(num))
	for i in range(2, sqr):
		if num % i == 0:
			return False
			break
	else:
		return True

print all_divisors(num)

for i in all_divisors(num):	
	if check_if_prime(i):
		print "%s is prime!" % (i)