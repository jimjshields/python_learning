# # path through grids

# import random

# def create_grid(n):
# 	grid = []
# 	for x in range (n + 1):
# 		for y in range (n + 1):
# 			grid.append((x, y))
# 	return grid

# def grid_paths(n):
# 	grid = create_grid(n)
# 	paths = {}

# 	for i in range (10000000):
# 		# fresh path
# 		current_path = []
# 		# start at (0, 0)
# 		current_position = grid[0]
# 		# if you're not at the end
# 		while current_position != grid[-1]:
# 			# add the current position to the path
# 			current_path.append(current_position)
# 			# set the x, y coordinates to x and y
# 			x, y = current_position[0], current_position[1]
# 			# can't go off the board
# 			if x == n:
# 				current_position = (x, y + 1)
# 			elif y == n:
# 				current_position = (x + 1, y)
# 			# if you're not at an edge, pick a random direction
# 			elif random.random() > 0.5:
# 				current_position = (x + 1, y)
# 			else:
# 				current_position = (x, y + 1)
# 		current_path.append(grid[-1])
# 		current_path = tuple(current_path)
# 		if current_path not in paths:
# 			paths[current_path] = current_path
# 	return len(paths)

# for i in range(21):
# 	print "%s: %s" % (i, grid_paths(i))

def build_path_grid(n):
	grid = []
	for i in range(n + 1):
		array = []
		if i == 0:
			array = [1] * (n + 1)
		else:
			for d in range(n + 1):
				if d == 0:
					array.append(1)
				else:
					array.append(array[d-1] + grid[i-1][d])
		grid.append(array)
	return grid

print build_path_grid(20)

