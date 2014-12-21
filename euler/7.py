import math

def check_if_prime(num):
	sqr = int(math.sqrt(num))
	for i in range(2, sqr + 1):
		if num % i == 0:
			return False
	else:
		return True

def prime_list(num_of_primes):
	primes = []
	i = 2
	while len(primes) < num_of_primes:
		if check_if_prime(i):
			primes.append(i)
		i += 1
	return primes

print prime_list(10001)[-1]
			