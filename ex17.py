from sys import argv
# exists returns True if a file exists, based on its name in a string as an argument.
# exists returns False if a not.
# from os.path import exists

script, from_file, to_file = argv

#print "Copying from {} to {}".format(from_file, to_file)

# We could do these two on one line too, how?
input = open(from_file)
indata = input.read()

# Do this instead if you only want to open this file once, read it and never touch it again.
# Other wise, use the medthod above
# indata = open(from_file).read()

#print "The input file is {} bytes long".format(len(indata))

#print "Does the output file exist? {}".format(exists(to_file))
#print "REady, hit RETURN to continue, CRTL-C to abort."
#raw_input()

output = open(to_file, 'w')
output.write(indata)

#print "Alright, all done."

output.close()
input.close()

