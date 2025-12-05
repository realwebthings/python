# Multi-dimensional Arrays in NumPy
import numpy as np

print("=" * 60)
print("0-DIMENSIONAL ARRAY (SCALAR)")
print("=" * 60)

# Create a 0-dimensional array (scalar)
array_0d = np.array('A')
print(f"Array: {array_0d}")
print(f"Shape: {array_0d.shape}")          # () - empty tuple means 0D
print(f"Data type: {array_0d.dtype}")      # <U1 - Unicode string, 1 character
print(f"Dimensions: {array_0d.ndim}")      # 0 - zero dimensions
print(f"Size: {array_0d.size}")            # 1 - one element
print(f"Item size: {array_0d.itemsize}")   # 4 - bytes per element
print(f"Total bytes: {array_0d.nbytes}")   # 4 - total memory used
print(f"Real part: {array_0d.real}")       # Real part (for complex numbers)
print(f"Imaginary part: {array_0d.imag}")  # Imaginary part (for complex numbers)
print(f"Data buffer: {array_0d.data}")     # Memory buffer object
print(f"Flags: {array_0d.flags}")          # Array flags (C_CONTIGUOUS, etc.)
print(f"Strides: {array_0d.strides}")      # () - steps to next element
print(f"Base: {array_0d.base}")            # None - base array if view
print(f"C types: {array_0d.ctypes}")       # C-compatible data types
print(f"Array interface: {array_0d.__array_interface__}")  # Array protocol info

print("\n" + "=" * 60)
print("1-DIMENSIONAL ARRAY (VECTOR)")
print("=" * 60)

# Create a 1-dimensional array (vector)
array_1d = np.array([1, 2, 3, 4, 5])
print(f"Array: {array_1d}")
print(f"Shape: {array_1d.shape}")          # (5,) - 5 elements in 1 dimension
print(f"Data type: {array_1d.dtype}")      # int64 - 64-bit integer
print(f"Dimensions: {array_1d.ndim}")      # 1 - one dimension
print(f"Size: {array_1d.size}")            # 5 - five elements total
print(f"Item size: {array_1d.itemsize}")   # 8 - bytes per element (int64)
print(f"Total bytes: {array_1d.nbytes}")   # 40 - total memory (5 * 8 bytes)

print("\n" + "=" * 60)
print("2-DIMENSIONAL ARRAY (MATRIX)")
print("=" * 60)

# Create a 2-dimensional array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array:\n{array_2d}")
print(f"Shape: {array_2d.shape}")           # (2, 3) - 2 rows, 3 columns
print(f"Data type: {array_2d.dtype}")      # int64 - 64-bit integer
print(f"Dimensions: {array_2d.ndim}")      # 2 - two dimensions
print(f"Size: {array_2d.size}")            # 6 - six elements total (2*3)
print(f"Item size: {array_2d.itemsize}")   # 8 - bytes per element
print(f"Total bytes: {array_2d.nbytes}")   # 48 - total memory (6 * 8 bytes)
print(f"Strides: {array_2d.strides}")      # (24, 8) - steps to next row/column

print("\n" + "=" * 60)
print("3-DIMENSIONAL ARRAY (TENSOR)")
print("=" * 60)

# Create a 3-dimensional array (tensor)
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"Array:\n{array_3d}")
print(f"Shape: {array_3d.shape}")           # (2, 2, 2) - 2x2x2 cube
print(f"Data type: {array_3d.dtype}")      # int64
print(f"Dimensions: {array_3d.ndim}")      # 3 - three dimensions
print(f"Size: {array_3d.size}")            # 8 - eight elements total
print(f"Strides: {array_3d.strides}")      # Steps to next element in each dimension

print("\n" + "=" * 60)
print("ARRAY ATTRIBUTES SUMMARY")
print("=" * 60)
print("• shape: Dimensions of the array (rows, columns, etc.)")
print("• dtype: Data type of elements (int64, float64, etc.)")
print("• ndim: Number of dimensions (0D, 1D, 2D, 3D, etc.)")
print("• size: Total number of elements")
print("• itemsize: Size of each element in bytes")
print("• nbytes: Total memory used (size * itemsize)")
print("• strides: Steps in bytes to next element in each dimension")
print("• real/imag: Real and imaginary parts (for complex numbers)")
print("• data: Memory buffer containing the array data")
print("• flags: Array properties (contiguous, writable, etc.)")
print("• base: Base array if this is a view, None otherwise")



# array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7]]]) # Error as elements are not continous
array_3d = np.array([
                        [
                            [1, 2],
                            [3, 4]
                        ], 
                        [
                            [5, 6],
                            [7, 8]
                        ]
                    ]) # Fixed by adding 8 

print(f"Array:\n{array_3d}")
print(f"Shape: {array_3d.shape}")           # (2, 2, 2) - 2x2x2 cube
print(array_3d[0][0][0])
print(array_3d[0, 0, 0])

num = array_3d[0, 0, 0] + array_3d[1, 1, 1] + array_3d[0, 1, 1] + array_3d[1, 0, 1]
print(num)

print("\n" + "=" * 60)
print("INHOMOGENEOUS SHAPES - WHAT HAPPENS WHEN DIMENSIONS DON'T MATCH")
print("=" * 60)

print("\n" + "-" * 40)
print("EXAMPLE 1: INHOMOGENEOUS 2D ARRAY")
print("-" * 40)

print("❌ PROBLEMATIC CODE:")
print("array_inhomo = np.array([[1, 2, 3], [4, 5]])  # Different row lengths")
print("\nWhat happens:")

