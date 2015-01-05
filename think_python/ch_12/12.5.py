# metathesis pair: can transform one into the other by swapping two letters

# best way:
# find all anagrams
# within those anagrams, check each word to see if it has a pair
# if it does, add the pair to the list

def signature(word):
	t = list(word)
	t.sort()
	t = ''.join(t)
	return t

def anagram_list(words):
    anagrams = {}
    for word in words:
    	t = signature(word)
        if t in anagrams:
            anagrams[t].append(word)
        else:
            anagrams[t] = [word]
    anagram_list = []
    for key in anagrams:
        anagram_list.append(anagrams[key])
    return anagram_list

def word_distance(word1, word2):
	assert len(word1) == len(word2)

	count = 0
	for c1, c2 in zip(word1, word2):
		if c1 != c2:
			count += 1

	return count

def find_metathesis(anagrams):
	metathesises = []
	for i in anagrams:
		for word1 in i:
			for word2 in i:
				if word1 < word2 and word_distance(word1, word2) == 2:
					print word1, word2

find_metathesis(anagram_list(['cool', 'beans', 'blah', 'bleh', 'albh', 'balh', 'cool', 'ocol', 'ebans', 'beasn']))