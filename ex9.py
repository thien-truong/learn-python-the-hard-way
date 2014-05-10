# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFed\nMar\nApr\nMay\nJun\nJul\nAug"

# note: the comma add an extra space in the printing result
print "Here are the days: ", days
print "Here are the months: ", months

print "Here are the days: {!s}".format(days)
print "Here are the months: {!s}".format(months)

print "Here are the days: " + days
print "Here are the months: " + months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
"""