# NumPy Broadcasting - Working with arrays of different shapes
import numpy as np

print("=" * 60)
print("NUMPY BROADCASTING EXPLAINED")
print("=" * 60)
print("Broadcasting allows NumPy to perform operations on arrays with different shapes")
print("by virtually expanding the smaller array to match the larger one's shape.")
print("\nBroadcasting Rules:")
print("1. Arrays are aligned from the rightmost dimension")
print("2. Dimensions are compatible if they are equal OR one of them is 1")
print("3. Missing dimensions are assumed to be 1")

print("\n" + "=" * 60)
print("EXAMPLE 1: SUCCESSFUL BROADCASTING")
print("=" * 60)

# Create a 2D array (2 rows, 3 columns)
a = np.array([[1, 2, 3], 
              [4, 5, 6]])
print(f"Array 'a' shape: {a.shape} (2x3)")
print(f"Array 'a':\n{a}")

# Create a 1D array (3 elements)
b = np.array([10, 20, 30])
print(f"\nArray 'b' shape: {b.shape} (3x1)")
print(f"Array 'b': {b}")

print("\nBroadcasting Analysis:")
print("a.shape: (2, 3)")
print("b.shape:    (3,)  <- NumPy treats this as (1, 3)")
print("Result:  (2, 3)  <- Compatible! b is broadcast to each row of a")

result1 = a + b
print(f"\na + b = \n{result1}")
print("Explanation: b [10, 20, 30] is added to each row of a")

print("\n" + "=" * 60)
print("EXAMPLE 2: BROADCASTING WITH COLUMN VECTOR")
print("=" * 60)

# Same 2D array
print(f"Array 'a' shape: {a.shape} (2x3)")
print(f"Array 'a':\n{a}")

# Create a column vector (2 rows, 1 column)
d = np.array([[100], 
              [200]])
print(f"\nArray 'd' shape: {d.shape} (2x1)")
print(f"Array 'd':\n{d}")

print("\nBroadcasting Analysis:")
print("a.shape: (2, 3)")
print("d.shape: (2, 1)")
print("Result:  (2, 3)  <- Compatible! d is broadcast to each column")

result2 = a + d
print(f"\na + d = \n{result2}")
print("Explanation: d [100, 200] is added to each column of a")

print("\n" + "=" * 60)
print("EXAMPLE 3: FAILED BROADCASTING (THE ERROR YOU SAW)")
print("=" * 60)

# Same 2D array
b_matrix = np.array([[1, 2, 3], 
                     [4, 5, 6]])
print(f"Array 'b_matrix' shape: {b_matrix.shape} (2x3)")
print(f"Array 'b_matrix':\n{b_matrix}")

# Create an incompatible array
c = np.array([1, 2])  # Only 2 elements
print(f"\nArray 'c' shape: {c.shape} (1x2)")
print(f"Array 'c': {c}")

print("\nBroadcasting Analysis:")
print("b_matrix.shape: (2, 3)")
print("c.shape:           (2,)  <- NumPy treats this as (1, 2)")
print("Result: INCOMPATIBLE! 3 ≠ 2")
print("\n❌ This causes the error: 'operands could not be broadcast together'")

try:
    result3 = b_matrix + c
except ValueError as e:
    print(f"\nError: {e}")
    print("\nWhy it fails:")
    print("- b_matrix needs 3 elements per row")
    print("- c only has 2 elements")
    print("- NumPy can't stretch 2 elements to fit 3 positions")

print("\n" + "=" * 60)
print("HOW TO FIX THE ERROR")
print("=" * 60)

print("Option 1: Make c have 3 elements")
c_fixed1 = np.array([1, 2, 3])
result3a = b_matrix + c_fixed1
print(f"c_fixed1 = {c_fixed1} (shape: {c_fixed1.shape})")
print(f"b_matrix + c_fixed1 =\n{result3a}")

print("\nOption 2: Reshape c to be a column vector")
c_fixed2 = c.reshape(2, 1)  # Make it (2, 1)
result3b = b_matrix + c_fixed2
print(f"c_fixed2 = \n{c_fixed2} (shape: {c_fixed2.shape})")
print(f"b_matrix + c_fixed2 =\n{result3b}")

print("\n" + "=" * 60)
print("BROADCASTING RULES SUMMARY")
print("=" * 60)
print("✅ COMPATIBLE shapes:")
print("   (3, 4) + (4,)     → (3, 4)")
print("   (3, 4) + (3, 1)   → (3, 4)")
print("   (3, 4) + (1, 4)   → (3, 4)")
print("   (3, 1) + (1, 4)   → (3, 4)")
print("\n❌ INCOMPATIBLE shapes:")
print("   (3, 4) + (3,)     → Error! (3 ≠ 4)")
print("   (3, 4) + (2, 4)   → Error! (3 ≠ 2)")
print("   (3, 4) + (3, 2)   → Error! (4 ≠ 2)")

print("\n💡 Remember: Broadcasting aligns from the RIGHT and works when:")
print("   - Dimensions are equal, OR")
print("   - One dimension is 1, OR")
print("   - One dimension is missing (treated as 1)")



array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)

print(array1 + array2)
print(array1 * array2)

