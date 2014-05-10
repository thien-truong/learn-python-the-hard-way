print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're {} old, {} tall and {} heavy.".format(
    age, height, weight)

age = raw_input('How old are you? ')
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print age, height, weight
    
print "What is your firstname?"
first_name = raw_input()
print "What is your lastname?"
last_name = raw_input()
print "What city do you live in?"
city = raw_input()
print "How many children to you have?"
number_of_children = raw_input()
print "How many apple have you eaten?"

#to convert a string to a float
apple_eaten = float(raw_input())
cost_of_apple_eaten = apple_eaten *.23

print "My name is {} {}.".format(first_name, last_name)    
#Python does not support this syntax:  print "My father's name is {}.".format(father_name = raw_input())
print "My father lives in {}.".format(city)
print "Today I ate {} apple and it costs {} dollars.".format(apple_eaten, cost_of_apple_eaten)
