# scope = the region of code where a variable is accessible
# global scope = variables defined outside of functions, accessible anywhere in the file
# local scope = variables defined inside a function, accessible only within that function

# order of variable scope resolution: local -> enclosing -> global -> built-in
# global variable
x = 10 

# function to demonstrate local scope
def my_function():
    # local variable
    y = 5
    print("Inside function:")
    print("x (global):", x)  # accessible
    print("y (local):", y)   # accessible


#demonstrate global scope
my_function()
print("Outside function:")
print("x (global):", x)  # accessible
# print("y (local):", y)   # NameError: y is not defined


# nested function to demonstrate enclosing scope
def outer_function():
    outer_var = "I'm from the outer function"

    def inner_function():
        inner_var = "I'm from the inner function"
        print("Inside inner function:")
        print(outer_var)  # accessible (enclosing scope)
        print(inner_var)  # accessible (local scope)

    inner_function()
    # print(inner_var)  # NameError: inner_var is not defined

print("\nDemonstrating enclosing scope:")
outer_function()


# demonstrating global keyword
count = 0  # global variable

def increment():
    global count
    count += 2
    print("Inside function:", count)
increment()
print("Outside function:", count)


# demonstrating nonlocal keyword
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

print("\nDemonstrating nonlocal keyword:")
outer()


# demonstrating built-in scope
print("\nDemonstrating built-in scope:")
print(len("Hello, World!"))  # len() is a built-in function


