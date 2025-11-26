# tuple. = collection of ordered, immutable objects (unchangeable)
# tuples are written with round brackets
# tuples can contain mixed data types

#different from lists bc tuples are immutable (cannot be changed after creation) 
# what it means is that you cannot add, remove, or modify elements in a tuple once it is created

my_tuple = ("apple", 42, 3.14, True)
print(my_tuple)  # Output: ('apple', 42, 3.14, True)
print(my_tuple[0])  # Output: apple
print(my_tuple[2:4])  # Output: (3.14, True)

for item in my_tuple:
    print(item)  # Print each item in the tuple

# unpacking tuples
fruit, number, pi, boolean = my_tuple
print(fruit)   # Output: apple
print(number)  # Output: 42
print(pi)      # Output: 3.14
print(boolean) # Output: True


if 42 in my_tuple:
    print("42 is in the tuple")  # Output: 42 is in the tuple
else:
    print("42 is not in the tuple")

# tuples are immutable, so the following operations will raise errors
# my_tuple[1] = 100  # This will raise a TypeError
# my_tuple.append("banana")  # This will raise an AttributeError
# my_tuple.remove("apple")  # This will raise an AttributeError

# however, you can concatenate tuples to create a new tuple
new_tuple = my_tuple + ("banana", "orange")
print(new_tuple)  # Output: ('apple', 42, 3.14, True, 'banana', 'orange')

# tuple methods
print(len(my_tuple))  # Output: 4 (number of items in the tuple)
print(my_tuple.count(42))  # Output: 1 (number of times 42 appears in the tuple)
print(my_tuple.index("apple"))  # Output: 0 (index
# of apple in the tuple)
# nested tuples
nested_tuple = (("a", "b"), (1, 2), (True, False))
print(nested_tuple[1][0])  # Output: 1 (first item in the second tuple)
for inner_tuple in nested_tuple:
    for item in inner_tuple:
        print(item)  # Print each item in the nested tuples 

# converting between tuples and lists
my_list = list(my_tuple)
print(my_list)  # Output: ['apple', 42, 3.14, True]
my_new_tuple = tuple(my_list)
print(my_new_tuple)  # Output: ('apple', 42, 3.14, True)

# single element tuple (note the comma)
single_element_tuple = ("only_one_element",)
print(single_element_tuple)  # Output: ('only_one_element',)
print(type(single_element_tuple))  # Output: <class 'tuple'>

not_a_tuple = ("not_a_tuple")
print(type(not_a_tuple))  # Output: <class 'str'>

