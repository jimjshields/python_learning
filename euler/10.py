import math

def check_if_prime(num):
	sqr = int(math.sqrt(num))
	for i in range(2, sqr + 1):
		if num % i == 0:
			return False
	else:
		return True

def prime_sum(max_num):
	primes = []
	for i in range(2, max_num):
		if check_if_prime(i):
			primes.append(i)
	total = 0
	print primes
	for n in primes:
		total += n
	return total

print prime_sum(2000000)