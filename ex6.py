x = "There are {} types of people.".format(10)
binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}.".format(binary, do_not)

print x
print y

print "I said: {0!r}.".format(x)
print "I said: {!r}.".format(x)
print "I also said: '{!s}'.".format(y)

hilarious = False
very_funny = "Yes!"
joke_evaluation = "Isn't that joke so funny?! {!r}"

print joke_evaluation.format(hilarious)
print joke_evaluation.format(very_funny)

# joke_evaluation written below would yeild the same result, but everytime you try to print 
# joke_evaluation, the result would be FALSE.  Writing it like above is good because it could be
# saved as a template where different variables (such as hilarious and very_funny) could be set for {!r} 
# instead of just hilarious.

joke_evaluation = "Isn't that joke so funny?! {!r}".format(hilarious)
print joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# real world application:  using a person's first name and last name
first_name = "Adam"
last_name = "Russell"

# note that the space between Hello and {} and {} will print out as a space.  This is why string format 
# is much more convenient than the example below.
print "Hello {} {}!".format(first_name, last_name)
# or

# note that a space between each word must be manually put in.  Computer doesn't figure out by itself.
print "Hello " + first_name + " " + last_name + "!"