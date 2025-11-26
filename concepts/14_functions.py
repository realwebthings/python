# function = "first-class citizen"
# functions can be assigned to variables, passed as arguments to other functions, and returned from other functions
# functions are defined using the "def" keyword
# functions can have parameters and return values
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


# functions can be assigned to variables
say_hello = greet
print(say_hello("Bob"))  # Output: Hello, Bob!


# functions can be passed as arguments to other functions
def call_function(func, name):
    return func(name)

print(call_function(greet, "Charlie"))  # Output: Hello, Charlie!


print(call_function(say_hello, "David"))  # Output: Hello, David!



# functions can return other functions
def make_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

morning_greet = make_greeting("Good morning")
print(morning_greet("Eve"))  # Output: Good morning, Eve!


evening_greet = make_greeting("Good evening")
print(evening_greet("Frank"))  # Output: Good evening, Frank!

#nested functions = functions defined inside other functions

#nested functions can access variables from the enclosing scope
def outer_function(msg):
    def inner_function():
        return f"Message: {msg}"
    return inner_function()


print(outer_function("Hello from the outer function!"))  # Output: Message: Hello from the outer function!

#nest functions can be used to create closures
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment



counter_instance = counter()
print(counter_instance())  # Output: 1
print(counter_instance())  # Output: 2
print(counter_instance())  # Output: 3

another_counter = counter()
print(another_counter())  # Output: 1
print(another_counter())  # Output: 2 