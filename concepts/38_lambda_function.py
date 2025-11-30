# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

double = lambda x: x * 2
print(double(5))
multiply = lambda x, y: x * y
print(multiply(5, 6))
add = lambda x, y, z: x + y + z
print(add(5, 6, 7))
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Bro", "Code"))
age_check = lambda age: True if age >= 18 else False
print(age_check(18))

# Lambda with keyword arguments
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))  # Uses default greeting
print(greet("Bob", greeting="Hi"))  # Uses custom greeting

# Lambda with *args and **kwargs
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))

format_info = lambda **kwargs: ", ".join([f"{k}: {v}" for k, v in kwargs.items()])
print(format_info(name="John", age=25, city="NYC"))

# Breaking down the format_info lambda:
# format_info = lambda **kwargs: ", ".join([f"{k}: {v}" for k, v in kwargs.items()])

# Step by step explanation:
# 1. **kwargs - collects all keyword arguments into a dictionary
# 2. kwargs.items() - returns key-value pairs from the dictionary
# 3. [f"{k}: {v}" for k, v in kwargs.items()] - list comprehension that creates strings like "key: value"
# 4. ", ".join(...) - joins all strings with ", " separator

# Example breakdown:
def explain_format_info(**kwargs):
    print(f"kwargs received: {kwargs}")
    print(f"kwargs.items(): {list(kwargs.items())}")
    
    # List comprehension step
    formatted_list = [f"{k}: {v}" for k, v in kwargs.items()]
    print(f"After list comprehension: {formatted_list}")
    
    # Join step
    result = ", ".join(formatted_list)
    print(f"After join: {result}")
    return result

print("\nStep-by-step breakdown:")
explain_format_info(name="John", age=25, city="NYC")