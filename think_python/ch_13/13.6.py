# dictionary subtraction - didn't do the whole thing, just the idea of set subtraction

def subtract_sets(book_words, word_list):
	"""input: all words in book (type: iterable),
			  all words in word list (type: iterable)
	   output: all words in book that aren't in the word list (type: set)"""
	return set(book_words) - set(word_list)