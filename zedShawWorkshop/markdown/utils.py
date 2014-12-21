import os

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

def discover_targets(files):
	results = []
	for source_file in files:
	# strip extension of source file
		base, ext = os.path.splitext(fname)
		path = base[len(source)+1:]
		target_dir = os.path.dirname(os.path.join(target, path))

		# check if directory exists
		if not os.path.exists(path):
			os.makedirs(target_dir)
		else:
			pass

		# append .html to the file name
		target_file = os.path.join(target_dir + '.html')
		results.append((source_file, target_file))

def generate_html(source_file, target_file):
	# open the source file
	contents = open(source).read()
	# convert to markdown
	html = markdown.markdown(contents)

	# open output with .html
	with open(target, 'w') as f:
		# write html to the .html
		f.write(html)

def convert_md_directory(source, target):
	# get all the files in the source
	sources = utils.troll_directories(source)
	targets = utils.discover_targets(source, target, sources)

	for source_file, target_file in targets:
		utils.generate_html(source_file, target_file)