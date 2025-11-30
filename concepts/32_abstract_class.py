# Abstract class : Prevents user from creating an object of that class
# + compels a user to override abstract methods in a child class

# Abstract class = a class which contains one or more abstract methods.
# Abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC): # inheriting ABC class doesn't matter with abstract method
    @abstractmethod #due to this decorator Vehicle class can't instantiate  as abstract class Vehicle without an implementation for abstract method 'go'
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

vehicle = Vehicle()
car = Car() # if we don't override abstract methods then error would be : Cannot instantiate abstract class "Car" as "Vehicle.stop" is not implemented
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()