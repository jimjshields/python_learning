def check_if_palindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False

def three_digit_products():
	products = []
	for i in range(100, 1000):
		for n in range(100, 1000):
			products.append(n * i)
	return sorted(products)

for i in three_digit_products():
	if check_if_palindrome(i):
		print "%s is a palindrome!" % (i)