# Modules, Classes, And Objects

# Python is something called an "Object Oriented Programming Language".  
# What this means is there's a construct in Python called a class that lets you structure
# your software in a particualar way.  Using classes you can add consistency to your 
# programs so that they can e used in a cleaner way.

# Module:
# A Python file with some functions or variales in it.
# You then import that file.
# And then you can access the functions or variables in that module with the '.' (dot) operator.

# A "class" is a way to take a grouping of functions and data and place them 
# inside a container so you can acccess them with the '.'(dot) operator.
# Classes are like blueprints or definitions for creating new mini-modules

# You can take class, and use it to craft many of them, millions at a time if you want,
# and they won't interfere with each other.
# With modules, when you import, there is only one for the entire program

# When you "instantiate" a class, what you get is called an "object"

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            
# creating an object that's called "happy_bday"        
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
lyrics = ["I am a fish", "Quack quack quack", "I like to eat"]
fish_song = Song(lyrics)

fish_song.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()   

class Employee(object):
    """Common base class for all employees"""
    # empCount is a class variable whose value would be shared among all instances of this class.
    # This can be accessed as Employee.empCount from inside the class or outside the class.
    empCount = 0
    
    # the first method __init__() is a special method which is called class constructor or 
    # intitialization method that Python calls when you create a new instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print "Total Employee {:d}".format(Employee.empCount)
        
    def displayEmployee(self):
        print "Name: {}, Salary: {}".format(self.name, self.salary)
        
# To create instances of a class, you call the class using class name and 
# pass in whatever arguments its __init__ method accepts.

# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
emp3 = Employee("Fish", 3283)

# ACCESSING ATTRIBUTES:  You access the objects' attribues using the dot operator with object.
# Class variable would be accessed using class name as follows:

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp1.displayCount()
print "Total Employee {:d}".format(Employee.empCount)
                  
# You can add, remove, or modify attributes of classes and objects at any time:
emp1.age = 7 # add an age attribute
print emp1.age
emp1.age = 9 # modify "age" attribute
print emp1.age
del emp1.age # delete "atribute"
# print emp1.age would raise an AttributeError: 'Employee' object has no attribute 'age'

# Instead of using the normal statements to access attributes, you can use the following functions:

# setattr(object, name, value) set an atribute.  If attribute does not exist then it would be created.
setattr(emp1, 'age', 8)
print emp1.age

# hasattr(obj, name) returns true if an attribute exists or not
print hasattr(emp1, 'age')

# getattr(obj, name[, default]) returns value of the mentioned attribute
print getattr(emp1, 'age')

# delattr(obj, name) delete an attribute
delattr(emp1, 'age')

print Employee.__doc__ # print the document string statement for class "Employee"

# CLASS INHERITANCE: Intead of starting from scratch, you can create a class by deriving 
# it from a preexisitng class by listing the parent class in parentheses after the new class name.
# The child class inherits the attributes of its parent class, and you can use those
# attributes as if they were defined in a child class.  A child class can also overide data
# members and methods from the parent.

class Parent(object):
    parentAttr = 100
    def __init__(self):
        print "Calling parent constructor"
        
    def parentMethod(self):
        print 'Calling parent method'
        
    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print "Parent attribute: ", Parent.parentAttr
        
class Child(Parent):
    def __init__(self):
        print "Calling child constructor"
        
    def childMethod(self):
        print "Calling child method"
        
c = Child() # instance of a child
c.childMethod() # child calls its method
c.parentMethod() # child calls parent's method
c.setAttr(200) # child calls parent's method
c.getAttr() # child calls parent's method

class TheThing(object):
    
    def __init__(self):
        self.number = 0
        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        self.number += more
        return self.number
        
a = TheThing() # making instance a of class TheThing
b = TheThing() # making instance b of class TheThing

a.some_function()
b.some_function()

a.add_me_up(20)
a.add_me_up(20)
b.add_me_up(30)
b.add_me_up(30)

print a.number
print b.number

