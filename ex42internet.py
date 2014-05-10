# Is-a, Has-a, Object and Classes

# Animal is-a object
class Animal(object):
    pass
    
# Dog is-a Animal
class Dog (Animal):

    def __init__(self, name):
        # class Dog has-a self.name attribute (Dog has a name of some kind)
        self.name = name
        
# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # class Cat has a self.name attribute (Cat has a name of some kind)
        self.name = name
        
# Person is-a object      
class Person(object):

    def __init__(self, name):
        # class Person has a self.name attribute (Person has a name of some kind)
        self.name = name
        
        # Person has a self.pet attribute (person has a pet of some kind)
        self.pet = None
        
# Employee is-a person
class Employee(Person):
    
    def __init__(self, name, salary):
        #
        super(Employee, self).__init__(name)
        #
        self.salary = salary 

# class Fish is-a objcet    
class Fish(object):
    pass

# class Salmon is-a Fish    
class Salmon(Fish):
    pass
    
# class Halibut is-a Fish
class Halibut(Fish):
    pass
    
    
# rover is a Dog
rover = Dog("Rover")

# satan is a Cat
satan = Cat("Satan")

# mary is a Person
mary = Person("Mary")

# mary has a pet
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-apet 
frank.pet = rover

# flipper is a Fish
flipper = Fish()

# couse is-a Salmon
crouse = Salmon()

# harry is-a Hilibut
harry = Halibut()







        
        

