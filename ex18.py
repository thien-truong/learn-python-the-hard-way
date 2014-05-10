# Fuctions: name the pieces of code the way ravirables name strings and numbers.  
# They take arguments the way your scripts take argv
# They let you make "tiny commands"

# this one is like your scripts with argv
# this function is called "print_two", inside the () are arguments/parameters

# This is like your script with argv
# The keyword def introduces a function definition.  It must be followed by the
# function name and the parenthesized list of formal parameters.  The statements that
# form the body of the function start at the next line, and must be indented.
def print_two(*args):
    """print 2 arguments.""" # This is a docstring or documentation string. It should concisely sumarize the object's purpose
    arg1, arg2 = args
    print "arg1: {}, arg2: {}".format(arg1, arg2)
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: {}, arg2: {}".format(arg1, arg2)
    
# This just takes one argument
def print_one(arg1):
    print "arg1: {}".format(arg1)
    
# This one takes no arguments:

def print_none():
    print "I got nothing'."
    
print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("First!")
print_none()
