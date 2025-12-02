class Student:
    school_name = "ABC School"  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
    
    def instance_method(self):
        # ✅ CAN access both instance and class data
        return f"{self.name} studies at {self.school_name}"
    
    @classmethod
    def class_method(cls):
        # ✅ CAN access class data, but NOT instance data
        return f"School: {cls.school_name}"
    
    @staticmethod
    def static_method():
        # ❌ CANNOT access class or instance data
        # return f"{self.name}"      # ERROR: no 'self'
        # return f"{cls.school_name}" # ERROR: no 'cls'
        return "This is just a utility function"

# Usage
student = Student("John")

print("Instance method:", student.instance_method())  # ✅ Works
print("Class method:", Student.class_method())        # ✅ Works  
print("Static method:", Student.static_method())      # ✅ Works but limited

# Static method is like a regular function inside a class
print("Static via instance:", student.static_method()) # Also works