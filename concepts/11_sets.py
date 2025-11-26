# Set = collection of unique items
# Sets are unordered, meaning the items have no defined order
# Sets are mutable, meaning you can add or remove items after creation


utensils = {"fork", "knife", "spoon"}
dishes = {"bowl", "plate", "cup", "knife"}


for x in utensils:
    print(x)  # Print each item in the utensils set (order may vary)
utensils.add("napkin")  # Add napkin to the utensils set
print(utensils)  # Output: {'fork', 'knife', 'spoon', 'napkin'} (order may vary)
utensils.remove("fork")  # Remove fork from the utensils set
print(utensils)  # Output: {'knife', 'spoon', 'napkin'} (order may vary)

# Set operations
print(utensils.union(dishes))  # Combine utensils and dishes sets
print(utensils.intersection(dishes))  # Items common to both sets
print(utensils.difference(dishes))  # Items in utensils but not in dishes
print(utensils.symmetric_difference(dishes))  # Items in either set but not both
# Check membership
print("spoon" in utensils)  # Output: True
print("bowl" in utensils)   # Output: False


# Set methods
utensils.update(dishes)  # Add all items from dishes to utensils
print(utensils)  # Output: utensils set now includes items from dishes
dishes.clear()  # Remove all items from dishes
print(dishes)  # Output: set() (empty set)


# Frozenset = immutable set (cannot be changed after creation)
frozen_utensils = frozenset(["fork", "knife", "spoon"])
print(frozen_utensils)  # Output: frozenset({'fork', 'knife', 'spoon'})

# frozen_utensils.add("napkin")  # This will raise an AttributeError
# frozen_utensils.remove("fork")  # This will raise an AttributeError

    
print(len(utensils))  # Output: number of items in the utensils set
print(len(frozen_utensils))  # Output: 3 (number of items in the frozenset)

# Set comprehension
squared_numbers = {x**2 for x in range(10)}
print(squared_numbers)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

nested_set = {x: {y for y in range(x)} for x in range(5)}
print(nested_set)  # Output: {0: set(), 1: {0}, 2: {0, 1}, 3: {0, 1, 2}, 4: {0, 1, 2, 3}}       


# Converting between sets and lists
my_list = ["apple", "banana", "apple", "orange"]
my_set = set(my_list)  # Convert list to set (removes duplicates)
print(my_set)  # Output: {'apple', 'banana', 'orange'} (order may vary)
new_list = list(my_set)  # Convert set back to list
print(new_list)  # Output: ['apple', 'banana', 'orange'] (order may vary)


# Converting between sets and tuples
my_tuple = ("apple", "banana", "apple", "orange")
my_set_from_tuple = set(my_tuple)  # Convert tuple to set (removes duplicates)
print(my_set_from_tuple)  # Output: {'apple', 'banana', 'orange'} (order may vary)
new_tuple = tuple(my_set_from_tuple)  # Convert set back to tuple
print(new_tuple)  # Output: ('apple', 'banana', 'orange') (order may vary)


# Empty set
empty_set = set()
print(empty_set)  # Output: set()
print(type(empty_set))  # Output: <class 'set'>


# Empty frozenset
empty_frozenset = frozenset()
print(empty_frozenset)  # Output: frozenset()
print(type(empty_frozenset))  # Output: <class 'frozenset'> 

# Note: {} creates an empty dictionary, not an empty set
empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'>