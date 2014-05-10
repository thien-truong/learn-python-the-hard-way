# del statement: to remove an item from a list given its index intead of its value.
# it can also be used to remove slices from a list or clear the entire list.

a = [-1, 1, 66.25, 333, 4039, 28.9, 348.245]
del a[0] # Remove value of index 0 from list a
print a # result: [1, 66.25, 333, 4039, 28.9, 348.245]
del a[2:4] #Remove value of index 2 and 3 (from 2 to before 4)
print a # result: [1, 66.25, 28.9, 348.245]
del a[-1] # Remove the last value in the list
print a

a = [-1, 1, 66.25, 333, 4039, 28.9, 348.245, 3, 5, 92, 86]
del a[:5] # Remove everything before index 5
print a # result: [28.9, 348.245, 3, 5, 92, 86]
del a[2:] # Remove everything starting from index 2 to end
print a # result [28.9, 348.245]
del a[:] # Remove everything
print a # result []

# There are at least 2 types of distinguishable kinds of errors: Syntax Errors and Exceptions
# Syntax errors are also called parsing errors
# Exceptions are errors detected during execution of a statement or expression (even if they are syntactically correct)
# There are different types of exceptions: Ex. ZeroDivisionError, NameError, TypeError...

# Try Statement:
# First, the "try" clause (the statement(s) between the try and exept keywords) is executed
# If no exception occurs, the except clause is skipped and execution of the try statement is finished
# If an exception occurs during exectution of the try clause, the rest of the clause is skipped
# Then if its type matches the exception named after the except keyword, the except clause is executed, 
# and then execution continues after the try statement

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        # The break statement, breaks out of the smalles enclosing "for" or "while" loop 
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
        
# The "try" statement has another optional clause which is intended to define clean-up actions that must be executed
# under all circumstances.  The "finally" clause is always executed before leaving the "try" statement, whether an exception
# has occurred or not.
#try:
    #raise KeyboardInterrupt
#finally:
    #print "Goodbye, world!"
        
        
# The "raise" statment allows the programmer to force a specified exception to occur.
#raise NameError('HiThere') # The sole argument to "raise" indicates the exeption to be raise.

# The "break" statement breaks out of the smallest enclosing "for" or "while" loop
# Loop statements may have an "else" clause; it is executed when the loop terminates through
# exhaustion of the list (with "for") or when the condition becomes False (with "while", but
# not when the loop is terminated by a break statement.  (It terminates the nearest enclosing loop,
# skipping the optional else clause if the loop has one.)
def search_for_prime(x, y):        
    for n in range(x, y):
        for a in range(2, n):
            if n % a == 0:
                print n, "equals", a, "*", n/a
                break
        else: 
            print n, "is a prime number"
            
search_for_prime(3, 9)


# The "continue" statement continues with the next iteration of the loop.
for num in range (2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        # if an even number has been found, skip "print "Found a number", num" 
        # and continue with the next iteration
        continue
    print "Found a number", num
    
    
# The "pass" statement does nothing. It can be use when a statement is required syntactically
# but the program requires no action.  Or it can be used as a place-holder for a function or conditional
# body when you are working on new code, allowing you to keep thinking at a more abstract level.
for i in range (3, 9):
    if i < 6:
        pass # if i < 6, do nothing
    else:
        print i
        
# The "lambda" keyword allows for small anonymous functions to be created.  Lambda forms ca
# be used whenerver function objects are required.  They are syntactically restricted to a single
# expression.   
def make_incrementor(n):
        return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)
        


# Assert statements are a convenient way ton insert debugging assertions into a program