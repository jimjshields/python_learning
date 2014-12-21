'''
take a directory of markdown (.md) files and produce a directory 
of .html files for a website

useful tool for using static files - great for a blog

want one (or several?) .md file to be converted into an html file

see markdown (https://pypi.python.org/pypi/Markdown) for actual package
reference docs (https://pythonhosted.org/Markdown/reference.html)
'''

#!/usr/bin/env python

import sys
import utils
import markdown
import os

# get the source directory
source = sys.argv[1]

# get the target directory
target = sys.argv[2]

utils.convert_md_directory(source, target)
