# Class methods : Allow operations reated to the class itself
#                 It takes the class as the first argument instead of self

# Instance methods = Best for operations on instances of the class (objects)
# Static methods   = Best for utility functions that do no need access to class data
# Class methods = Best for class-level data or require access to the class itself.
# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by Python's built-in when certain operations
#                 are performed on instances of the class.
#                 They allow developers to define or customise the behavior of objects

class Student:
    number_of_students = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        # self.__class__.number_of_students += 1
        self.name = name
        self.age = gpa
        Student.number_of_students += 1
        Student.total_gpa += gpa

    @classmethod
    def get_avg_gpa(cls):
        if cls.total_gpa > 0:
            return cls.total_gpa / cls.number_of_students
    
    @classmethod
    def get_number_of_students(cls):
        return cls.number_of_students
    

student1 = Student("Ram", 7)
student2 = Student("Shyam", 8)
student3 = Student("Kumar", 9)

print(Student.get_number_of_students())
print(Student.get_avg_gpa())