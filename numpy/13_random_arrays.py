# NumPy Random Number Generation
import numpy as np

print("=" * 60)
print("NUMPY RANDOM NUMBER GENERATION")
print("=" * 60)

print("\n" + "=" * 50)
print("1. CREATING A RANDOM NUMBER GENERATOR")
print("=" * 50)

# Method 1: Without seed (different numbers each time)
print("Without seed (random each time):")
rng_no_seed = np.random.default_rng()
print(f"Random float: {rng_no_seed.random()}")
print(f"Random float: {rng_no_seed.random()}")
print("Note: These numbers change every time you run the program")

# Method 2: With seed (same numbers each time)
print("\nWith seed=1 (reproducible):")
rng = np.random.default_rng(seed=1)
print(f"Random float: {rng.random()}")
print(f"Random float: {rng.random()}")
print("Note: These numbers are the same every time you run with seed=1")

print("\n" + "=" * 50)
print("2. GENERATING RANDOM FLOATS")
print("=" * 50)

# Reset generator for consistent examples
rng = np.random.default_rng(seed=1)

# Generate random float between 0.0 and 1.0
random_float = rng.random()
print(f"rng.random() = {random_float}")
print("Explanation: Generates float between 0.0 (inclusive) and 1.0 (exclusive)")

# Generate multiple random floats
random_floats = rng.random(5)
print(f"\nrng.random(5) = {random_floats}")
print("Explanation: Generates array of 5 random floats between 0.0 and 1.0")

# Generate random floats in custom range using uniform
print("\n" + "-" * 30)
print("UNIFORM DISTRIBUTION (CUSTOM RANGE)")
print("-" * 30)

# Single float between 10.0 and 20.0
uniform_single = rng.uniform(10.0, 20.0)
print(f"rng.uniform(10.0, 20.0) = {uniform_single:.3f}")
print("Explanation: Random float between 10.0 and 20.0")

# Multiple floats in custom range
uniform_array = rng.uniform(low=5.0, high=15.0, size=4)
print(f"\nrng.uniform(low=5.0, high=15.0, size=4) = {uniform_array}")
print("Explanation: 4 random floats between 5.0 and 15.0")

# 2D array of uniform floats
uniform_2d = rng.uniform(-1.0, 1.0, size=(2, 3))
print(f"\nrng.uniform(-1.0, 1.0, size=(2, 3)) =")
print(uniform_2d)
print("Explanation: 2x3 array of floats between -1.0 and 1.0")

print("\n" + "=" * 50)
print("3. GENERATING RANDOM INTEGERS")
print("=" * 50)

# Reset generator
rng = np.random.default_rng(seed=1)

# Single integer from 0 to 6 (7 excluded)
int1 = rng.integers(7)
print(f"rng.integers(7) = {int1}")
print("Explanation: Random integer from 0 to 6 (7 is excluded)")

# Single integer from 1 to 6 (7 excluded)
int2 = rng.integers(1, 7)
print(f"\nrng.integers(1, 7) = {int2}")
print("Explanation: Random integer from 1 to 6 (like a dice roll)")

# Array of 10 integers from 0 to 6
int_array = rng.integers(7, size=10)
print(f"\nrng.integers(7, size=10) = {int_array}")
print("Explanation: Array of 10 random integers, each from 0 to 6")

print("\n" + "=" * 50)
print("4. USING KEYWORD ARGUMENTS")
print("=" * 50)

# Using explicit parameter names for clarity
keyword_ints = rng.integers(low=1, high=7, size=5)
print(f"rng.integers(low=1, high=7, size=5) = {keyword_ints}")
print("Explanation: 5 random integers from 1 to 6 (dice rolls)")
print("Parameters:")
print("  - low=1: minimum value (inclusive)")
print("  - high=7: maximum value (exclusive)")
print("  - size=5: generate 5 numbers")

print("\n" + "=" * 50)
print("5. GENERATING 2D ARRAYS")
print("=" * 50)

# 2D array of random integers
array_2d = rng.integers(low=1, high=100, size=(2, 3))
print(f"rng.integers(low=1, high=100, size=(2, 3)) =")
print(array_2d)
print("Explanation: 2x3 matrix of random integers from 1 to 99")
print(f"Shape: {array_2d.shape}")
print("Parameters:")
print("  - low=1: minimum value")
print("  - high=100: maximum value (exclusive)")
print("  - size=(2, 3): 2 rows, 3 columns")

print("\n" + "=" * 50)
print("6. MORE RANDOM GENERATION METHODS")
print("=" * 50)

# Reset for consistent examples
rng = np.random.default_rng(seed=42)

# Random choice from array
colors = np.array(['red', 'blue', 'green', 'yellow'])
random_color = rng.choice(colors)
print(f"Random color: {random_color}")
print(f"From choices: {colors}")

# Multiple random choices
random_colors = rng.choice(colors, size=3)
print(f"\n3 random colors: {random_colors}")

# Random normal distribution
normal_nums = rng.normal(loc=0, scale=1, size=5)
print(f"\nNormal distribution (mean=0, std=1): {normal_nums}")

# Shuffle an array
data = np.array([1, 2, 3, 4, 5])
print(f"\nOriginal array: {data}")
rng.shuffle(data)
print(f"Shuffled array: {data}")

print("\n" + "=" * 50)
print("RANDOM GENERATION SUMMARY")
print("=" * 50)
print("🎲 rng.random()           - Float between 0.0 and 1.0")
print("🎲 rng.uniform(low, high)  - Float between low and high")
print("🎲 rng.integers(high)     - Integer from 0 to high-1")
print("🎲 rng.integers(low, high) - Integer from low to high-1")
print("🎲 rng.choice(array)      - Random element from array")
print("🎲 rng.normal(mean, std)  - Normal distribution")
print("🎲 rng.shuffle(array)     - Shuffle array in-place")
print("\n🔑 Key Parameters:")
print("   - size: Number of values or shape (e.g., 5 or (2,3))")
print("   - seed: For reproducible results")
print("   - low/high: Range for integers (high is exclusive)")
print("\n💡 Remember:")
print("   - Use seed for reproducible results")
print("   - high parameter is always EXCLUSIVE")
print("   - size can be integer or tuple for multi-dimensional")