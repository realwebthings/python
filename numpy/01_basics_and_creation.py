# NumPy Basics and Array Creation
import numpy as np

print("=" * 60)
print("NUMPY BASICS AND ARRAY CREATION")
print("=" * 60)

# Basic array creation
arr = np.array([1, 2, 3, 4, 5])
print(f"Basic array: {arr}")
print(f"Type: {type(arr)}")
print(f"Shape: {arr.shape}")
print(f"Size: {arr.size}")
print(f"Dimensions: {arr.ndim}")

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}")

# Array creation functions
zeros = np.zeros(5)
ones = np.ones((2, 3))
full = np.full(4, 7)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

print(f"\nZeros: {zeros}")
print(f"Ones:\n{ones}")
print(f"Full: {full}")
print(f"Arange: {arange}")
print(f"Linspace: {linspace}")

# Basic operations
arr = np.array([1, 2, 3, 4, 5])
print(f"\nOriginal: {arr}")
print(f"Add 1: {arr + 1}")
print(f"Multiply by 2: {arr * 2}")
print(f"Square: {arr ** 2}")