# NumPy Array Sorting
import numpy as np

print("=" * 60)
print("NUMPY ARRAY SORTING")
print("=" * 60)

# Sample data
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])

print(f"1D array: {arr}")
print(f"2D array:\n{arr_2d}")

print("\n" + "=" * 50)
print("1. BASIC SORTING")
print("=" * 50)

# Sort array (returns new sorted array)
sorted_arr = np.sort(arr)
print(f"Original: {arr}")
print(f"Sorted: {sorted_arr}")

# Sort in-place
arr_copy = arr.copy()
arr_copy.sort()
print(f"In-place sorted: {arr_copy}")

print("\n" + "=" * 50)
print("2. SORTING 2D ARRAYS")
print("=" * 50)

# Sort along different axes
sort_axis0 = np.sort(arr_2d, axis=0)  # Sort columns
sort_axis1 = np.sort(arr_2d, axis=1)  # Sort rows
sort_none = np.sort(arr_2d, axis=None)  # Flatten and sort

print(f"Sort along axis=0 (columns):\n{sort_axis0}")
print(f"Sort along axis=1 (rows):\n{sort_axis1}")
print(f"Sort flattened: {sort_none}")

print("\n" + "=" * 50)
print("3. ARGSORT - SORTING INDICES")
print("=" * 50)

# Get indices that would sort the array
indices = np.argsort(arr)
print(f"Array: {arr}")
print(f"Sort indices: {indices}")
print(f"Sorted using indices: {arr[indices]}")

# Reverse order (descending)
desc_indices = np.argsort(arr)[::-1]
print(f"Descending indices: {desc_indices}")
print(f"Descending sorted: {arr[desc_indices]}")

print("\n" + "=" * 50)
print("4. SEARCHING IN SORTED ARRAYS")
print("=" * 50)

sorted_arr = np.array([1, 2, 3, 5, 7, 8, 9])
print(f"Sorted array: {sorted_arr}")

# Binary search
search_val = 5
index = np.searchsorted(sorted_arr, search_val)
print(f"Insert position for {search_val}: {index}")

# Search multiple values
search_vals = [0, 4, 6, 10]
indices = np.searchsorted(sorted_arr, search_vals)
print(f"Insert positions for {search_vals}: {indices}")

print("\n" + "=" * 50)
print("5. PARTIAL SORTING")
print("=" * 50)

# Get k smallest elements
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
k = 3
k_smallest = np.partition(arr, k)
print(f"Array: {arr}")
print(f"Partitioned (k={k}): {k_smallest}")
print(f"First {k+1} elements are the {k+1} smallest")

# Get indices of k smallest
k_indices = np.argpartition(arr, k)
print(f"Partition indices: {k_indices}")

print("\n" + "=" * 50)
print("SORTING SUMMARY")
print("=" * 50)
print("BASIC SORTING:")
print("- np.sort(): Return sorted copy")
print("- array.sort(): Sort in-place")
print("\nSORT INDICES:")
print("- np.argsort(): Get sorting indices")
print("- Use [::-1] for descending order")
print("\nSEARCHING:")
print("- np.searchsorted(): Binary search in sorted array")
print("\nPARTIAL SORTING:")
print("- np.partition(): Partial sort (k smallest/largest)")
print("- np.argpartition(): Get partition indices")