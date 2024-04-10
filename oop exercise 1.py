# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


vehile = Vehicle(80, 20)
print(vehile.max_speed, vehile.mileage)
print("-------------------------------------------------")


# Create a Vehicle class without any variables and methods

class Vehicle:
    pass


# Create a Bus object that will inherit all the variables and methods of the parent Vehicle class and display it.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


bus = Bus("RatnamTravels", 100, 25)

print("name:", bus.name, "speed: ", bus.max_speed, "mileage: ", bus.mileage)

print("-------------------------------------------------")


# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=55):
        return super().seating_capacity(capacity=55)


bus = Bus("SCTB", 100, 25)

print("name:", bus.name, "speed: ", bus.max_speed, "mileage: ", bus.mileage)
print(bus.seating_capacity())
print("-------------------------------------------------")

#  Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    color = "White"

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=55):
        return super().seating_capacity(capacity=55)

class Van(Vehicle):
    pass


bus = Bus("SCTB", 100, 25)
van = Van("TATA", 70, 40)
print("color :",van.color, "name :", van.name, "speed :", van.max_speed, "mileage :", van.mileage )
print("color :", bus.color, "name :", bus.name, "speed :", bus.max_speed, "mileage :", bus.mileage)
print(bus.seating_capacity())
print("-------------------------------------------------")

#