# from sys import argv
from os.path import exists

# script, from_file, to_file = argv

from_file = raw_input("Which file would you like to copy from?")
to_file = raw_input("Which file would you like to copy to?")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "Alright, all done."