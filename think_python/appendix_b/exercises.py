# 4 - hashtables
# implementing a hashtable without using dictionaries

class LinearMap(object):

	def __init__(self):
		self.items = []

	def add(self, k, v):
		self.items.append((k, v))

	def get(self, k):
		for key, val in self.items:
			if key == k:
				return val
		raise KeyError

# essentially creates a list of n empty objects which are filled in only when add is called
# hash function finds the index (somehow)

class BetterMap(object):

	def __init__(self, n=100):
		self.maps = []
		for i in range(n):
			self.maps.append(LinearMap())

	def find_map(self, k):
		index = hash(k) % len(self.maps)
		return self.maps[index]

	def add(self, k, v):
		m = self.find_map(k)
		m.add(k, v)

	def get(self, k):
		m = self.find_map(k)
		return m.get(k)