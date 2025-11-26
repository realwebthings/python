# two types of function arguments: positional and keyword arguments
# positional arguments are passed in the order they are defined
# keyword arguments are passed with the name of the parameter
# functions can have default parameter values
# functions can have variable-length arguments using *args and **kwargs
# functions can return multiple values as tuples
# functions can have keyword-only arguments
# functions can have positional-only arguments (Python 3.8+)
# functions can have type hints for parameters and return values
# functions can have variable-length keyword arguments using **kwargs



def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Grace"))  # Output: Hello, Grace!
print(greet("Grace", "Hi"))  # Output: Hi, Grace!

# functions can have default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))  # Output: 9
print(power(2, 3))  # Output: 8


#functions can have multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([3, 1, 4, 1, 5, 9]))  # Output: (1, 9)

#functions can have keyword-only arguments
def introduce(name, *, age): # name is positional, age is keyword-only and keyword argument order does not matter
    return f"My name is {name} and I am {age} years old."

print(introduce("Grace", age=30))  # Output: My name is Grace and I am 30 years old.

#functions can have variable-length arguments
def sum_all(*args): # positional arguments collected into a tuple, so cannot be altered inside function
    return sum(args)
    # another way to write it:
    # total = 0
    # for num in args:
    #     total += num
    # return total


print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5, 10, 15))  # Output: 30

#functions can have variable-length keyword arguments
def print_info(**kwargs): # keyword arguments collected into a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Grace", age=30, city="New York")