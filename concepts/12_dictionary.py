# dict = dictionary = key-value pairs
# Keys must be unique and immutable (e.g., strings, numbers, tuples)
# Values can be of any data type and can be duplicated


my_dict = {}

my_dict["name"] = "Alice"
my_dict["age"] = 30
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30   

my_dict["age"] = 31  # Update age
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}


del my_dict["city"]  # Remove city
print(my_dict)  # Output: {'name': 'Alice', 'age': 31}


for key, value in my_dict.items():
    print(f"{key}: {value}")  # Print each key-value pair

print("name" in my_dict)  # Output: True
print("city" in my_dict)  # Output: False

print(len(my_dict))  # Output: 2 (number of key-value pairs)


# Dictionary methods
dict_keys = my_dict.keys()
print(dict_keys)  # Output: dict_keys(['name', 'age'])  


dict_values = my_dict.values()
print(dict_values)  # Output: dict_values(['Alice', 31])


dict_items = my_dict.items()
print(dict_items)  # Output: dict_items([('name', 'Alice'), ('age', 31)])


my_dict.clear()  # Remove all key-value pairs
print(my_dict)  # Output: {} (empty dictionary)


# Nested dictionaries
nested_dict = {
    "person1": {"name": "Bob", "age": 25},
    "person2": {"name": "Carol", "age": 28}
}

print(nested_dict["person1"]["name"])  # Output: Bob
print(nested_dict["person2"]["age"])   # Output: 28



for person, info in nested_dict.items():
    print(f"{person}:")
    for key, value in info.items():
        print(f"  {key}: {value}")  # Print each key-value pair in the nested dictionary

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Converting between dictionaries and lists of tuples
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
dict_from_tuples = dict(list_of_tuples)
print(dict_from_tuples)  # Output: {'a': 1, 'b': 2, 'c': 3}


list_of_tuples_from_dict = list(dict_from_tuples.items())
print(list_of_tuples_from_dict)  # Output: [('a', 1), ('b', 2), ('c', 3)]

# Converting between dictionaries and lists of lists
list_of_lists = [["x", 10], ["y", 20], ["z", 30]]
dict_from_lists = dict(list_of_lists)
print(dict_from_lists)  # Output: {'x': 10, 'y': 20, 'z': 30}

list_of_lists_from_dict = list(dict_from_lists.items())
print(list_of_lists_from_dict)  # Output: [('x', 10), ('y', 20), ('z', 30)]

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}  # dict2 values will overwrite dict1 values for duplicate keys
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using the update() method to merge dictionaries
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Creating a dictionary with default values using fromkeys()
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(default_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# Using setdefault() to get a value or set a default if the key doesn't exist
value = default_dict.setdefault("country", "USA")
print(value)  # Output: USA         
print(default_dict)  # Output: {'name': 'unknown', 'age': 'unknown , 'city': 'unknown', 'country': 'USA'}   

# Using pop() to remove a key and return its value
age = default_dict.pop("age", "not found")
print(age)  # Output: unknown
print(default_dict)  # Output: {'name': 'unknown', 'city': 'unknown', 'country': 'USA'}

age2 = default_dict.pop("age2", "not found")
print(age2)  # Output: not found
# Using popitem() to remove and return the last inserted key-value pair
last_item = default_dict.popitem()
print(last_item)  # Output: ('country', 'USA')
print(default_dict)  # Output: {'name': 'unknown', 'city': 'unknown'}


# Using the copy() method to create a shallow copy of the dictionary
copied_dict = default_dict.copy()
print(copied_dict)  # Output: {'name': 'unknown', 'city': 'unknown'}


# Using the dict() constructor to create a new dictionary
new_dict = dict(name="Dave", age=40, city="Chicago")
print(new_dict)  # Output: {'name': 'Dave', 'age': 40, 'city': 'Chicago'}


# Using the merge (|) operator to merge dictionaries (Python 3.9+)
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
merged_dict2 = dict_a | dict_b  # dict_b values will overwrite dict_a values
print(merged_dict2)  # Output: {'x': 1, 'y': 3, 'z': 4}









