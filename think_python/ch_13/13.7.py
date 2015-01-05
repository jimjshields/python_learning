# for whitespace, punctuation
import string
# for getting an argument
import sys
import random
from bisect import bisect

def process_file(filename):
    # read file
    f = open(filename)
    # header hasn't been passed yet
    header = False
    # dict for words/counts
    hist = dict()
    # break each line into words
    for line in f:
        # once header is passed
        if "THE SMALL PRINT! FOR PUBLIC DOMAIN ETEXTS" in line:
            header = True
        if header:
            # clean up the line of whitespace/punctuation
            process_line(line, hist)

    return hist

def process_line(line, hist):
    line = line.replace('-', '')
    for word in line.split():
        # strip whitespace and punctuation
        word = word.strip(string.punctuation + string.whitespace)
        # convert to lowercase
        word = word.lower()
        # add 1 to histogram - default to 0 if not there yet
        hist[word] = hist.get(word, 0) + 1

word_freq = process_file('emma.txt')
keys = word_freq.keys()

freq_list = [freq for freq in word_freq.values()]

def build_cumul_freq_lists(word_freq):
    """input: dict of words and frequencies
       output: one list of words, one list of cumulative frequencies"""
    words = []
    freqs = []
    total_freq = 0
    for word, freq in word_freq.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)
    return words, freqs

def find_random_word_weighted(words, freqs):
    """input: ordered list of words, ordered list of cumulative frequencies
       output: random word weighted for frequency"""
    high = max(freqs) - 1
    low = 0
    rand_num = random.randint(low, high)
    index = bisect(freqs, rand_num)
    return words[index]

words, freqs = build_cumul_freq_lists(word_freq)
print find_random_word_weighted(words, freqs)