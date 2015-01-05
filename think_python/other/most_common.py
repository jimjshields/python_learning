### modules ###

import string  # module that has string operations below 

### functions ###

def process_file(filename): # function to build dictionary of words and frequencies for a file
    hist = dict()  # hist is the empty dictionary
    fp = open(filename)  # fp is the opened file
    for line in fp:  # running through each line in the opened file
        process_line(line, hist)  # process that line using the process_line function
    return hist   # returning the dictionary
    
def process_line(line, hist):  # function to take a single line in a file, strip punctuation, and separate ('split') into strings
    line = line.replace('-', ' ')  # method to replace hyphens with spaces
    
    for word in line.split():  # going through each separate string in the line, using the split method to separate the strings
        word = word.strip(string.punctuation + string.whitespace)   # strip method removes punctuation and whitespace
        word = word.lower()    # converts each word to lowercase
        
        hist[word] = hist.get(word, 0) + 1    # if the word is in the dictionary, increase the count by one; if not, add it with a value of 0 (then add 1)
        
def most_common(hist):    # function to build a list of tuples - the words and frequencies - and sorting in desc order
    t = []    # empty list
    for key, value in hist.items():     # for each key and value in the items of the dictionary
        t.append((value, key))  # add the value, then the key, to the list (in a tuple - so they can be sorted)
    
    t.sort(reverse=True)    # sort desc
    return t    # return the list of sorted items

def print_most_common(hist, num=10):    # function to print the most common num (if provided, else 10) words

    t = most_common(hist)   # setting t (separate from above t) equal to the above function run on the processed file
    
    print 'The most common words are:'  # a string
    for freq, word in t[:num]:   # going through the top num most frequent words
        print word, '\t', freq  # printing the word, a tab, and the frequency

### setting variables ###

hist1 = process_file('exposures.txt')    # process this file, set it equal to hist (separate from above hist)
hist2 = process_file('text.txt')

### calling functions ###

print_most_common(hist1, 10)
print_most_common(hist2, 10)