import math
# triangle numbers

def find_triangle_nums(max_num):
	triangle_numbers = []
	total = 0

	for i in range(1, max_num):
		total += i
		triangle_numbers.append(total)

	return triangle_numbers

def count_divisors(num):
	divisors = [1, num]
	for i in range(2, int(math.sqrt(num)))[::-1]:
		if i not in divisors:
			if num % i == 0:
				divisors.append(i) 
				divisors.append(num/i)
	return len(divisors)

for i in [x for x in find_triangle_nums(1000000) if x > 5000000]:
	if count_divisors(i) > 500:
		print "%s has over 500 divisors!!!!" % (i)