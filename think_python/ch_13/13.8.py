# for whitespace, punctuation
import string
# for getting an argument
import sys
import random

def process_line(line, book_word_list):
    """input: a single line of text, a list of words from the text
       output: the list adds those words stripped of whitespace and punctuation"""

    line = line.replace('-', '')
    for word in line.split():
        # strip whitespace and punctuation
        word = word.strip(string.whitespace) #string.punctuation + 
        # convert to lowercase
        word = word.lower()
        # add word to the list in order
        book_word_list.append(word)

def create_book_word_list(filename):
    """input: a text filename
       output: a list of every word, in order, from the text"""

    # read file
    f = open(filename)
    
    # header hasn't been passed yet
    header = False
    
    # empty lists for every book word
    book_word_list = []
    
    # break each line into words
    for line in f:
        # once header is passed
        if "THE SMALL PRINT! FOR PUBLIC DOMAIN ETEXTS" in line:
            header = True
        if header:
            # adds all words in the line to the list
            process_line(line, book_word_list)

    return book_word_list

def create_suffix_dict(book_word_list, prefix_length):
    """input: list of words in a book, length of prefix you want
       output: dictionary of all possible prefixes of length prefix_length
       and a list of the respective suffixes"""

    prefixes = []
    suffix_dict = {}

    # adds all possible prefixes to the list
    for i in range(len(book_word_list) - (prefix_length)):
        prefix = []
        # add all words up to prefix_length
        for n in range(prefix_length):
            prefix.append(book_word_list[i + n])
        prefix = ' '.join(prefix)

        # grab the suffix
        suffix = book_word_list[i + prefix_length]

        # if it's not in the dict yet, initialize with the first suffix
        if prefix not in suffix_dict:
            suffix_dict[prefix] = [suffix]
        # if it is, add the new suffix
        else:
            suffix_dict[prefix].append(suffix)
    
    return suffix_dict

book_word_list = create_book_word_list('emma.txt')

def random_prefix_suffix(suffix_dict, prefix, prefix_length):
    """input: dictionary of prefixes/suffixes, given prefix
       output: string of the prefix and a randomly chosen suffix, 
       and string of the new prefix"""

    words = []
    random_suffix = random.choice(suffix_dict[prefix])
    
    prefix_list = prefix.split()

    for word in prefix_list:
        words.append(word)

    words.append(random_suffix)

    words_string = ' '.join(words)
    new_prefix = ' '.join(words[(len(words) - prefix_length):])

    return words_string, new_prefix, random_suffix

def generate_markov_text(prefix_length, text_length=100):
    """input: dictionary of prefixes/suffixes
       output: random selection of text based on the dictionary"""
    
    suffix_dict = create_suffix_dict(book_word_list, prefix_length)
    text = []
    for i in range(text_length):
        if i == 0:
            # pick the first prefix randomly
            prefix = random.choice(suffix_dict.keys())
            words_string, prefix, suffix = random_prefix_suffix(suffix_dict, prefix, prefix_length)
            text.append(words_string)
        else:
            # get the full prefix/suffix combo, and a new prefix
            words_string, prefix, suffix = random_prefix_suffix(suffix_dict, prefix, prefix_length)
            # add it to the text
            text.append(suffix)
    text = ' '.join(text)
    return text

print generate_markov_text(5)