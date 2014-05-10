ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # If no index is specified, a.pop() removes and returns the last item in the list
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's {} items now.".format(len(stuff))
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #[-1] is the index of last item on list
print stuff.pop() #a.pop() removes and returns the last item on the list
print ' '.join(stuff)# join all items on list using a space between the items
print '#'.join(stuff[3:5]) # join items on index 3 and 4 using a # between them
