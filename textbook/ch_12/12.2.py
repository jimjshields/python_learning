import math
import random

def sort_by_length_rand(words):
    w = []
    for word in words:
        w.append((len(word), random.random(), word))
    w.sort(reverse = True)
    
    res = []
    for length, rand, word in w:
        res.append(word)
    print res
    
words = 'cool', 'beans', 'bean', 'cool beans'

sort_by_length_rand(words)