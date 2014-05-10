# WHAT IF
# An if statement creates what is called a "branch" within the code. 

people = 20
cats = 30
dogs = 15

# If this statement is True, then run the code under it, otherwise skip it."
if people < cats:
    print "Too many cats! The world is doomed!"
    
if people > cats:
    print "Not many cats! The world is saved!"
    
if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"
    

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs."
    
if people == dogs:
    print "People are dogs."