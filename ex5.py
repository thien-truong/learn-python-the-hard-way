name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "My name is %s. Let's talk about %s." % (name, name)

# the brackets and characters within them (called format fields) are replaced with 
# the objects passed into the str.format() method. A number in the brackets refers 
# to the position of the object passed into the str.format() method. 
print "My name is {0}. Let's talk about {0}.".format(name)

print "My name is {}.  Let's talk about {}.".format(name, name)
print "He's %d inches tall." % height
print "He's {} inches tall.".format(height)
print "He's {} inches tall. His friend is {} inches tall.".format(height, 5)

#.format(height, eyes) is called a positional argument
print "He's {0} inches tall.  His friend is also {0} inches tall.  His mom has {1} eyes.".format(height, eyes)

# If keyword arguments are used in the str.format() method, their values are referred to by using the name of
# the argument.  This type is called "keyword argument."  Since the keywords (such as "type" and "kind" is specified,
# the order of the argument does not matter.
print "He's a {type}. While his cat's a {kind}.".format(type = 'human', kind = "mamal")
print "He's %d pounds heavy." % weight
print "He's {} pounds heavy.".format(weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "He's got {} eyes and {} hair.".format(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "His teeth are usually {} depending on the coffee.".format(teeth)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
print "If I add {}, {}, and {} I get {}.".format(
    age, height, weight, age + height + weight)

