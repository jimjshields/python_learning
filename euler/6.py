def sum_of_squares(max_num):
	squares = []
	for i in range(1, max_num + 1):
		squares.append(i * i)
	total = 0
	for i in squares:
		total += i
	return total

def square_of_sum(max_num):
	total = 0
	for i in range(1, max_num + 1):
		total += i
	return total * total

print square_of_sum(100) - sum_of_squares(100)