#Dictionaries, Oh Lovely Dictionaries - Online Version
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff['name']
print stuff['height']
stuff['city'] = "San Francisco"
print stuff['city']

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]
print stuff[2]
print stuff

del stuff['city']
del stuff[1]
del stuff[2]
print stuff

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'California',
    'MI': 'Michigan',
    'FL': 'Florida'
}


# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cites dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
# items() return a copy of the dictionary's list of (key, value) pairs
print '-' * 10
for state, abbrev in states.items():
    print "{} is abbreviated {}".format(state, abbrev)
    
# print every city in state
print '_' * 10
for abbrev, city in cities.items():
    print "{} has the city {}".format(abbrev, city)
    
# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
    print "{} state is abbreviated {} and has city {}".format(state, abbrev, cities[abbrev])

# get(key[, default]) return the value for key if key is in the dictionary, else default.
# If "default" is not given, it defaults to None, so that this method never raises a Keyerror.   
print '-' * 10
# safely get a abbreviation by that that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."
    
# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is:  {}".format(city)