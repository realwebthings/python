# NumPy Array Creation Functions - Different ways to create arrays
import numpy as np

print("=" * 60)
print("NUMPY ARRAY CREATION FUNCTIONS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. ZEROS, ONES, AND EMPTY")
print("=" * 50)

# Create arrays filled with zeros
zeros_1d = np.zeros(5)
zeros_2d = np.zeros((3, 4))
print(f"Zeros 1D: {zeros_1d}")
print(f"Zeros 2D:\n{zeros_2d}")

# Create arrays filled with ones
ones_1d = np.ones(4)
ones_2d = np.ones((2, 3))
print(f"\nOnes 1D: {ones_1d}")
print(f"Ones 2D:\n{ones_2d}")

# Create uninitialized arrays (faster but contains garbage)
empty_arr = np.empty(3)
print(f"\nEmpty array: {empty_arr}")
print("Note: Contains random values from memory")

print("\n" + "=" * 50)
print("2. FILLED ARRAYS")
print("=" * 50)

# Fill with specific value
full_arr = np.full(5, 7)
full_2d = np.full((2, 3), 3.14)
print(f"Full array (value=7): {full_arr}")
print(f"Full 2D (value=3.14):\n{full_2d}")

# Create arrays like existing arrays
sample = np.array([[1, 2], [3, 4]])
zeros_like = np.zeros_like(sample)
ones_like = np.ones_like(sample)
full_like = np.full_like(sample, 99)

print(f"\nSample array:\n{sample}")
print(f"Zeros like sample:\n{zeros_like}")
print(f"Ones like sample:\n{ones_like}")
print(f"Full like sample (99):\n{full_like}")

print("\n" + "=" * 50)
print("3. RANGE ARRAYS")
print("=" * 50)

# arange - like Python range
arange_basic = np.arange(10)
arange_range = np.arange(2, 10)
arange_step = np.arange(0, 10, 2)
arange_float = np.arange(0, 1, 0.1)

print(f"arange(10): {arange_basic}")
print(f"arange(2, 10): {arange_range}")
print(f"arange(0, 10, 2): {arange_step}")
print(f"arange(0, 1, 0.1): {arange_float}")

# linspace - evenly spaced numbers
linspace_basic = np.linspace(0, 10, 5)
linspace_inclusive = np.linspace(0, 10, 11, endpoint=True)
linspace_exclusive = np.linspace(0, 10, 10, endpoint=False)

print(f"\nlinspace(0, 10, 5): {linspace_basic}")
print(f"linspace(0, 10, 11, endpoint=True): {linspace_inclusive}")
print(f"linspace(0, 10, 10, endpoint=False): {linspace_exclusive}")

# logspace - logarithmically spaced
logspace_arr = np.logspace(0, 2, 5)  # 10^0 to 10^2
print(f"logspace(0, 2, 5): {logspace_arr}")

print("\n" + "=" * 50)
print("4. IDENTITY AND DIAGONAL MATRICES")
print("=" * 50)

# Identity matrix
identity_3x3 = np.eye(3)
identity_rect = np.eye(3, 4)  # 3x4 identity
print(f"Identity 3x3:\n{identity_3x3}")
print(f"Identity 3x4:\n{identity_rect}")

# Diagonal matrix
diag_values = np.array([1, 2, 3, 4])
diag_matrix = np.diag(diag_values)
print(f"\nDiagonal matrix from {diag_values}:\n{diag_matrix}")

# Extract diagonal from matrix
sample_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
extracted_diag = np.diag(sample_matrix)
print(f"Extract diagonal from matrix: {extracted_diag}")

print("\n" + "=" * 50)
print("5. MESHGRID FOR COORDINATE ARRAYS")
print("=" * 50)

# Create coordinate grids
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)

print(f"x: {x}")
print(f"y: {y}")
print(f"X (meshgrid):\n{X}")
print(f"Y (meshgrid):\n{Y}")
print("Use case: Creating coordinate grids for plotting")

print("\n" + "=" * 50)
print("6. RANDOM ARRAY CREATION")
print("=" * 50)

# Random arrays (using default_rng)
rng = np.random.default_rng(seed=42)

random_uniform = rng.random((2, 3))
random_normal = rng.normal(0, 1, (2, 3))
random_integers = rng.integers(1, 10, (2, 3))

print(f"Random uniform [0,1):\n{random_uniform}")
print(f"Random normal (mean=0, std=1):\n{random_normal}")
print(f"Random integers [1,10):\n{random_integers}")

print("\n" + "=" * 50)
print("ARRAY CREATION SUMMARY")
print("=" * 50)
print("🔢 BASIC CREATION:")
print("  • np.zeros(shape) - Array of zeros")
print("  • np.ones(shape) - Array of ones") 
print("  • np.full(shape, value) - Array filled with value")
print("  • np.empty(shape) - Uninitialized array")
print("\n📏 RANGE CREATION:")
print("  • np.arange(start, stop, step) - Like Python range")
print("  • np.linspace(start, stop, num) - Evenly spaced")
print("  • np.logspace(start, stop, num) - Logarithmically spaced")
print("\n🔲 SPECIAL MATRICES:")
print("  • np.eye(n) - Identity matrix")
print("  • np.diag(array) - Diagonal matrix")
print("  • np.meshgrid(x, y) - Coordinate grids")
print("\n🎲 RANDOM CREATION:")
print("  • rng.random(shape) - Uniform [0,1)")
print("  • rng.normal(mean, std, shape) - Normal distribution")
print("  • rng.integers(low, high, shape) - Random integers")