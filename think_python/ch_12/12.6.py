# longest reducible word
# mine is super slow - possibly due to the way i'm memoizing the words?
# i'm definitely doing some calculation far too often when it only needs to be done once

f = open('words.txt')

word_list = f.read().split('\r\n')
word_list.append('a')
word_list.append('i')

def word_children(word, word_list):
	# word - string of a known word
	# word_list - list of known words
	# returns list of words that can be formed by removing one letter
	children = []
	possible_children = []
	for i in range(len(word)):
		if i == 0:
			child_test = word[1:]
		elif i == len(word):
			child_test = word[:-2]
		else:
			child_test = word[:i] + word[i + 1:]
		possible_children.append(child_test)
	for i in possible_children:
		if i in word_list:
			children.append(i)
	return children

reducible = {}
reducible[''] = ['']

def check_reducible(word, word_list):
	if word in reducible:
		return reducible[word]
	res = []
	for i in word_children(word, word_list):
		t = check_reducible(i, word_list)
		if t:
			res.append(i)
	reducible[word] = res
	return res

def find_reducible(word_list):
	res = []
	for word in word_list:
		t = check_reducible(word, word_list)
		if t != []:
			res.append((len(word), word))
		print word, len(res)
	res.sort(reverse=True)
	print res
	return res
	
# reducible = ['a', 'i', '']
find_reducible(word_list)
# print check_reducible('an', word_list)

# """This module contains code from
# Think Python by Allen B. Downey
# http://thinkpython.com

# Copyright 2012 Allen B. Downey
# License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

# """

# def make_word_dict():
#     """Reads the words in words.txt and returns a dictionary
#     that contains the words as keys."""
#     d = dict()
#     fin = open('words.txt')
#     for line in fin:
#         word = line.strip().lower()
#         d[word] = word

#     # have to add single letter words to the word list;
#     # also, the empty string is considered a word.
#     for letter in ['a', 'i', '']:
#         d[letter] = letter
#     return d

# word_dict = make_word_dict()


# """memo is a dictionary that maps from each word that is known
# to be reducible to a list of its reducible children.  It starts
# with the empty string."""

# memo = {}
# memo[''] = ['']


# def is_reducible(word, word_dict):
#     """If word is reducible, returns a list of its reducible children.

#     Also adds an entry to the memo dictionary.

#     A string is reducible if it has at least one child that is 
#     reducible.  The empty string is also reducible.

#     word: string
#     word_dict: dictionary with words as keys
#     """
#      # if have already checked this word, return the answer
#     if word in memo:
#         return memo[word]

#     # check each of the children and make a list of the reducible ones
#     res = []
#     for child in children(word, word_dict):
#         t = is_reducible(child, word_dict)
#         if t:
#             res.append(child)

#     # memoize and return the result
#     memo[word] = res
#     return res


# def children(word, word_dict):
#     """Returns a list of all words that can be formed by removing one letter.

#     word: string

#     Returns: list of strings
#     """
#     res = []
#     for i in range(len(word)):
#         child = word[:i] + word[i+1:]
#         if child in word_dict:
#             res.append(child)
#     return res


# def all_reducible(word_dict):
#     """Checks all words in the word_dict; returns a list reducible ones.

#     word_dict: dictionary with words as keys
#     """
#     res = []
#     for word in word_dict:
#         t = is_reducible(word, word_dict)
#         if t != []:
#             res.append(word)
#     return res


# def print_trail(word):
#     """Prints the sequence of words that reduces this word to the empty string.

#     If there is more than one choice, it chooses the first.

#     word: string
#     """
#     if len(word) == 0:
#         return
#     print word,
#     t = is_reducible(word, word_dict)
#     print_trail(t[0])


# def print_longest_words(word_dict):
#     words = all_reducible(word_dict)

#     # use DSU to sort by word length
#     t = []
#     for word in words:
#         t.append((len(word), word))
#     t.sort(reverse=True)

#     # print the longest 5 words
#     for length, word in t[0:5]:
#         print_trail(word)
#         print '\n'

# print_longest_words(word_dict)

# if __name__ == '__main__':
#     word_dict = make_word_dict()
#     print_longest_words(word_dict)