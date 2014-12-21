# importing argv from sys module
from sys import argv

# assigning variables to argv - must type in command line
script, input_file = argv

# defining print_all function
def print_all(f):
# it prints f - the file in the command line
	print f.read()
	
# defining the rewind function
def rewind(f):
# it goes to the beginning of the file
	f.seek(0)
	
# defining the print_a_line function
def print_a_line(line_count, f):
# it prints "line_count" (an argument) and one line of the file - the line it's on
	print line_count, f.readline(),
	
# defining current_file as the opening of the input_file
current_file = open(input_file)

# printing some nonsense
print "First let's print the whole file:\n"

# printing the entire file
print_all(current_file)

# printing some nonsense
print "Now let's rewind, kind of like a tape."

# rewinding the file
rewind(current_file)

# printing some nonsense
print "Let's print three lines:"

# starting at the first line
current_line = 1
# printing the first line
print_a_line(current_line, current_file)

# moving to the next line
current_line += 1
# printing that line
print_a_line(current_line, current_file)

# moving to the next line
current_line += 1
# printing that linepyth
print_a_line(current_line, current_file)	