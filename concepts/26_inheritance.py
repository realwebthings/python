# inheritance : Means inheriting methods from parent class and use it .


class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")  
    
    def sleep(self):
        print("This animal is sleeping")



class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.eat()
rabbit.sleep()

fish.eat()

hawk.sleep()

