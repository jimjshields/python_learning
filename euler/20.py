# sum of digits of 100!

def factorial(num):
	if num == 1:
		total = 1
	else:
		total = num * factorial(num - 1)
	return total

def sum_of_digits(num):
	total = 0
	for i in str(num):
		total += int(i)
	return total

print sum_of_digits(factorial(100))