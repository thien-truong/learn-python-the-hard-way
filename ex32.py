# LOOPS AND LIST
# A list is a container of things that are organized in order.  The list starts with the [ (left bracket) and
# ends with the ] (right bracket), the items in the list are separated by commas. 

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print "This is count {:d}".format(number)
    
# same as above
for fruit in fruits:
    print "A fruit of type: {}".format(fruit)
    
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got {}".format(i)

# we can also build lists, first start with an empty one
# elements is called a list objects.
# The list data type has some methods:  
# list.append(x) -- add an item to the end of the list
# list.extend(L)
# list.insert(i, x) -- where i is the index of the element before which to insert
# list.remove(x) -- remove the first item from the list whose value is x
# list.pop([i]) -- remove the item at the given position in the list, and return it.
# list.index(x) -- return the index in the list of the first item whose value is x
# list.count(x) -- return the number of times x appears in the list
# list.sort() -- sort the items of the list, in place
# list.reverse() -- reverse the elements of the list, in place

elements = []

# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
    #print "Adding {} to the list.".format(i)
    # append is a function that lists understand
    #elements.append(i)
 
# using extend instead of append would give same result as above 
# if use append, the result would print:  Element was: [0, 1, 2, 3, 4, 5]
elements.extend(range(0, 6))
    
elements.append('fish')
elements.append('eggs')
    
for i in elements:
    print "Element was: {}".format(i)
    
# Write a list of number that is the square of the numbers which start from 0 to 30 in increments of 5.
numbers = []
for number in range(0, 30, 5):
    numbers.append(number**2)
    
numbers.extend(range(2, 7))
numbers.append(range(2, 7))

for number in numbers:
    print "This number is {}".format(number)
