#well we have some number of cars here
cars = 100
#we are saying 4 ppl can fit in your toyota, Karen
space_in_a_car = 4
#really 1 driver is too many but yeah 
drivers = 30
#good luck
passengers = 90
#well if the cars off the drivers then no driven cars!
cars_not_driven = cars - drivers
#not really sure why we are just renaming that variable above here but sure
cars_driven = drivers
#mmm multiplication
carpool_capacity = cars_driven * space_in_a_car
#division time
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
