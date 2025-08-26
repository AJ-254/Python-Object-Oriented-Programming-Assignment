# Assignment 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        return "The vehicle is moving..."

class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying "

class Boat(Vehicle):
    def move(self):
        return "Sailing "

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling "

# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())
