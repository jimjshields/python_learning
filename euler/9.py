import math

def find_pyth_triplets(max_num):
	sets = []
	# for all numbers to the max
	for i in range (1, max_num + 1):
		# go through all numbers to the max
		for n in range (1, max_num + 1):
			# add their squares together, check if its square root is an integer
			if int(math.sqrt((i * i) + (n * n))) == math.sqrt((i * i) + (n * n)):
				# if so, add it to the list
				pyth_triplet = sorted([i, n, int(math.sqrt((i * i) + (n * n)))])
				if pyth_triplet not in sets:
					sets.append(sorted(pyth_triplet))
	return sets

def check_sum(num, sets):
	new_sets = []
	for i in sets:
		total = 0
		for n in i:
			total += n
		if total == num:
			new_sets.append(i)
	return new_sets

def set_product(given_set):
	total = 1
	for i in given_set:
		total *= i
	return total

pyth_triplets = check_sum(1000, find_pyth_triplets(1000))

for i in pyth_triplets:
	print set_product(i)