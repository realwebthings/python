class Car:
    # the are class variables
    make = None # not needed to declare
    model = None # not needed to declare
    year = None # not needed to declare
    color = None # not needed to declare
    
    def __init__(self, make, model, year, color):
        # these are instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color 

    def drive(self):
        print(f"{self.make} car is driving")

    def stop(self):
        print(f"{self.make} car is stopped")



if __name__ == "__main__":
    car_1 = Car("Chevy", "Corvette", 2021, "blue")
    car_2 = Car("Ford", "Mustang", 2022, "red")

    print(car_1.make)
    print(car_1.model)
    print(car_1.year)
    print(car_1.color)

    car_1.drive()
    car_1.stop()

    print(car_2.make)
    print(car_2.model)
    print(car_2.year)
    print(car_2.color)

    car_2.drive()
    car_2.stop()
