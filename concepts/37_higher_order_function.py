# Higher Order Function : A function that either accepts a function as an argument or returns a function
# map, filter, reduce, all of these are higher order functions

# def greet(func):
#     func()

# def greet2():
#     def func():
#         return 5
#     return func()


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)
    # return func("Hello")

hello(loud)
hello(quiet)


# returns a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10)) # 5.0