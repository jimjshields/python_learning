# importing the argv function from the sys module
from sys import argv

# assigning the two variables (script, filename) to argv - you must type into the terminal
script, filename = argv

# setting txt as a variable to contain the opened file
txt = open(filename)

# printing a response to the user with the filename
print "Here's your file %r:" % filename

# printing the contents of the file
print txt.readlines()

# asking for the filname again
print "Type the filename again:"

# prompting for the filename
file_again = raw_input("> ")

# setting txt_again = to opening the prompted filename
txt_again = open(file_again)

# printing the contents of the file just entered
print txt_again.read()

txt.close()
txt_again.close()