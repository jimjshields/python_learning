def check_if_divisible(num):
	for i in range(11, 20)[::-1]:
		if num % i != 0:
			return False
	else:
		return True

for i in range (20, 1000000000, 20):
	if check_if_divisible(i):
		print "%s: %s" % (i, check_if_divisible(i))

# not_found = True

# while not_found:
# 	i = 20
# 	if check_if_divisible(i):
# 		not_found = False
# 		print "%s is divisible by everything from 1 to 20!" % (i)
# 	else:
# 		i += 20