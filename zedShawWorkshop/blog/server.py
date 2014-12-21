### all unfinished - lost track and just watched ###

#!/usr/bin/env python

from flask import Flask
import markdown
import utils
import os
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	# convert the markdown
	html = utils.convert_markdown("index")
	# render the template with contents
	# return to browser
	return render_template("layout.html", body=html)

# if they go to .html, serve that .md file
# /stuff/index.html
# /foo.html
@app.route("/<doc>.html")
def md_file(doc):
	return utils.convert_markdown(doc)

# if they go to any other directory, serve that index.html
# /stuff/
# /hello/there/you/
### unfinished ###
@app.route("/<subdir>/")
def sub_directory(subdir):
	path = os.path.join(subdir, "index")
	return utils.convert_markdown(path)

@app.route("/edit/<doc>.html")
def edit(doc):
	return render_template("edit.html", doc=doc, content = contents)

if __name__ == "__main__":
    app.run()