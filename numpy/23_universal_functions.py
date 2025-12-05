# NumPy Universal Functions (ufuncs)
import numpy as np

print("=" * 60)
print("NUMPY UNIVERSAL FUNCTIONS (UFUNCS)")
print("=" * 60)

# Sample data
arr = np.array([1, 4, 9, 16, 25])
arr2 = np.array([1, 2, 3, 4, 5])

print(f"Array 1: {arr}")
print(f"Array 2: {arr2}")

print("\n" + "=" * 50)
print("1. MATHEMATICAL UFUNCS")
print("=" * 50)

# Basic math ufuncs
print(f"Square root: {np.sqrt(arr)}")
print(f"Square: {np.square(arr2)}")
print(f"Absolute: {np.abs(np.array([-1, -2, 3, -4]))}")
print(f"Exponential: {np.exp(np.array([0, 1, 2]))}")
print(f"Logarithm: {np.log(arr)}")

print("\n" + "=" * 50)
print("2. TRIGONOMETRIC UFUNCS")
print("=" * 50)

angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(f"Angles: {angles}")
print(f"Sine: {np.sin(angles)}")
print(f"Cosine: {np.cos(angles)}")
print(f"Tangent: {np.tan(angles)}")

print("\n" + "=" * 50)
print("3. BINARY UFUNCS")
print("=" * 50)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"Add: {np.add(a, b)}")
print(f"Subtract: {np.subtract(a, b)}")
print(f"Multiply: {np.multiply(a, b)}")
print(f"Divide: {np.divide(a, b)}")
print(f"Power: {np.power(a, 2)}")
print(f"Maximum: {np.maximum(a, b)}")
print(f"Minimum: {np.minimum(a, b)}")

print("\n" + "=" * 50)
print("4. UFUNC METHODS")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5])

# Reduce method
sum_result = np.add.reduce(arr)
print(f"Add reduce (sum): {sum_result}")

# Accumulate method
cumsum_result = np.add.accumulate(arr)
print(f"Add accumulate (cumsum): {cumsum_result}")

# Outer method
outer_result = np.multiply.outer([1, 2, 3], [4, 5])
print(f"Multiply outer:\n{outer_result}")

print("\n" + "=" * 50)
print("5. CUSTOM UFUNCS")
print("=" * 50)

# Create custom ufunc
def custom_func(x):
    return x * 2 + 1

# Vectorize the function
vectorized_func = np.vectorize(custom_func)
result = vectorized_func(arr)
print(f"Custom function (x*2+1): {result}")

# Using frompyfunc
def add_one(x):
    return x + 1

ufunc_add_one = np.frompyfunc(add_one, 1, 1)
result2 = ufunc_add_one(arr)
print(f"Custom ufunc (add 1): {result2}")

print("\n" + "=" * 50)
print("UFUNCS SUMMARY")
print("=" * 50)
print("CHARACTERISTICS:")
print("- Element-wise operations")
print("- Broadcasting support")
print("- Fast C implementations")
print("- Support for different data types")
print("\nCOMMON UFUNCS:")
print("- Math: sqrt, square, exp, log, abs")
print("- Trig: sin, cos, tan, arcsin, arccos")
print("- Binary: add, subtract, multiply, divide")
print("- Comparison: greater, less, equal")
print("\nUFUNC METHODS:")
print("- reduce(): Apply operation across array")
print("- accumulate(): Cumulative operation")
print("- outer(): Outer product operation")