# inheritance : Means inheriting methods from parent class and use it .


class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")  
    
    def sleep(self):
        print("This animal is sleeping")



class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running")
    
    def eat(self):
        print("This rabbit is eating")

class Fish(Animal):
    
    
    def swim(self):
        print("This fish is swimming")

    def eat(self):
        print("This fish is eating")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")
    
    def eat(self):
        print("This hawk is eating")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)

rabbit.eat()
rabbit.run()

fish.swim()
fish.eat()

hawk.fly()
hawk.eat()
