# sort() method : used with lists
# sort() function : used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
students.sort()
# students.sort(reverse=True)
# students.sort(key=lambda name: name.split(" ")[-1].lower())


# # Breaking down: students.sort(key=lambda name: name.split(" ")[-1].lower())

# print("Step-by-step breakdown:")
# print("Original list:", students)

# # Let's see what the lambda function does for each name:
# for name in students:
#     split_name = name.split(" ")
#     print(f"'{name}' -> split: {split_name}")
    
#     last_part = split_name[-1]
#     print(f"  -> last part: '{last_part}'")
    
#     lowercase = last_part.lower()
#     print(f"  -> lowercase: '{lowercase}'")
#     print()

# print("Explanation:")
# print("1. name.split(' ') - splits the name by spaces into a list")
# print("2. [-1] - gets the last element (last name)")
# print("3. .lower() - converts to lowercase for case-insensitive sorting")
# print("4. The sort uses this last name (lowercase) as the sorting key")

# # Note: In this example, all names are single words, so split(" ") just returns [name]
# # and [-1] gets that same name. This would be more useful with full names like:
# full_names = ["John Smith", "Alice Brown", "Bob Anderson", "Carol Davis"]
# print(f"\nWith full names: {full_names}")
# full_names.sort(key=lambda name: name.split(" ")[-1].lower())
# print(f"Sorted by last name: {full_names}")

for i in students:
    print(i)

students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
sorted_students = sorted(students)

for i in sorted_students:
    print(i)

students = [
    {"name": "Squidward", "age": 18},
    {"name": "Sandy", "age": 25},
    {"name": "Patrick", "age": 30},
    {"name": "Spongebob", "age": 15},
    {"name": "Mr. Krabs", "age": 50}
]

age = lambda student: student["age"]
print("grade")
students.sort(key=age)
# students.sort(key=lambda student: student["age"])
sorted_students = sorted(students, key=age)

for i in students:
    print(i)
# DIFFERENCE BETWEEN sort() vs sorted()

print("=== DIFFERENCE BETWEEN sort() vs sorted() ===\n")

# Original lists for comparison
list1 = [3, 1, 4, 1, 5]
list2 = [3, 1, 4, 1, 5]

print(f"Original list1: {list1}")
print(f"Original list2: {list2}")

# Using sort() method
print("\n--- Using sort() method ---")
list1.sort()  # Modifies the original list
print(f"After list1.sort(): {list1}")
print("Returns: None")

# Using sorted() function  
print("\n--- Using sorted() function ---")
result = sorted(list2)  # Creates a new list
print(f"After sorted(list2): result = {result}")
print(f"Original list2 unchanged: {list2}")

print("\n=== KEY DIFFERENCES ===")
print("sort():")
print("- Method (only works on lists)")
print("- Modifies original list in-place")
print("- Returns None")
print("- More memory efficient")

print("\nsorted():")
print("- Function (works on any iterable)")
print("- Creates new sorted list")
print("- Returns the new sorted list")
print("- Original remains unchanged")

# Example with tuple (sort() won't work, but sorted() will)
print("\n=== Example with tuple ===")
tuple_data = (3, 1, 4, 1, 5)
print(f"Original tuple: {tuple_data}")
# tuple_data.sort()  # This would cause an error!
sorted_tuple = sorted(tuple_data)
print(f"sorted(tuple): {sorted_tuple}")