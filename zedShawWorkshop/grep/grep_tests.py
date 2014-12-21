from nose.tools import *
from grep import utils
import re

def test_convert_patterns():
	# test that i can convert pattenrs to expressions
	results = utils.convert_patterns(['.*.py'])
	# asset that they are equal to my expectations
	asset_equal(results, [])

def test_troll_directories():
	# given a directory, return all of its contents
	results = utils.troll_directories('.')
	# asset that we have the same contents
	assert_true('./NOTES' in results)

def test_apply_patterns():
	# get a list of directories
	files = utils.troll_directories('test')
	patterns = utils.convert_patterns(['test_'])
	# apply a simple pattern on them
	utils.apply_patterns(files, patterns)
	# assert that we get the right results