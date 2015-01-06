# 18.1
class Card(object):
	"""Represents a standard playing card."""

	def __init__(self, suit=0, rank=2):
		# default with 2 of clubs
		self.suit = suit
		self.rank = rank
