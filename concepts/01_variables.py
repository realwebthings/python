# Variables in Python

# String variable
name = "Aman"
print("Hello, " + name + "!")

# Different data types
age = 25
height = 5.9
is_student = True

# Multiple ways to print
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")

# Variable reassignment
name = "John"
print(f"Updated name: {name}")

print(type(name))        # str
print(type(age))         # int
print(type(height))      # float
print(type(is_student))  # bool


# detail = name + " is " + age + " years old."

# print(detail)  # TypeError: can only concatenate str (not "int") to str

detail = name + " is " + str(age) + " years old."

print(detail)  # Corrected: Now works fine



# name = "Aman"
# age = 30
# is_student = False
# height_in_meters = 1.75
# favorite_colors = ["blue", "green", "red"]
# address = {
#     "street": "123 Main St",
#     "city": "Anytown",
#     "zip_code": "12345"
# }

# def greet():
#     return f"Hello, my name is {name}."

# # Test the function
# print(greet())
# print(f"Age: {age}")
# print(f"Student: {is_student}")
# print(f"Colors: {favorite_colors}")


name, age, is_student = "Aman", 30, False

print(name, age, is_student)


aman_age = suresh_age = neelam_age = 25

print(aman_age, suresh_age, neelam_age)

