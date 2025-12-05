# NumPy Array Copying - Views vs Copies
import numpy as np

print("=" * 60)
print("NUMPY ARRAY COPYING - VIEWS VS COPIES")
print("=" * 60)

# Original array
original = np.array([1, 2, 3, 4, 5])
print(f"Original array: {original}")

print("\n" + "=" * 50)
print("1. VIEW (SHALLOW COPY)")
print("=" * 50)

# Create a view
view = original.view()
print(f"View: {view}")
print(f"Same data? {view.base is original}")

# Modify view
view[0] = 999
print(f"After modifying view[0] = 999:")
print(f"Original: {original}")
print(f"View: {view}")

print("\n" + "=" * 50)
print("2. COPY (DEEP COPY)")
print("=" * 50)

# Reset original
original = np.array([1, 2, 3, 4, 5])
copy = original.copy()
print(f"Copy: {copy}")
print(f"Same data? {copy.base is original}")

# Modify copy
copy[0] = 999
print(f"After modifying copy[0] = 999:")
print(f"Original: {original}")
print(f"Copy: {copy}")

print("\n" + "=" * 50)
print("3. SLICING CREATES VIEWS")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5])
slice_view = arr[1:4]
print(f"Original: {arr}")
print(f"Slice: {slice_view}")

slice_view[0] = 888
print(f"After modifying slice:")
print(f"Original: {arr}")
print(f"Slice: {slice_view}")

print("\n" + "=" * 50)
print("4. WHEN TO USE VIEW VS COPY")
print("=" * 50)
print("Use VIEW when:")
print("- You want to save memory")
print("- Changes should affect original")
print("- Working with large arrays")
print("\nUse COPY when:")
print("- You want independent arrays")
print("- Original should remain unchanged")
print("- Passing to functions that modify data")