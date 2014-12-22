import random

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle_array = [i.split(' ') for i in triangle.split('\n')]

def possible_paths(max_num, arrays):
	array = []
	for i in range(max_num):
		if i == 0:
			array.append(0)
		else:
			array.append(random.randint(array[i-1], array[i-1] + 1))
	if array not in arrays:
		arrays.append(array)

arrays = []
for i in range(200000):
	possible_paths(15, arrays)

print len(arrays)

totals = []

for array in arrays:
	total = 0
	for i in range(len(array)):
		total += int(triangle_array[i][array[i]])
	totals.append(total)

totals.sort(reverse=True)
print totals[:9]

# def one_path(triangle_array, row_num, i):
# 	total = 0
# 	if row_num == len(triangle_array):
# 		return total
# 	else:
# 		total += int(triangle_array[row_num][i])
# 		row_num += 1
# 		one_path(triangle_array, row_num, i)
			
# print one_path(triangle_array, 0, 0)


# def all_paths(triangle_array):
# 	sums = []
# 	total = 0
# 	for row in triangle_array:
		


# # for i in range(len(triangle_array)):
# # 	for n in range(len(triangle_array[i])):
# # 		triangle_rank[(i, n)] = triangle_array[i][n]