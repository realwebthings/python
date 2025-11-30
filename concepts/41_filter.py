# filter() : creates a collection of elements from iterable for which  a function returns true.

# filter(function, iterable)
# function: It is a function to which filter passes each element in the iterable.
# iterable: It is a iterable like sets, lists, tuples etc.

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)  # Output: 18 24 32


friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

print("drinking buddies:", drinking_buddies)
