class Student:
    number_of_students = 0
    
    def __init__(self, name):
        self.name = name
        # Using self.__class__ (dynamic)
        self.__class__.number_of_students += 1

class HighSchoolStudent(Student):
    number_of_students = 0  # Separate counter for high school students

class CollegeStudent(Student):
    number_of_students = 0  # Separate counter for college students

# Test with inheritance
print("=== Using self.__class__ (Dynamic) ===")

# Create students
student1 = Student("John")
hs_student1 = HighSchoolStudent("Alice") 
hs_student2 = HighSchoolStudent("Bob")
college_student1 = CollegeStudent("Charlie")

print(f"Student count: {Student.number_of_students}")           # 1
print(f"HighSchool count: {HighSchoolStudent.number_of_students}") # 2  
print(f"College count: {CollegeStudent.number_of_students}")    # 1

print("\n" + "="*50)

# Now let's see what happens with Student.number_of_students
class StudentFixed:
    number_of_students = 0
    
    def __init__(self, name):
        self.name = name
        # Using class name directly (static)
        StudentFixed.number_of_students += 1

class HighSchoolStudentFixed(StudentFixed):
    number_of_students = 0

class CollegeStudentFixed(StudentFixed):
    number_of_students = 0

print("=== Using StudentFixed.number_of_students (Static) ===")

# Create students
student1 = StudentFixed("John")
hs_student1 = HighSchoolStudentFixed("Alice")
hs_student2 = HighSchoolStudentFixed("Bob") 
college_student1 = CollegeStudentFixed("Charlie")

print(f"StudentFixed count: {StudentFixed.number_of_students}")           # 4 (all students!)
print(f"HighSchoolFixed count: {HighSchoolStudentFixed.number_of_students}") # 0 (not updated)
print(f"CollegeFixed count: {CollegeStudentFixed.number_of_students}")    # 0 (not updated)