# This creates an object array, not a regular NumPy array
# array_inhomo = np.array([[1, 2, 3], [4, 5]])
# print(f"Result: {array_inhomo}")
# print(f"Shape: {array_inhomo.shape}")
# print(f"Data type: {array_inhomo.dtype}")
# print(f"Dimensions: {array_inhomo.ndim}")
print("\nExplanation: NumPy creates an object array containing Python lists")
print("This is NOT a regular NumPy array - it's less efficient!")

print("\n" + "-" * 40)
print("EXAMPLE 2: INHOMOGENEOUS 3D ARRAY (YOUR COMMENTED CODE)")
print("-" * 40)

print("❌ PROBLEMATIC CODE:")
print("array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7]]])  # Missing element")
print("\nWhat happens:")

# This also creates an object array
# array_inhomo_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7]]])
# print(f"Result: {array_inhomo_3d}")
# print(f"Shape: {array_inhomo_3d.shape}")
# print(f"Data type: {array_inhomo_3d.dtype}")
print("\nExplanation: The second sub-array has only one element [7] instead of two")
print("NumPy can't create a regular 3D array, so it creates an object array")

print("\n" + "-" * 40)
print("EXAMPLE 3: MIXED DATA TYPES")
print("-" * 40)

# Mixed data types also create object arrays
# mixed_array = np.array([1, 'hello', [1, 2, 3]])
# print(f"Mixed array: {mixed_array}")
# print(f"Shape: {mixed_array.shape}")
# print(f"Data type: {mixed_array.dtype}")
print("\nExplanation: Can't have a single data type for numbers, strings, and lists")

print("\n" + "-" * 40)
print("WHY OBJECT ARRAYS ARE PROBLEMATIC:")
print("-" * 40)

# Compare performance and functionality
regular_array = np.array([[1, 2, 3], [4, 5, 6]])
object_array = np.array([[1, 2, 3], [4, 5]])

print(f"Regular array shape: {regular_array.shape}")
print(f"Object array shape: {object_array.shape}")
print("\nProblems with object arrays:")
print("• No vectorized operations (slower)")
print("• Can't use most NumPy functions")
print("• Unpredictable behavior")
print("• More memory usage")

# Try to demonstrate the difference
print("\nTrying vectorized operations:")
try:
    print(f"Regular array * 2: {regular_array * 2}")
except Exception as e:
    print(f"Regular array failed: {e}")

try:
    result = object_array * 2
    print(f"Object array * 2: {result}")
    print("Note: This works but may not do what you expect!")
except Exception as e:
    print(f"Object array failed: {e}")

print("\n" + "-" * 40)
print("HOW TO FIX INHOMOGENEOUS SHAPES:")
print("-" * 40)

print("✅ SOLUTION 1: Pad with zeros or fill values")
# Pad shorter arrays with zeros
padded_array = np.array([[1, 2, 3], [4, 5, 0]])  # Add 0 to make same length
print(f"Padded array: {padded_array}")
print(f"Shape: {padded_array.shape}")
print(f"Data type: {padded_array.dtype}")

print("\n✅ SOLUTION 2: Use np.nan for missing values")
nan_array = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, np.nan]])
print(f"NaN array: {nan_array}")
print(f"Shape: {nan_array.shape}")
print(f"Data type: {nan_array.dtype}")

print("\n✅ SOLUTION 3: Use separate arrays")
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5])
print(f"Array 1: {array1} (shape: {array1.shape})")
print(f"Array 2: {array2} (shape: {array2.shape})")
print("Keep them separate and process individually")

print("\n✅ SOLUTION 4: Use lists when you need variable lengths")
jagged_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"Jagged list: {jagged_list}")
print("Use Python lists for truly variable-length data")

print("\n" + "-" * 40)
print("DETECTING OBJECT ARRAYS:")
print("-" * 40)

def check_array_type(arr, name):
    print(f"{name}:")
    print(f"  Shape: {arr.shape}")
    print(f"  Data type: {arr.dtype}")
    print(f"  Is object array: {arr.dtype == object}")
    print(f"  Can do vectorized ops: {arr.dtype != object}")
    print()

check_array_type(regular_array, "Regular array")
check_array_type(object_array, "Object array")
check_array_type(mixed_array, "Mixed array")

print("-" * 40)
print("BEST PRACTICES FOR AVOIDING INHOMOGENEOUS SHAPES:")
print("-" * 40)
print("💡 PREVENTION TIPS:")
print("• Always ensure all sub-arrays have the same length")
print("• Use consistent data types throughout")
print("• Pad shorter sequences with appropriate fill values")
print("• Check array.dtype after creation - avoid 'object'")
print("• Use np.full() or np.zeros() to pre-allocate with correct shape")
print("\n🔍 DETECTION:")
print("• Check if array.dtype == object")
print("• Unexpected shape (like (2,) instead of (2, 3))")
print("• Vectorized operations don't work as expected")
print("\n⚙️ SOLUTIONS:")
print("• Reshape or pad data to make it rectangular")
print("• Use np.nan for missing numeric values")
print("• Keep variable-length data as separate arrays")
print("• Use Python lists when you truly need jagged arrays")

print("\n" + "=" * 60)
print("SUMMARY: HOMOGENEOUS vs INHOMOGENEOUS")
print("=" * 60)
print("✅ HOMOGENEOUS (Good):")
print("  • All rows/columns have same length")
print("  • Same data type throughout")
print("  • Regular NumPy array (int64, float64, etc.)")
print("  • Fast vectorized operations")
print("  • Predictable shape")
print("\n❌ INHOMOGENEOUS (Problematic):")
print("  • Different row/column lengths")
print("  • Mixed data types")
print("  • Object array (dtype=object)")
print("  • Slow operations")
print("  • Limited NumPy functionality")
print("\n🎯 GOAL: Always aim for homogeneous arrays for best performance!")