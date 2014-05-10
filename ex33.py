# WHILE-LOOP
# A while-loop will keep executing the code block under it as long as a boolean expression is True.
# In other words, instead of running the code block once, it jumps back
# to the "top" where the while is, and repeat.  It keeps doing this until the expression is False.
# Problem with while-loops:  sometimes they do not stop.
# To avoid: make sure to use while-loops sparingly (usually for-loop is better).
# Review while statements and make sure that the thing be tested will become False at some point.
# When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing


def printing_list(int, increment):
    i = 0   
    numbers = []

    while i < int:
        print "At the top i is {}".format(i)
        numbers.append(i)
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is {}".format(i)
    
    print "The numbers: "

    for num in numbers:
        print num
    
printing_list(7, 2)

def printing_list_1(int, increment):
    #i = 0       
    numbers = []
    
    for i in range(0, int, increment):
        if i < int:
            print "At the top i is {}".format(i)
            numbers.append(i)
            i = i + increment
            print "Numbers now: ", numbers
            print "At the bottom i is {}".format(i)
            
printing_list_1(89, 9)