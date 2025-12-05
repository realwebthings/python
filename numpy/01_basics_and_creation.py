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

print(f"\nZeros: {zeros}")
print(f"Ones:\n{ones}")
print(f"Full: {full}")

print("\n" + "=" * 50)
print("RANGE ARRAYS")
print("=" * 50)

# arange - like Python range
arange_basic = np.arange(10)
arange_range = np.arange(2, 8)
arange_step = np.arange(0, 10, 2)
print(f"arange(10): {arange_basic}")
print(f"arange(2, 8): {arange_range}")
print(f"arange(0, 10, 2): {arange_step}")

# linspace - evenly spaced numbers
linspace_basic = np.linspace(0, 1, 5)
linspace_more = np.linspace(0, 10, 6)
print(f"linspace(0, 1, 5): {linspace_basic}")
print(f"linspace(0, 10, 6): {linspace_more}")

print("\n" + "=" * 50)
print("BASIC OPERATIONS")
print("=" * 50)

# Basic operations
arr = np.array([1, 2, 3, 4, 5])
print(f"Original: {arr}")
print(f"Add 1: {arr + 1}")
print(f"Multiply by 2: {arr * 2}")
print(f"Square: {arr ** 2}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("• np.arange(start, stop, step) - Like Python range")
print("• np.linspace(start, stop, num) - Evenly spaced numbers")
print("• np.zeros(), np.ones(), np.full() - Filled arrays")
print("• Basic arithmetic: +, -, *, /, **")