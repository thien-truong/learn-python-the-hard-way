# open() returns a file object, and is mostly commonly used with two arguments:  open(filename, mode).
# The first argument is a string containing the filename.  
# The second argument is another string containing a few characters describing the way in which the file will be used.
# mode can be 'r' when the file will only be read
# 'w' for only writing (an existing file with the same name will be erased)
# 'a' opens the file for appending, any data wrtten to the file is automatically added to the end
# 'r+' opens the file for both reading and writing <--- tried this, didn't work
# The mode arguement is optional, 'r' will be assumed if it's omitted

from sys import argv

script, filename = argv

#print "We're going to erease {}.".format(filename)
#print "If you don't want that, hit CTRL-C (^C)."
#print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# the lines above could also be comebined like this:
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# you could also write a string.  Note how to use \ to escape the single quote?
target.write('I\'m a fish' + "\n")
target.write('I\'m a fish\n')

# or if you already knows about loops, do this:
for line in (line1, line2, line3):
    target.write(line + "\n")

target = open(filename)
print target.read()

#target = open(filename, 'w')
#target.truncate()

print "And finally, we close it."
target.close()
