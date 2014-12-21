import random

# make a histogram
def create_hist(seq):
	hist = {}
	for i in seq:
		hist[i] = hist.get(i, 0) + 1
	return hist

# choose a random value from a histogram in proportion to its frequency
def choose_from_hist(hist):
	hist_list = []
	for i, freq in hist.items():
		hist_list.extend([i] * freq)
	return random.choice(hist_list)

t = ['a', 'a', 'b', 'c', 'c', 'c']
hist = create_hist(t)
print choose_from_hist(hist)