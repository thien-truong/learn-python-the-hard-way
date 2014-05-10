from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file)
indata = input.read()

print "Does the to file exists?"
print exists(to_file)

output = open(to_file, 'w')
outdata = output.write(indata)

input.close()
output.close()