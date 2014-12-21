# power digit sum - sum of all digits in 2**1000

num = 2**1000

total = 0
for i in str(num):
	total += int(i)
	print "%s: %s" % (i, total)

print total