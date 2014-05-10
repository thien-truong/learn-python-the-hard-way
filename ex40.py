# Dictionary is an unordered set of key:value pairs, with the requirements that the keys are unique (within one dictionary).
# The main operations on a dicitonary are storing a value with some key, and extracting the value given the key
# An object is "hashable" if it has a hash value which never changes during its lifetime, and can be compared to other objects.
# Hasability makes an object usable as a dictionary key and a set memeber, because these data structures use the hash value internally.
# Keys can be any immutalbe type.
# An immutalbe object is an object with fixed value.  Immuatalbe objects include numbers, strings, and tuples.  Such an object
# cannot be altered.  A new object has to be created if a different value has to be stored.  They play an importlant roll in places
# where a constant hash value is needed, for example as a key in a dictionary.
tel = {'jack': 4098, 'sape': 4194, 'gust': 2847}
print tel
# adding 'guido': 4132 to the dictionary
tel['guido'] = 4132
print tel
# delete key:value pair 'jack': 4098
del tel['jack']
# the "keys" method of a dictionary object returns a list of all the keys in the dictionary (in arbitrary order)
print tel.keys()
# to check whether a single key is in the dictionary, use the "in" keyword
print 'jack' in tel
print 'sape' in tel 
# len(d) retuns the number of items in dictionary d
print len(tel)
# get(key[, default]) return the value for key if key is in the dictionary, else default.
# If "default" is not given, it defaults to None, so that this method never raises a Keyerror.
print tel.get('sape') 
# copy() returns a shallow copy of the dictionary
print tel.copy()
# items() return a copy of the dictionary's list of (key, value) pairs
print tel.items()

# clear(d) removes all items in dictionary d



cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Looping through dictionaries is looping though its keys
# items() return a copy of the dictionary's list of (key, value) pairs
for state, city in cities.items():
    print state, city
    
# iterating through the keys and print out the keys (same as cities.keys())
for state in cities:
    print state
    
# iterating through the keys to pull the values from dictionary   
for state in cities:
    print cities[state]

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"
        
# ok pay attention! 
# Reassigning find_city to the variable cities['_find'].  Nothing to do with dictionary.
# Put in here to mess up our head.
cities['_find'] = find_city

while True:
    print "state? (ENTER to quit)",
    state = raw_input("> ")
    # "break" allows user to exit when enter is pressed.  Otherwise when user press enter, "State? (Enter to quit)" will
    # keep running
    if not state: break

    # This line is the most important line
    # city_found = calling the "find_city" function with the "cities and state" as arguements
    city_found = cities['_find'](cities, state)
    print city_found
    
    
    

