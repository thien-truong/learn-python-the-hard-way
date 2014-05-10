print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: {}".format(five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: {}".format(start_point)
print "We'd have {:d} beans, {:d} jars, and {:d} crates.".format(beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have {:d} beans, {:d} jars, and {:d} crates.".format(*secret_formula(start_point))

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition
are requires and explanation
\n\t\twhere there is non.
"""

print "--------------"
print poem
print "-" * 14

five = 10 - 2 + 3 - 6
print "This should be five: {!s}".format(five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates #This function returns 3 values
    
start_point = 10000
beans, jars, crates = secret_formula(start_point) # Assign 3 returned values to 3 variables

print "With a starting point of:  {:d}".format(start_point)
print "We'd have {:d} beans, {:d} jars, and {:d} crates.".format(beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"

# Without the * in front of secret_formula, python gave a value error: unknow format code 'd' for object of type 'str'
print "We'd have {:d} beans, {:d} jars, and {:d} crates.".format(*secret_formula(start_point))