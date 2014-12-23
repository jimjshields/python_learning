# names scores
# each name in the text file has an alpha position
# and a alpha value (adding up the number position of its letters)
# multiply those two to get its name scores
# what's the total of all of the name scores?

# store the names in a list
def store_names(file):

	'''
	expects an open file
	returns a list of names from the file
	'''

	# not sure why i have to iterate?
	for i in file:
		name_list = i.replace('"', '').split(',')
	return name_list

# alphabetize it
def sort_names(name_list):
	return sorted(name_list)

# alpha scores
def alpha_score(letter):
	
	'''
	expects a letter
	returns its score
	'''

	return ord(letter) - 96

def alpha_value(word):

	'''
	expects a word
	returns its score
	'''

	word = word.lower()

	score = 0
	for letter in word:
		score += alpha_score(letter)
	return score

# alpha position
def alpha(name_list):

	'''
	expects a list of sorted names
	returns a dictionary of names as keys
	and alpha position as values
	'''

	alpha = {}

	for i in range(len(name_list)):
		alpha[name_list[i]] = (i + 1, alpha_value(name_list[i]))

	# test given by project euler
	assert alpha['COLIN'] == (938, 53)

	return alpha

def full_score(alpha):
	
	'''
	expects dictionary of name, tuple of position and score
	returns the total score of a dictionary
	'''

	total = 0

	for name in alpha:
		score = 1
		for i in alpha[name]:
			score *= i
		total += score

	return total

# open the file
f = open('p022_names.txt')

# store necessary variables
name_list = store_names(f)
sorted_names = sort_names(name_list)
alpha = alpha(sorted_names)

# print the full score
print full_score(alpha)