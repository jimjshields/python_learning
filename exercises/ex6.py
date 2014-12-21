# defining x
x = "There are %d types of people." % 10
# defining binary
binary = "binary"
# defining do_not
do_not = "don't"
# defining y with multiple strings
y = "Those who know %s and those who %s." % (binary, do_not)

# printing x
print x
# printing y
print y

# printing string with x
print "I said: %r." % x
# printing string with y
print "I also said: '%s'." % y

# defining hilarious
hilarious = False
# defining joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# printing joke_evaluation with hilarious
print joke_evaluation % hilarious

# defining w
w = "This is the left side of..."
# defining e
e = "a string with a right side."

# printing w and e
print w + e
