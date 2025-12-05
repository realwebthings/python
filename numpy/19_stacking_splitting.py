# NumPy Array Stacking and Splitting
import numpy as np

print("=" * 60)
print("NUMPY ARRAY STACKING AND SPLITTING")
print("=" * 60)

# Sample arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])

print("Sample arrays:")
print(f"a: {a}")
print(f"b: {b}")
print(f"c:\n{c}")
print(f"d:\n{d}")

print("\n" + "=" * 50)
print("1. STACKING ARRAYS")
print("=" * 50)

# Vertical stack (vstack)
v_stack = np.vstack((a, b))
print(f"Vertical stack:\n{v_stack}")

# Horizontal stack (hstack)
h_stack = np.hstack((a, b))
print(f"Horizontal stack: {h_stack}")

# Stack along axis
stack_axis0 = np.stack((a, b), axis=0)
stack_axis1 = np.stack((a, b), axis=1)
print(f"Stack axis=0:\n{stack_axis0}")
print(f"Stack axis=1:\n{stack_axis1}")

# 2D array stacking
v_stack_2d = np.vstack((c, d))
h_stack_2d = np.hstack((c, d))
print(f"2D vertical stack:\n{v_stack_2d}")
print(f"2D horizontal stack:\n{h_stack_2d}")

print("\n" + "=" * 50)
print("2. SPLITTING ARRAYS")
print("=" * 50)

# Array to split
arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Array to split: {arr}")

# Split into equal parts
split_equal = np.split(arr, 3)
print(f"Split into 3 parts: {split_equal}")

# Split at specific indices
split_indices = np.split(arr, [2, 4])
print(f"Split at indices [2, 4]: {split_indices}")

# 2D array splitting
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"\n2D array:\n{arr_2d}")

# Horizontal split
h_split = np.hsplit(arr_2d, 2)
print(f"Horizontal split:")
for i, part in enumerate(h_split):
    print(f"Part {i}:\n{part}")

# Vertical split
v_split = np.vsplit(arr_2d, 3)
print(f"Vertical split:")
for i, part in enumerate(v_split):
    print(f"Part {i}: {part}")

print("\n" + "=" * 50)
print("STACKING/SPLITTING SUMMARY")
print("=" * 50)
print("STACKING:")
print("- np.vstack(): Stack vertically (rows)")
print("- np.hstack(): Stack horizontally (columns)")
print("- np.stack(): Stack along new axis")
print("\nSPLITTING:")
print("- np.split(): Split into equal parts")
print("- np.hsplit(): Split horizontally")
print("- np.vsplit(): Split vertically")