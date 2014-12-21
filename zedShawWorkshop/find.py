#!/usr/bin/env python
import sys
import re
import os

# get the patterns from the cmd line arguments
pattern = sys.argv[1]

# convert them to regular expressions
expr = re.compile(pattern)

# traverse the directories for all files
for root, dirs, files in os.walk('.'):
	for fname in files:
		# if a file matches the pattern, print its name
		if expr.search(fname):
			print os.path.join(root, fname)