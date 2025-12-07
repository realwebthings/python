import matplotlib.pyplot as plt
import numpy as np
import time

print("=" * 60)
print("PERFORMANCE COMPARISON: Python Lists vs NumPy Arrays")
print("=" * 60)

# Test with large dataset
size = 1000000

print("\n" + "=" * 50)
print("METHOD 1: Using time module")
print("=" * 50)

# Python lists
start = time.time()
x_list = list(range(size))
y_list = [i * 2 for i in x_list]
end = time.time()
list_time = end - start
print(f"Python lists: {list_time:.4f} seconds")

# NumPy arrays
start = time.time()
x_array = np.arange(size)
y_array = x_array * 2
end = time.time()
numpy_time = end - start
print(f"NumPy arrays: {numpy_time:.4f} seconds")

print(f"\nSpeedup: {list_time/numpy_time:.2f}x faster with NumPy")

print("\n" + "=" * 50)
print("METHOD 2: Using time.perf_counter() (more precise)")
print("=" * 50)

# Python lists
start = time.perf_counter()
x_list = list(range(size))
y_list = [i * 2 for i in x_list]
end = time.perf_counter()
list_time = end - start
print(f"Python lists: {list_time:.6f} seconds")

# NumPy arrays
start = time.perf_counter()
x_array = np.arange(size)
y_array = x_array * 2
end = time.perf_counter()
numpy_time = end - start
print(f"NumPy arrays: {numpy_time:.6f} seconds")

print(f"\nSpeedup: {list_time/numpy_time:.2f}x faster with NumPy")

print("\n" + "=" * 50)
print("METHOD 3: Using timeit module (most accurate)")
print("=" * 50)

import timeit

# Python lists
list_code = """
x = list(range(1000))
y = [i * 2 for i in x]
"""
list_time = timeit.timeit(list_code, number=1000)
print(f"Python lists (1000 runs): {list_time:.6f} seconds")

# NumPy arrays
numpy_code = """
import numpy as np
x = np.arange(1000)
y = x * 2
"""
numpy_time = timeit.timeit(numpy_code, number=1000)
print(f"NumPy arrays (1000 runs): {numpy_time:.6f} seconds")

print(f"\nSpeedup: {list_time/numpy_time:.2f}x faster with NumPy")

print("\n" + "=" * 50)
print("SUMMARY - How to Measure Time")
print("=" * 50)

print("""
1. time.time() - Basic timing
   start = time.time()
   # your code
   end = time.time()
   print(f"Time: {end - start} seconds")

2. time.perf_counter() - More precise (recommended)
   start = time.perf_counter()
   # your code
   end = time.perf_counter()
   print(f"Time: {end - start} seconds")

3. timeit module - Most accurate (for benchmarking)
   import timeit
   time_taken = timeit.timeit('your_code', number=1000)

WHEN TO USE WHAT:
• time.time() - Simple timing, good enough for most cases
• time.perf_counter() - More accurate, better for short operations
• timeit - Best for benchmarking, runs code multiple times
""")
