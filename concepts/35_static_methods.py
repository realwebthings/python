# Static methods : A method that belog to a class rather than any object from that class (instance)
#                   It doesn't have access to the class or instance of the class
#                   It is defined using the @staticmethod decorator
#                   It can be called using the class name or an instance of the class
#                   It is used to create utility functions that don't need access to instance-specific data
#
# Instance methods : Best for operations on instances of the class (Objects)
# Static methods   : Best for utility functions that do no need access to class data


class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
print(Math.add10(10))
Math.pr()