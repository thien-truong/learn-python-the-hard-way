from sys import argv

script, input_file = argv

# this function is to print the whole file
def print_all(f):
    """Print the whole file."""
    print f.read()
# f.tell() returns an interger giving the file object's current position in the file, 
# measured in bytes from the beginning of the file. 
# To change the file object's position, use f.seek(offset, from_what).  
# The position is computed from adding offset to a reference point; the reference point is
# selected by the from_what argument.  
# A from_what value of 0 measures from the beginning of a file, 1 uses the current file position,
# and 2 uses the end of the file as the reference point.  from_what can be omited and defaults to 0,
# using the beginning of the file as the reference point.

# this definition function is to go to the beginning of the file after reading it
def rewind(f):
    """Go to the beginning of the file."""
    f.seek(0)
  
# this function is to print the line number and it's content    
def print_a_line(line_count, f):
    print line_count, f.readline() # f.readline() reads a single line from the file.
    
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a type."

rewind(current_file)

print "Let's print three lines:"

# line_count = current_line = 1 ---> The current line is line one
current_line = 1
print_a_line(current_line, current_file)

# line_count now is current_line plus 1 = 2 ---> The current line is two
current_line = current_line + 1
print_a_line(current_line, current_file)

# line_count is now current_line (which is line#2) plus one ---> The current line is three
current_line = current_line + 1
print_a_line(current_line, current_file)
