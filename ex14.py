from sys import argv

script, user_name = argv
prompt = '> '

print "Hi {}, I'm the {} script.".format(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me {}?".format(user_name)
likes = raw_input(prompt)

print "Where do you live {}?".format(user_name)
lives = raw_input(prompt)

# This line will prints the answer twice because it has both a print and a raw_input
print raw_input("Where do you live {}?".format(user_name))

print "What kind of computer do you have?"
computer = raw_input(prompt)
raw_input("What kind of computer do you have? ")
 

print """
Alright, so you said {} about liking me.
You live in {}.  Not sure where that is.
And you have a {} computer.  Nice.
""".format(likes, lives, computer)

