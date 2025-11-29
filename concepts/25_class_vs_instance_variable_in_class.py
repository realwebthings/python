class Car:
    wheels = 4

    def __init__(self, make, model, year, color):
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

    car_1.wheels = 2
    print(car_1.wheels)
    print(car_2.wheels)

    car_1.drive()
    car_1.stop()
    
    
    car_2.drive()
    car_2.stop()

    print("============= after updating class variables ====")
    Car.wheels = 2
    
    print(car_1.wheels)
    print(car_2.wheels)


    car_1.drive()
    car_1.stop()
    
    
    car_2.drive()
    car_2.stop()
