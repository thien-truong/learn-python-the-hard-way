from sys import argv

script, input_file = argv

def print_whole_file(file_to_print):
    print(file_to_print.read())
    
def return_to_beginning_of_file(some_file):
    some_file.seek(0)
    
def print_line(line_count, file_object):
    print line_count, file_object.readline()

    
current_file = open(input_file)

print_whole_file(current_file)

return_to_beginning_of_file(current_file)

current_line = 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line, current_file)

    
    