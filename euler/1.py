# https://projecteuler.net/problem=1

three_and_five = []

for i in range(1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		three_and_five.append(i)

total = 0
for i in three_and_five:
	total += i

print total