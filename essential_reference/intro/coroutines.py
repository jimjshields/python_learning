def print_matches(matchtext):
	print "Looking for", matchtext
	while True:
		line = (yield) # the coroutine
		if matchtext in line:
			print line

# using it - kind of weird, but effectively just creating a function to traverse through whatever you send it
matcher = print_matches("python")

matcher.next()

matcher.send("Hello world")
matcher.send("python is cool")
# python is cool
matcher.send("yow!")

matcher.close()