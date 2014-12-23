# what numbers <= 28123 are not the sum of any two abundant numbers?

# build dictionary of divisors
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

def sum_all(array):

	'''
	expects array
	returns total sum of the items in the array
	'''

	total = 0
	for i in array:
		total += i
	return total

def abundant_numbers(divisors):

	'''
	expects a dictionary of numbers and their divisors
	returns a list of abundant numbers in that range
	'''

	abundant = []

	# for each number
	for num in divisors:
		# if the sum of its divisors is greater than the num itself (i.e., abundant)
		if sum_all(divisors[num]) > num:
			# add it to the list
			abundant.append(num)
	return abundant

def abundant_sums(abundant):
	
	'''
	expects a list of abundant numbers
	returns a list of all possible sums of those numbers
	'''

	sums = set()

	# for each abundant number
	for i in abundant:
		# start the total as the number
		total = i
		# then get all of the possible sums for that number
		for n in abundant:
			# but only add it if it's new
			if total + n not in sums:
				# debugging
				print total + n
				sums.append(total + n)

	return sorted(sums)

def is_abundant_sum(num, abundants):
	'''
	expects any number
	checks if number is a sum of two abundant numbers
	returns a boolean
	'''

	abundants_for_num = [i for i in abundants if i < num]
	for i in abundants_for_num:
		if num - i in abundants_for_num:
			return True


def non_abundant(max_num):
	
	'''
	takes in a maximum number
	returns a list of numbers not summed through abundant numbers
	'''

	divisors = proper_divisors(max_num)
	abundant = abundant_numbers(divisors)
	sums = abundant_sums(abundant)

	non_abundant = []

	for i in range(1, max_num + 1):
		if i not in sums:
			non_abundant.append(i)

	return non_abundant

num = 28123
abundants = abundant_numbers(proper_divisors(num))
non_abundant = [i for i in range(num + 1) if not is_abundant_sum(i, abundants)]
print non_abundant
print sum_all(non_abundant)
	

# non_abundant = non_abundant(28123)
# print sum_all(non_abundant)