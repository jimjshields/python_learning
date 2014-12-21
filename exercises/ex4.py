# defining cars
cars = 100
# defining space in a car
space_in_a_car = 4.0
# defining drivers
drivers = 30
# defining passengers
passengers = 90
# defining cars not driven
cars_not_driven = cars - drivers
# defining cars driven
cars_driven = drivers
# defining carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# defining avg passengers per car
average_passengers_per_car = passengers / cars_driven

# printing how many cars
print "There are %s cars available." % cars
# printing how many drivers
print "There are only", drivers, "drivers available."
# printing how many empty cars
print "There will be", cars_not_driven, "empty cars today."
# printing how much capacity for carpool
print "We can transport", carpool_capacity, "people today."
# printing number of passengers
print "We have", passengers, "to carpool today."
# printing avg passengers per car
print "We need to put about", average_passengers_per_car, "in each car."