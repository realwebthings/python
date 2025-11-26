#str.format() method examples
name = "Aman"
age = 25

print("My name is "+name+" and I am "+str(age)+" years old.")  # Output: My name is Aman and I am 25 years old. (Not recommended

# using str.format() method
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Aman and I am 25 years old.

# Using positional arguments
print("My name is {0} and I am {1} years old. {0} is learning Python.".format(name, age))  # Output: My name is Aman and I am 25 years old. Aman is learning Python.

# Using keyword arguments
print("My name is {name} and I am {age} years old.".format(name="Grace", age=30))  # Output: My name is Grace and I am 30 years old.

# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Aman and I am 25 years old.

# f-strings with expressions
print(f"In five years, I will be {age + 5} years old.")  # Output: In five years, I will be 30 years old.


print(f"Hello, My Name is {name:10}. My age is {age}")  # Output: Hello, My Name is Aman
print(f"Hello, My Name is {name:<10}. My age is {age}")  # Output: Hello, My Name is Aman default left align
print(f"Hello, My Name is {name:>10}. My age is {age}")  # Output: Hello, My Name is Aman (right align)
print(f"Hello, My Name is {name:^10}. My age is {age}")  # Output: Hello, My Name is Aman (center align)





