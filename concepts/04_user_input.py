# User Input and Type Conversion
try:
    name = input("Enter your name: ")  # User enters: Alice
    age = int(input("Enter your age: "))  # User enters: 20
    is_student_input = input("Are you a student? (yes/no): ")  # User enters: yes
except EOFError:
    # Default values for testing when no input available
    name = "John"
    age = 25
    is_student_input = "yes"
    print("Using default values for testing")  # Output: Using default values for testing

is_student = is_student_input.lower() in ['yes', 'y', 'true', '1']  # Converts to boolean

# Display results
print(f"\nHello {name}!")  # Output: Hello John! (or Hello Alice!)
print(f"You are {age} years old")  # Output: You are 25 years old (or You are 20 years old)
print(f"Student status: {is_student}")  # Output: Student status: True
print(f"Age type: {type(age)}")  # Output: Age type: <class 'int'>
print(f"Student type: {type(is_student)}")  # Output: Student type: <class 'bool'>

# Calculate birth year
birth_year = 2024 - age
print(f"You were born around {birth_year}")  # Output: You were born around 1999 (or 2004) 
