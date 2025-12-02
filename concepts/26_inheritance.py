#Polymorphism = Greak work that means to "have many forms or faces"
#               Poly = Many
#               Morphe = Form
#               
#               Two ways to achieve polymorphism
#               1. inheritance : Means inheriting methods from parent class and use it .
#               2. Duck typing : concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "if it walks like a duck, and it quacks like a duck, then it must be a a duck."
   

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

