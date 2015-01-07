# 18.1
class Card(object):
	"""Represents a standard playing card."""

	def __init__(self, suit=0, rank=2):
		# default with 2 of clubs
		self.suit = suit
		self.rank = rank

# 18.2
class Card(object):
	"""Represents a standard playing card."""

	def __init__(self, suit=0, rank=2):
		# default with 2 of clubs
		self.suit = suit
		self.rank = rank

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank],
							 Card.suit_names[self.suit])

queen_of_diamonds = Card(1, 12)

# 18.3
class Card(object):
	"""Represents a standard playing card."""

	def __init__(self, suit=0, rank=2):
		# default with 2 of clubs
		self.suit = suit
		self.rank = rank

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank],
							 Card.suit_names[self.suit])

	def __cmp__(self, other):
		# check the suits
		if self.suit > other.suit: return 1
		if self.suit < other.suit: return -1

		# suits are the same... check ranks
		if self.rank > other.rank: return 1
		if self.rank < other.rank: return -1

		# ranks are the same... it's a tie
		return 0

	# or easier, using tuple comparison
	def __cmp__(self, other):
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		# cmp -> positive if first is larger, negative if second is, 0 if equal
		return cmp(t1, t2)

ace_of_spades = Card(3, 1)
queen_of_hearts = Card(2, 12)

# print "%s, %s, %s" % (queen_of_diamonds, queen_of_diamonds, queen_of_diamonds > queen_of_diamonds)

# ex 1
class Time(object):
	"""represents time in hours, minutes, seconds"""

	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __cmp__(self, other):
		t1 = self.hour, self.minute, self.second
		t2 = other.hour, other.minute, other.second
		return cmp(t1, t2)

time1 = Time(11, 30, 5)
time2 = Time(11, 30, 0)

# 18.4
class Deck(object):
	"""Represents a deck of cards"""

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

# 18.5
class Deck(object):
	"""Represents a deck of cards"""

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __cmp__(self, other):
		t1 = self.hour, self.minute, self.second
		t2 = other.hour, other.minute, other.second
		return cmp(t1, t2)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

# 18.6
import random

class Deck(object):
	"""Represents a deck of cards"""

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def __cmp__(self, other):
		t1 = self.hour, self.minute, self.second
		t2 = other.hour, other.minute, other.second
		return cmp(t1, t2)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

# ex 2
	def sort(self):
		self.cards.sort()

	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())

deck = Deck()
deck.sort()

# 18.7
class Hand(Deck):
	"""Represents a hand of playing cards."""

	def __init__(self, label=''):
		self.cards = []
		self.label = label

# ex 3
import random

class Deck(object):
	"""Represents a deck of cards"""

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def __cmp__(self, other):
		t1 = self.hour, self.minute, self.second
		t2 = other.hour, other.minute, other.second
		return cmp(t1, t2)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())

	def deal_hands(self, num_hands, cards_per_hand):
		self.shuffle()
		hands = []
		for i in range(1, num_hands + 1):
			hand = Hand(i)
			self.move_cards(hand, cards_per_hand)
			hands.append(hand)
		return hands

deck = Deck()
hands = deck.deal_hands(3, 5)

# ex 5

import sys
import string
import random

class Markov(object):


	def __init__(self):
		# global variables
		self.suffix_map = {}        # map from prefixes to a list of suffixes
		self.prefix = ()            # current tuple of words


	def process_file(filename, order=2):
	    """Reads a file and performs Markov analysis.

	    filename: string
	    order: integer number of words in the prefix

	    Returns: map from prefix to list of possible suffixes.
	    """
	    fp = open(filename)
	    skip_gutenberg_header(fp)

	    for line in fp:
	        for word in line.rstrip().split():
	            process_word(word, order)


	def skip_gutenberg_header(fp):
	    """Reads from fp until it finds the line that ends the header.

	    fp: open file object
	    """
	    for line in fp:
	        if line.startswith('*END*THE SMALL PRINT!'):
	            break


	def process_word(word, order=2):
	    """Processes each word.

	    word: string
	    order: integer

	    During the first few iterations, all we do is store up the words; 
	    after that we start adding entries to the dictionary.
	    """
	    if len(self.prefix) < order:
	        self.prefix += (word,)
	        return

	    try:
	        self.suffix_map[self.prefix].append(word)
	    except KeyError:
	        # if there is no entry for this prefix, make one
	        self.suffix_map[self.prefix] = [word]

	    self.prefix = shift(self.prefix, word)


	def random_text(n=100):
	    """Generates random wordsfrom the analyzed text.

	    Starts with a random prefix from the dictionary.

	    n: number of words to generate
	    """
	    # choose a random prefix (not weighted by frequency)
	    start = random.choice(self.suffix_map.keys())
	    
	    for i in range(n):
	        suffixes = self.suffix_map.get(start, None)
	        if suffixes == None:
	            # if the start isn't in map, we got to the end of the
	            # original text, so we have to start again.
	            random_text(n-i)
	            return

	        # choose a random suffix
	        word = random.choice(suffixes)
	        print word,
	        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(name, filename='', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    main(*sys.argv)

# ex 6
