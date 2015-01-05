# for whitespace, punctuation
import string

def process_file(filename):
    # read file
    f = open(filename)
    # break each line into words
    for line in f:
        # clean up the line of whitespace/punctuation
        process_line(line)

def process_line(line):
    for word in line.split():
        # strip whitespace and punctuation
        word = word.strip(string.punctuation + string.whitespace)
        # convert to lowercase
        word = word.lower()
        print word


process_file('sherlock.txt')