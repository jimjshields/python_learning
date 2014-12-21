# 1
def anagram_list(words):
    anagrams = {}
    for word in words:
        word_tuple = tuple(sorted(list(word)))
        if word_tuple in anagrams:
            anagrams[word_tuple].append(word)
        else:
            anagrams[word_tuple] = [word]
    anagram_list = []
    for key in anagrams:
        anagram_list.append(anagrams[key])
    return anagram_list

print anagram_list(['cool', 'beans', 'oocl'])

# 2
def anagram_list_sorted(anagram_list):
    count = []
    for anagrams in anagram_list:
        count.append((len(anagrams), anagrams))
    count.sort(reverse=True)
    new_count = []
    for i in count:
        new_count.append(i[1])
    return new_count

print anagram_list_sorted(anagram_list(['cool', 'beans', 'oocl', 'abc', 'cba', 'bca']))

# 3
# just use the thing above and take the top one out of a set of words

def find_max_scrabble(anagram_list_sorted):
    return anagram_list_sorted[0]