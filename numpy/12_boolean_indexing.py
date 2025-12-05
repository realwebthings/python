# NumPy Array Filtering - Selecting elements based on conditions
import numpy as np

print("=" * 60)
print("NUMPY ARRAY FILTERING")
print("=" * 60)
print("Filtering allows you to select elements from arrays based on conditions")
print("It returns a new array containing only elements that meet the criteria")

print("\n" + "=" * 60)
print("EXAMPLE 1: BASIC FILTERING WITH 1D ARRAY")
print("=" * 60)

# Create a 1D array of ages
ages = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Original ages: {ages}")
print(f"Array shape: {ages.shape}")

# Create a boolean mask
mask = ages > 50
print(f"\nBoolean mask (ages > 50): {mask}")
print(f"Mask type: {type(mask)}")

# Apply the filter
seniors = ages[ages > 50]
print(f"\nFiltered result (ages > 50): {seniors}")
print(f"Number of seniors: {len(seniors)}")

print("\n" + "=" * 60)
print("EXAMPLE 2: FILTERING WITH 2D ARRAY")
print("=" * 60)

# Create a 2D array
ages_2d = np.array([[10, 12, 16, 18, 20, 21, 24, 30], 
                    [40, 42, 45, 48, 50, 55, 60, 70]])
print(f"2D ages array:")
print(ages_2d)
print(f"Shape: {ages_2d.shape}")

# Filter teenagers (< 18)
teenagers = ages_2d[ages_2d < 18]
print(f"\nTeenagers (< 18): {teenagers}")
print("Note: Filtering flattens 2D arrays into 1D")

print("\n" + "=" * 60)
print("EXAMPLE 3: MULTIPLE CONDITIONS (THE ERROR YOU SAW)")
print("=" * 60)

print("❌ WRONG WAY (causes error):")
print("adults = ages[(ages >= 18) and (ages < 60)]")
print("Error: 'and' doesn't work with NumPy arrays")

print("\n✅ CORRECT WAY:")
print("Use & (bitwise AND) instead of 'and'")
print("Use | (bitwise OR) instead of 'or'")
print("Use ~ (bitwise NOT) instead of 'not'")
print("Always use parentheses around each condition!")

# Correct way to combine conditions
adults = ages_2d[(ages_2d >= 18) & (ages_2d < 60)]
print(f"\nAdults (18 <= age < 60): {adults}")

print("\n" + "=" * 60)
print("EXAMPLE 4: MORE COMPLEX FILTERING")
print("=" * 60)

# Create sample data
scores = np.array([85, 92, 78, 96, 88, 73, 91, 82, 95, 79])
names = np.array(['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 
                  'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'])

print(f"Scores: {scores}")
print(f"Names: {names}")

# Filter high performers (score >= 90)
print("\n" + "-" * 40)
print("DETAILED LOOK AT BOOLEAN MASK:")
print("-" * 40)

high_scores_mask = scores >= 90
print(f"\nBoolean mask (scores >= 90):")
print(f"high_scores_mask = {high_scores_mask}")
print(f"Mask type: {type(high_scores_mask)}")
print(f"Mask shape: {high_scores_mask.shape}")
print(f"Mask dtype: {high_scores_mask.dtype}")

print(f"\nStep-by-step breakdown:")
for i, (score, is_high) in enumerate(zip(scores, high_scores_mask)):
    status = "✅ SELECTED" if is_high else "❌ FILTERED OUT"
    print(f"  Index {i}: {names[i]:8} score={score:2d} >= 90? {is_high} {status}")

print(f"\nHow filtering works:")
print(f"1. scores >= 90 creates boolean mask: {high_scores_mask}")
print(f"2. names[mask] selects only True positions")
print(f"3. Result: names at positions {np.where(high_scores_mask)[0]}")

high_performers = names[high_scores_mask]
high_scores_values = scores[high_scores_mask]

print(f"\nFinal results - High performers (score >= 90):")
for name, score in zip(high_performers, high_scores_values):
    print(f"  {name}: {score}")

# Multiple conditions: good but not excellent (80 <= score < 90)
good_mask = (scores >= 80) & (scores < 90)
good_performers = names[good_mask]
good_scores = scores[good_mask]

print(f"\nGood performers (80 <= score < 90):")
for name, score in zip(good_performers, good_scores):
    print(f"  {name}: {score}")

# Using OR condition: either very high (>= 95) or struggling (<= 75)
extreme_mask = (scores >= 95) | (scores <= 75)
extreme_performers = names[extreme_mask]
extreme_scores = scores[extreme_mask]

print(f"\nExtreme performers (>= 95 OR <= 75):")
for name, score in zip(extreme_performers, extreme_scores):
    print(f"  {name}: {score}")

print("\n" + "=" * 60)
print("EXAMPLE 5: FILTERING WITH WHERE()")
print("=" * 60)

# np.where() is another way to filter/replace values
data = np.array([1, -2, 3, -4, 5, -6, 7, -8])
print(f"Original data: {data}")

# Replace negative values with 0
positive_only = np.where(data > 0, data, 0)
print(f"Replace negatives with 0: {positive_only}")

# Get indices where condition is true
negative_indices = np.where(data < 0)
print(f"Indices of negative values: {negative_indices[0]}")
print(f"Negative values: {data[negative_indices]}")

print("\n" + "=" * 60)
print("FILTERING OPERATORS SUMMARY")
print("=" * 60)
print("✅ CORRECT for NumPy arrays:")
print("  & (bitwise AND)    - Use instead of 'and'")
print("  | (bitwise OR)     - Use instead of 'or'")
print("  ~ (bitwise NOT)    - Use instead of 'not'")
print("  Always use parentheses: (condition1) & (condition2)")
print("\n❌ WRONG for NumPy arrays:")
print("  and, or, not - These cause 'ambiguous truth value' errors")
print("\n🔍 Comparison operators (work normally):")
print("  ==, !=, <, <=, >, >= - Create boolean masks")
print("\n💡 Remember:")
print("  - Filtering flattens multi-dimensional arrays")
print("  - Boolean masks have the same shape as original array")
print("  - Use np.where() for conditional replacement")



print("\n" + "=" * 60)

print("NumPy where")

print("=" * 60)

ages = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

filtered_ages = np.where(ages > 50, ages, 0) # 0 is the replacement value

print(filtered_ages)