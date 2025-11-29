# Multi inheritance : when a class is derived from more than one base class it is called multi inheritance
class Father:
    def travel(self):
        print("Father is travelling")


class Mother:
    def reading(self):
        print("Mother is reading")


class Child(Father, Mother):
    def play(self):
        print("Child is playing")


c = Child()
c.travel()
c.reading()
c.play()



print("===============*******===============")

class Prey:
    def flee(self):
        print("This animal flees")

    
class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
