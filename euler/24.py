# what is the millionth lexicographic permutation of 0123456789?

def num_array(num):
	
	'''
	expects a string of a number
	returns array of the number
	'''

	num_array = []
	for i in num:
		num_array.append(int(i))
	return num_array

def ordered_permutations(num_array, num):
	'''
	expects a number array
	returns an ordered list 
	of the first num permutations
	'''

	permutations = []

	for n in range(num + 1):
		for i in range(len(num_array), 0, -1):
			prefix = num_array[0:i]
			suffix = num_array[i:len(num_array)]
			perm = []

def all_perms(elements):
	if len(elements) <= 1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
		    for i in range(len(elements)):
		        yield perm[:i] + elements[0:1] + perm[i:]
		
perms = all_perms('0123456789')
perms_sorted = sorted([i for i in perms])

print perms_sorted
print perms_sorted[999999]