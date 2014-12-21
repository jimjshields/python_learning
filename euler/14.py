# longest collatz sequence

def collatz(num, array):
	array.append(num)
	if num != 1:
		if num % 2 == 0:
			collatz(num/2, array)
		else:
			collatz((3 * num) + 1, array)
	return array

def longest_collatz(max_num):
	all_collatz = {}
	for num in range(1, max_num + 1):
		collatz_array = []
		all_collatz[num] = len(collatz(num, collatz_array))
	
	ranked = []

	for tup in all_collatz.items():
		ranked.append((tup[1], tup[0]))
	
	ranked.sort(reverse=True)

	return ranked[0:9]

print longest_collatz(1000000)