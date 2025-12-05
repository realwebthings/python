# NumPy Array Manipulation - Joining, splitting, and transforming arrays
import numpy as np

print("=" * 60)
print("NUMPY ARRAY MANIPULATION")
print("=" * 60)

# Sample arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_2d1 = np.array([[1, 2], [3, 4]])
arr_2d2 = np.array([[5, 6], [7, 8]])

print("Sample arrays:")
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"arr_2d1:\n{arr_2d1}")
print(f"arr_2d2:\n{arr_2d2}")

print("\n" + "=" * 50)
print("1. JOINING ARRAYS")
print("=" * 50)

# Concatenate
concat_1d = np.concatenate([arr1, arr2])
print(f"Concatenate 1D: {concat_1d}")

concat_2d_axis0 = np.concatenate([arr_2d1, arr_2d2], axis=0)
print(f"Concatenate 2D (axis=0):\n{concat_2d_axis0}")

concat_2d_axis1 = np.concatenate([arr_2d1, arr_2d2], axis=1)
print(f"Concatenate 2D (axis=1):\n{concat_2d_axis1}")

# Stack
vstack_result = np.vstack([arr1, arr2])
print(f"Vertical stack:\n{vstack_result}")

hstack_result = np.hstack([arr1, arr2])
print(f"Horizontal stack: {hstack_result}")

print("\n" + "=" * 50)
print("2. SPLITTING ARRAYS")
print("=" * 50)

# Split 1D array
large_array = np.array([1, 2, 3, 4, 5, 6])
split_result = np.split(large_array, 3)
print(f"Split into 3 parts: {split_result}")

# Split 2D array
large_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
vsplit_result = np.vsplit(large_2d, 3)
print(f"Vertical split: {[arr.tolist() for arr in vsplit_result]}")

hsplit_result = np.hsplit(large_2d, 2)
print(f"Horizontal split: {[arr.tolist() for arr in hsplit_result]}")

print("\n" + "=" * 50)
print("3. ARRAY TRANSFORMATIONS")
print("=" * 50)

# Transpose
original = np.array([[1, 2, 3], [4, 5, 6]])
transposed = original.T
print(f"Original:\n{original}")
print(f"Transposed:\n{transposed}")

# Flatten
flattened = original.flatten()
print(f"Flattened: {flattened}")

# Ravel (similar to flatten but returns view when possible)
raveled = original.ravel()
print(f"Raveled: {raveled}")

print("\n" + "=" * 50)
print("4. ARRAY COPYING")
print("=" * 50)

# View vs Copy
original_arr = np.array([1, 2, 3, 4, 5])
view_arr = original_arr.view()
copy_arr = original_arr.copy()

print(f"Original: {original_arr}")
print(f"View: {view_arr}")
print(f"Copy: {copy_arr}")

# Modify original
original_arr[0] = 999
print(f"\nAfter modifying original[0] = 999:")
print(f"Original: {original_arr}")
print(f"View: {view_arr}")  # Changes with original
print(f"Copy: {copy_arr}")  # Remains unchanged