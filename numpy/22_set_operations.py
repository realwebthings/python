# NumPy Set Operations
import numpy as np

print("=" * 60)
print("NUMPY SET OPERATIONS")
print("=" * 60)

# Sample arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
c = np.array([1, 1, 2, 2, 3, 3, 4])

print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"Array c (with duplicates): {c}")

print("\n" + "=" * 50)
print("1. UNIQUE VALUES")
print("=" * 50)

# Find unique values
unique_c = np.unique(c)
print(f"Unique values in c: {unique_c}")

# Unique with counts
unique_vals, counts = np.unique(c, return_counts=True)
print(f"Values: {unique_vals}")
print(f"Counts: {counts}")

# Unique with indices
unique_vals, indices = np.unique(c, return_index=True)
print(f"First occurrence indices: {indices}")

print("\n" + "=" * 50)
print("2. SET OPERATIONS")
print("=" * 50)

# Intersection (common elements)
intersection = np.intersect1d(a, b)
print(f"Intersection of a and b: {intersection}")

# Union (all unique elements)
union = np.union1d(a, b)
print(f"Union of a and b: {union}")

# Difference (elements in a but not in b)
difference = np.setdiff1d(a, b)
print(f"Difference (a - b): {difference}")

# Symmetric difference (elements in either a or b, but not both)
sym_diff = np.setxor1d(a, b)
print(f"Symmetric difference: {sym_diff}")

print("\n" + "=" * 50)
print("3. MEMBERSHIP TESTING")
print("=" * 50)

# Test if elements of one array are in another
test_values = np.array([2, 5, 9])
is_in_a = np.isin(test_values, a)
print(f"Test values: {test_values}")
print(f"In array a: {is_in_a}")

# Which elements are in a
in_a = test_values[is_in_a]
print(f"Elements that are in a: {in_a}")

print("\n" + "=" * 50)
print("4. PRACTICAL EXAMPLES")
print("=" * 50)

# Example: Finding common customers
customers_jan = np.array(['Alice', 'Bob', 'Charlie', 'David'])
customers_feb = np.array(['Bob', 'Charlie', 'Eve', 'Frank'])

common_customers = np.intersect1d(customers_jan, customers_feb)
new_customers = np.setdiff1d(customers_feb, customers_jan)
lost_customers = np.setdiff1d(customers_jan, customers_feb)

print(f"January customers: {customers_jan}")
print(f"February customers: {customers_feb}")
print(f"Common customers: {common_customers}")
print(f"New customers: {new_customers}")
print(f"Lost customers: {lost_customers}")

print("\n" + "=" * 50)
print("SET OPERATIONS SUMMARY")
print("=" * 50)
print("UNIQUE VALUES:")
print("- np.unique(): Find unique elements")
print("- return_counts=True: Get counts")
print("- return_index=True: Get first occurrence indices")
print("\nSET OPERATIONS:")
print("- np.intersect1d(): Common elements")
print("- np.union1d(): All unique elements")
print("- np.setdiff1d(): Elements in first but not second")
print("- np.setxor1d(): Elements in either but not both")
print("\nMEMBERSHIP:")
print("- np.isin(): Test membership")
print("- Returns boolean array")