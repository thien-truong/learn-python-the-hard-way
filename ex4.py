cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# each person is allowed 1 portion
oranges = 200
servings_per_orange = 4.0
eaters = 34
orange_eaten = eaters / servings_per_orange
orange_not_eaten = oranges - orange_eaten

print "There are", oranges, "oranges."
print "There are {} oranges.".format(oranges)
print "Each orange allows %d servings." % servings_per_orange
print "Each orange allows {} servings.".format(servings_per_orange)
print "Each orange allows", servings_per_orange, "servings."
print "%d will eat %d oranges." %(eaters, orange_eaten)
print "{} will eat {} oranges.".format(eaters, orange_eaten)
print eaters, "will eat", orange_eaten, "oranges."
print "Therefore the amount of orange left is {}.".format(orange_not_eaten)

