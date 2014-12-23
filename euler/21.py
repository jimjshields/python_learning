# amicable numbers
# pair - sum of proper divisors of one equals the other and vice versa

import sys

def proper_divisors(max_num):
	
	'''
	expects a maximum number
	returns a dictionary - each number up to the max 
	mapped to a list of its proper (i.e., exact) divisors
	'''

	# initialize with 1
	divisors = {1: [1]}
	
	# for each number after 1 until the max
	for n in range(2, max_num + 1):
		# set the divisors equal to an empty array
		divisors[n] = []
		# for each number up to half of n (maximum possible divisors)
		for i in range(1, n/2 + 1):
			# if it's a proper divisor
			if n % i == 0:
				# check if it's already been calculated
				if i in divisors:
					# if so just take those divisors
					for d in divisors[i]:
						# and make sure not to duplicate
						if d not in divisors[n]:
							divisors[n].append(d)
				# if it hasn't been calculated, just add that number
				if i not in divisors[n]:
					divisors[n].append(i)
	# return the dictionary
	return divisors

def divisors_sum(num, dict):
	
	'''
	expects a number and a dictionary of divisors
	returns the sum of the number's divisors
	'''

	total = 0
	for i in dict[num]:
		total += i
	return total

def find_amicable(dict):
	
	'''
	expects a dictionary of divisors
	returns a list of amicable tuples
	'''

	amicable = []
	# go through all numbers in the given dictionary
	for i in dict.keys():
		# set this equal to the sum of the divisors of the first
		divisors_sum_i = divisors_sum(i, dict)
		# then go through all of them again
		for n in dict.keys():
			# if the opposite isn't already in there
			if (i, n) not in amicable:
				# set the second var equal to the sum of its divisors
				divisors_sum_n = divisors_sum(n, dict)
				# check if n and i are amicable
				if i == divisors_sum_n and n == divisors_sum_i and n != i:
					# if so, add it
					amicable.append((n, i))
	return amicable

def amicable_sum(amicable):
	
	'''
	expects a list of amicable pair tuples
	returns the sum of all of the pairs
	'''

	total = 0
	for pair in amicable:
		total += pair[0] + pair[1]
	return total


# set the variables
max_num = int(sys.argv[1])
divisors = proper_divisors(max_num)
amicable = find_amicable(divisors)


# print the answers to the console
print amicable
print amicable_sum(amicable)