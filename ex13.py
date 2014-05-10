# argv = argument variable, which holds the arguments you pass to your Python
# script when you run it.
from sys import argv
# modules give features

script, first, second, third = raw_input(argv)

# the lines below unpacks argv so that rather than holding all the arguments, 
# it gets assigned to four variables you can work with: script, first, second, third
print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third

print "The script is called: {}".format(script)
print "The first variable is: {}".format(first)
print "The second variable is: {}".format(second)
print "The third variable is: {}".format(third)