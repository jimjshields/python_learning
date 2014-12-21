import re
import os
import markdown

def convert_markdown(doc):
	# open the .md version of doc
	contents = open("docs/" + doc + ".md").read()
	# convert to markdown
	html = markdown.markdown(contents)
	# return to browser
	return html