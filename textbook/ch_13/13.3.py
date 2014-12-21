# for whitespace, punctuation
import string
# for getting an argument
import sys

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
        if "START OF THIS PROJECT GUTENBERG EBOOK" in line:
            header = True
        if header:        
            # clean up the line of whitespace/punctuation
            process_line(line, hist)

    word_count = []

    for word, count in hist.items():
        word_count.append((count, word))

    word_count.sort(reverse=True)
    return word_count[:19]

def process_line(line, hist):
    line = line.replace('-', '')
    for word in line.split():
        # strip whitespace and punctuation
        word = word.strip(string.punctuation + string.whitespace)
        # convert to lowercase
        word = word.lower()
        # add 1 to histogram - default to 0 if not there yet
        hist[word] = hist.get(word, 0) + 1

book = sys.argv[1]

print process_file(book)