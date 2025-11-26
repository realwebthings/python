# modules in Python are files containing Python code that can define functions, classes, and variables.
# They allow for code organization and reuse across different programs.

import message as msg
# from message import greet, add, multiply
# from message import * (not recommended due to potential namespace conflicts)

message1 = msg.greet("Alice")
sum_result = msg.add(5, 7)
product_result = msg.multiply(4, 6)

print(message1)            # Output: Hello, Alice!
print(sum_result)         # Output: 12
print(product_result)     # Output: 24

help(msg)  # Displays documentation about the 'message' module

help(msg.greet)  # Displays documentation about the 'greet' function

help('modules')  # Displays a list of all available modules