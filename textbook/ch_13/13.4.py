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

def create_word_list(word_file):
    words = open(word_file)
    word_dict = {}
    for word in words:
        word_dict[word.strip('\r\n')] = None
    return word_dict

def check_words(book_words, word_dict):
    unique_words = []
    for word in book_words:
        if word not in word_dict:
            unique_words.append(word)
    return unique_words

book = sys.argv[1]

book_words = process_file(book)
words = create_word_list('words.txt')

print check_words(book_words, words)