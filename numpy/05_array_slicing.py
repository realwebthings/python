# NumPy Array Slicing - Extracting parts of arrays
import numpy as np

# Create a 2D array (4 rows, 5 columns)
array = np.array([
    [1,  2,  3,  4,  5],   # Row 0
    [6,  7,  8,  9,  10],  # Row 1
    [11, 12, 13, 14, 15],  # Row 2
    [16, 17, 18, 19, 20]   # Row 3
])

print("Original Array:")
print(array)
print(f"Shape: {array.shape}")

print("\n" + "=" * 50)
print("1. ROW SLICING: array[start:end:step]")
print("=" * 50)

# Slice rows: start=0, end=4, step=2 (every 2nd row)
result1 = array[0:4:2]
print(f"array[0:4:2] - Every 2nd row from 0 to 4:")
print(result1)
print(f"Shape: {result1.shape}")
print("Explanation: Takes rows 0, 2 (skips row 1, 3)")

print("\n" + "=" * 50)
print("2. 2D SLICING: array[rows, columns]")
print("=" * 50)

# Slice both rows and columns
result2 = array[0:4:2, 0:4:2]
print(f"array[0:4:2, 0:4:2] - Every 2nd row AND every 2nd column:")
print(result2)
print(f"Shape: {result2.shape}")
print("Explanation: Takes rows 0,2 and columns 0,2 (creates 2x2 array)")
print("Selected elements: [1,3] from row 0, [11,13] from row 2")

print("\n" + "=" * 50)
print("3. REVERSE ALL ROWS: array[::-1]")
print("=" * 50)

# Reverse the order of rows
result3 = array[::-1]
print(f"array[::-1] - Reverse row order:")
print(result3)
print(f"Shape: {result3.shape}")
print("Explanation: Flips array upside down (row 3 becomes row 0)")

print("\n" + "=" * 50)
print("4. REVERSE EVERY 2ND ROW: array[::-2]")
print("=" * 50)

# Reverse and take every 2nd row
result4 = array[::-2]
print(f"array[::-2] - Reverse order, every 2nd row:")
print(result4)
print(f"Shape: {result4.shape}")
print("Explanation: Start from end, take every 2nd row (rows 3, 1)")

result5 = array[:, ::2]
print(f"array[:, ::2] - Every 2nd column:")
print(result5)
print(f"Shape: {result5.shape}")
print("Explanation: Takes every 2nd column (columns 0, 2, 4)")

print("\n" + "=" * 50)
print("SLICING SYNTAX SUMMARY")
print("=" * 50)
print("array[start:end:step]")
print("• start: Starting index (inclusive)")
print("• end: Ending index (exclusive)")
print("• step: Step size (1=every element, 2=every 2nd, -1=reverse)")
print("\nFor 2D arrays: array[row_slice, column_slice]")
print("• : means 'all elements'")
print("• ::-1 means 'all elements in reverse'")
print("• ::2 means 'every 2nd element'")

print("\n" + "=" * 50)
print("MORE EXAMPLES")
print("=" * 50)

# Additional examples
print(f"First row: array[0] = {array[0]}")
print(f"Last row: array[-1] = {array[-1]}")
print(f"First column: array[:, 0] = {array[:, 0]}")
print(f"Last column: array[:, -1] = {array[:, -1]}")
print(f"Center 2x2: array[1:3, 1:3] =\n{array[1:3, 1:3]}")