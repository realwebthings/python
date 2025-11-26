# Type Casting Examples
x = 1      # int
y = 2.5    # float
z = "3"    # str

print("Before type casting:")
print("x:", x, "type:", type(x))  # Output: x: 1 type: <class 'int'>
print("y:", y, "type:", type(y))  # Output: y: 2.5 type: <class 'float'>
print("z:", z, "type:", type(z))  # Output: z: 3 type: <class 'str'>

print("\nAfter type casting:")
print("x to float:", float(x), "type:", type(float(x)))  # Output: x to float: 1.0 type: <class 'float'>
print("y to float:", float(y), "type:", type(float(y)))  # Output: y to float: 2.5 type: <class 'float'>
print("z to float:", float(z), "type:", type(float(z)))  # Output: z to float: 3.0 type: <class 'float'>

print("\nx to int:", int(x), "type:", type(int(x)))  # Output: x to int: 1 type: <class 'int'>
print("y to int:", int(y), "type:", type(int(y)))  # Output: y to int: 2 type: <class 'int'>
print("z to int:", int(z), "type:", type(int(z)))  # Output: z to int: 3 type: <class 'int'>

print("\nx to str:", str(x), "type:", type(str(x)))  # Output: x to str: 1 type: <class 'str'>
print("y to str:", str(y), "type:", type(str(y)))  # Output: y to str: 2.5 type: <class 'str'>
print("z to str:", str(z), "type:", type(str(z)))  # Output: z to str: 3 type: <class 'str'>

# Operations with different types
print("\nOperations:")
print(x + y)                    # Output: 3.5
print(x + float(z), x + int(z)) # Output: 4.0 4
print(str(x) + z)               # Output: 13
print(int(y) + int(z))          # Output: 5
