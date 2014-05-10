from sys import argv

script, filename = argv

# A file must be opened before it can be read/print
txt = open(filename)

print "Here's your file {}:".format(filename)

# You can give a file a command (or a function/method) by using the . (dot or period),
# the name of the command, and parameteres.
print txt.read() # call a function on txt.  "Hey txt! Do your read command with no parameters!"

# it is important to close files when you are done with them
txt.close()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

