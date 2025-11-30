# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function, iterable)

# function: It is a function to which map passes each element of given iterable.
# iterable: It is a iterable like sets, lists, tuples etc.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))  # Output: [2, 4, 6, 8]


store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)