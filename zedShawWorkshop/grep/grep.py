import re
import os

def convert_patterns(patterns):
	results = []

	# for each patterns
	for pattern in patterns:
		# make a regex with it
		expr = re.compile(pattern)
		# add the regex to the empty list
		results.append(expr)

def troll_directories(start):
	results = []

	# troll for all the directories like in find.py
	# traverse the directories for all files
	for root, dirs, files in os.walk('.'):
		for fname in files:
			# join root and fname
			path = os.path.join(root, fname)
			# put the full path into the results
			results.append(path)

	return results

def apply_patterns(files, patterns):
	# for each files in files
	for fname in files:
		# open the file and read the lines
		lines = open(fname).readlines()
		for num, line in enumerate(lines):
			# for each pattern
			for pattern in patterns:			
				# if pattern found in lines
				if pattern.search(lines):
					# print file, line number, line
					print "%s:%d: %s" % (os.path.join(fname), num+1, line),
					# comma forces it not to start a new line