# NumPy Array Indexing - Advanced indexing techniques
import numpy as np

print("=" * 60)
print("NUMPY ARRAY INDEXING")
print("=" * 60)

# Create sample arrays
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])

print("Sample arrays:")
print(f"1D array: {arr_1d}")
print(f"2D array:\n{arr_2d}")

print("\n" + "=" * 50)
print("1. BASIC INDEXING")
print("=" * 50)

# Single element access
print(f"arr_1d[0]: {arr_1d[0]}")  # First element
print(f"arr_1d[-1]: {arr_1d[-1]}")  # Last element
print(f"arr_2d[1, 2]: {arr_2d[1, 2]}")  # Row 1, Column 2
print(f"arr_2d[0][3]: {arr_2d[0][3]}")  # Alternative syntax

print("\n" + "=" * 50)
print("2. FANCY INDEXING")
print("=" * 50)

# Index with arrays
indices = np.array([0, 2, 4])
print(f"arr_1d[{indices}]: {arr_1d[indices]}")

# 2D fancy indexing
rows = np.array([0, 2])
cols = np.array([1, 3])
print(f"arr_2d[{rows}, {cols}]: {arr_2d[rows, cols]}")

print("\n" + "=" * 50)
print("3. BOOLEAN INDEXING")
print("=" * 50)

# Boolean mask
mask = arr_1d > 25
print(f"Mask (arr_1d > 25): {mask}")
print(f"Filtered values: {arr_1d[mask]}")

# 2D boolean indexing
mask_2d = arr_2d > 6
print(f"2D mask (> 6):\n{mask_2d}")
print(f"Values > 6: {arr_2d[mask_2d]}")

print("\n" + "=" * 50)
print("4. ADVANCED INDEXING COMBINATIONS")
print("=" * 50)

# Combine different indexing methods
print(f"First and last rows: \n{arr_2d[[0, -1]]}")
print(f"Specific elements: {arr_2d[[0, 1, 2], [0, 1, 2]]}")  # Diagonal

# Using conditions
even_positions = arr_1d[arr_1d % 20 == 0]
print(f"Values divisible by 20: {even_positions}")