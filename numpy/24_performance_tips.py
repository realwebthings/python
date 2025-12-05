# NumPy Performance Tips and Best Practices
import numpy as np
import time

print("=" * 60)
print("NUMPY PERFORMANCE TIPS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. VECTORIZATION VS LOOPS")
print("=" * 50)

# Create large arrays
size = 1000000
a = np.random.random(size)
b = np.random.random(size)

# Python loop (slow)
start = time.time()
result_loop = []
for i in range(len(a)):
    result_loop.append(a[i] + b[i])
loop_time = time.time() - start

# NumPy vectorization (fast)
start = time.time()
result_vectorized = a + b
vectorized_time = time.time() - start

print(f"Loop time: {loop_time:.4f} seconds")
print(f"Vectorized time: {vectorized_time:.4f} seconds")
print(f"Speedup: {loop_time/vectorized_time:.1f}x faster")

print("\n" + "=" * 50)
print("2. MEMORY LAYOUT - C vs FORTRAN ORDER")
print("=" * 50)

# C-order (row-major) - default
c_order = np.random.random((1000, 1000))
# Fortran-order (column-major)
f_order = np.random.random((1000, 1000)).T

print(f"C-order flags: {c_order.flags}")
print(f"F-order flags: {f_order.flags}")

# Row access performance
start = time.time()
for i in range(100):
    _ = c_order[i, :].sum()
c_row_time = time.time() - start

start = time.time()
for i in range(100):
    _ = f_order[i, :].sum()
f_row_time = time.time() - start

print(f"C-order row access: {c_row_time:.4f}s")
print(f"F-order row access: {f_row_time:.4f}s")

print("\n" + "=" * 50)
print("3. IN-PLACE OPERATIONS")
print("=" * 50)

# Create test array
arr = np.random.random(100000)
arr_copy = arr.copy()

# Not in-place (creates new array)
start = time.time()
result1 = arr * 2
not_inplace_time = time.time() - start

# In-place operation
start = time.time()
arr_copy *= 2
inplace_time = time.time() - start

print(f"Not in-place: {not_inplace_time:.6f}s")
print(f"In-place: {inplace_time:.6f}s")
print("In-place operations save memory and can be faster")

print("\n" + "=" * 50)
print("4. AVOID UNNECESSARY COPIES")
print("=" * 50)

# Views vs copies
original = np.random.random((1000, 1000))

# View (no copy)
start = time.time()
view = original[::2, ::2]  # Every other element
view_time = time.time() - start

# Copy
start = time.time()
copy = original[::2, ::2].copy()
copy_time = time.time() - start

print(f"View creation: {view_time:.6f}s")
print(f"Copy creation: {copy_time:.6f}s")
print(f"View is {copy_time/view_time:.1f}x faster")

print("\n" + "=" * 50)
print("5. CHOOSE APPROPRIATE DATA TYPES")
print("=" * 50)

# Memory usage comparison
size = 1000000
int64_array = np.ones(size, dtype=np.int64)
int32_array = np.ones(size, dtype=np.int32)
int8_array = np.ones(size, dtype=np.int8)

print(f"int64 memory: {int64_array.nbytes / 1024 / 1024:.1f} MB")
print(f"int32 memory: {int32_array.nbytes / 1024 / 1024:.1f} MB")
print(f"int8 memory: {int8_array.nbytes / 1024 / 1024:.1f} MB")

# Performance comparison
start = time.time()
_ = int64_array.sum()
int64_time = time.time() - start

start = time.time()
_ = int32_array.sum()
int32_time = time.time() - start

print(f"int64 sum time: {int64_time:.6f}s")
print(f"int32 sum time: {int32_time:.6f}s")

print("\n" + "=" * 50)
print("6. USE BUILT-IN FUNCTIONS")
print("=" * 50)

arr = np.random.random(100000)

# Manual implementation
start = time.time()
manual_mean = arr.sum() / len(arr)
manual_time = time.time() - start

# Built-in function
start = time.time()
builtin_mean = np.mean(arr)
builtin_time = time.time() - start

print(f"Manual mean: {manual_time:.6f}s")
print(f"Built-in mean: {builtin_time:.6f}s")
print(f"Built-in is {manual_time/builtin_time:.1f}x faster")

print("\n" + "=" * 50)
print("PERFORMANCE BEST PRACTICES")
print("=" * 50)
print("✅ DO:")
print("- Use vectorized operations instead of loops")
print("- Use in-place operations when possible")
print("- Choose appropriate data types")
print("- Use views instead of copies when safe")
print("- Use built-in NumPy functions")
print("- Consider memory layout for access patterns")
print("\n❌ DON'T:")
print("- Use Python loops on large arrays")
print("- Create unnecessary copies")
print("- Use larger data types than needed")
print("- Mix different data types unnecessarily")
print("- Ignore memory access patterns")

print("\n" + "=" * 50)
print("MEMORY OPTIMIZATION TIPS")
print("=" * 50)
print("🧠 MEMORY EFFICIENCY:")
print("- Use smallest suitable data type")
print("- Delete large arrays when done: del array")
print("- Use memory-mapped files for huge datasets")
print("- Consider sparse matrices for sparse data")
print("- Use views instead of copies when possible")
print("\n⚡ SPEED OPTIMIZATION:")
print("- Vectorize operations")
print("- Use NumPy's built-in functions")
print("- Minimize array creation in loops")
print("- Use appropriate algorithms (e.g., searchsorted)")
print("- Consider numba for complex operations")