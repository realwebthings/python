# NumPy Data Types - Understanding different data types and their limits
import numpy as np

print("=" * 70)
print("NUMPY DATA TYPES AND OVERFLOW ERRORS")
print("=" * 70)

print("\n" + "=" * 50)
print("1. DEFAULT DATA TYPE (AUTO-DETECTED)")
print("=" * 50)

# NumPy automatically detects data type
array = np.array([1, 2, 3, 4, 5])
print(f"Array: {array}")
print(f"Data type: {array.dtype} (auto-detected)")
print(f"Item size: {array.itemsize} bytes per element")
print(f"Total memory: {array.nbytes} bytes")
print("Explanation: NumPy chose int64 because it's the default for integers")

print("\n" + "=" * 50)
print("2. EXPLICIT DATA TYPES")
print("=" * 50)

# Explicitly specify int64
array2 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print(f"\nint64 array: {array2}")
print(f"Data type: {array2.dtype}")
print(f"Item size: {array2.itemsize} bytes")
print(f"Range: {np.iinfo(np.int64).min:,} to {np.iinfo(np.int64).max:,}")

# Float64
array3 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(f"\nfloat64 array: {array3}")
print(f"Data type: {array3.dtype}")
print(f"Item size: {array3.itemsize} bytes")
print(f"Range: {np.finfo(np.float64).min:.2e} to {np.finfo(np.float64).max:.2e}")

print("\n" + "=" * 50)
print("3. THE OVERFLOW ERROR EXPLAINED")
print("=" * 50)

print("❌ PROBLEMATIC CODE:")
print("array4 = np.array([100, 200, 300, 4, 5], dtype=np.int8)")
print("\nWhy it fails:")
print(f"int8 range: {np.iinfo(np.int8).min} to {np.iinfo(np.int8).max}")
print("Values 200 and 300 are outside this range!")

print("\n✅ FIXED VERSION:")
# Use values that fit in int8 range
array4_fixed = np.array([100, 120, 127, 4, 5], dtype=np.int8)
print(f"array4_fixed = np.array([100, 120, 127, 4, 5], dtype=np.int8)")
print(f"Result: {array4_fixed}")
print(f"Data type: {array4_fixed.dtype}")
print(f"Item size: {array4_fixed.itemsize} byte (very memory efficient!)")
print("All values are within -128 to 127 range ✅")

print("\n" + "=" * 50)
print("4. DATA TYPE RANGES COMPARISON")
print("=" * 50)

# Show ranges for different integer types
integer_types = [np.int8, np.int16, np.int32, np.int64]
print("INTEGER TYPES:")
for dtype in integer_types:
    info = np.iinfo(dtype)
    print(f"{dtype.__name__:>6}: {info.min:>12,} to {info.max:>20,} ({dtype().itemsize} bytes)")

print("\nUNSIGNED INTEGER TYPES:")
unsigned_types = [np.uint8, np.uint16, np.uint32, np.uint64]
for dtype in unsigned_types:
    info = np.iinfo(dtype)
    print(f"{dtype.__name__:>6}: {info.min:>12,} to {info.max:>20,} ({dtype().itemsize} bytes)")

print("\nFLOAT TYPES:")
float_types = [np.float16, np.float32, np.float64]
for dtype in float_types:
    info = np.finfo(dtype)
    print(f"{dtype.__name__:>8}: {info.min:>12.2e} to {info.max:>12.2e} ({dtype().itemsize} bytes)")

print("\nBOOLEAN TYPE:")
bool_array = np.array([True, False, True], dtype=np.bool_)
print(f"{'bool_':>8}: True or False only ({bool_array.itemsize} byte per element)")
print(f"Example: {bool_array}")

print("\nSTRING TYPES:")
# Fixed-length string
string_array = np.array(['hello', 'world', 'numpy'], dtype=np.str_)  # Unicode, max 10 chars
print(f"{'U10':>8}: Unicode string, max 10 chars ({string_array.itemsize} bytes per element)")
print(f"Example: {string_array}")

# Variable-length string (object type)
string_obj = np.array(['short', 'much longer string', 'x'], dtype=np.object_)
print(f"{'object':>8}: Variable-length strings ({string_obj.itemsize} bytes pointer)")
print(f"Example: {string_obj}")

print("\n" + "=" * 50)
print("5. CHOOSING THE RIGHT DATA TYPE")
print("=" * 50)

# Example: Age data (0-120)
ages = np.array([25, 30, 45, 67, 89], dtype=np.uint8)  # uint8: 0-255
print(f"Ages: {ages}")
print(f"dtype: {ages.dtype} - Memory: {ages.nbytes} bytes")

# Example: Temperature data (-50 to 50)
temps = np.array([-10, 0, 25, 40, -5], dtype=np.int8)  # int8: -128 to 127
print(f"\nTemperatures: {temps}")
print(f"dtype: {temps.dtype} - Memory: {temps.nbytes} bytes")

# Example: Large numbers
large_nums = np.array([1000000, 2000000, 3000000], dtype=np.int32)
print(f"\nLarge numbers: {large_nums}")
print(f"dtype: {large_nums.dtype} - Memory: {large_nums.nbytes} bytes")

# Example: Precise decimals
precise = np.array([3.14159265359, 2.71828182846], dtype=np.float64)
print(f"\nPrecise floats: {precise}")
print(f"dtype: {precise.dtype} - Memory: {precise.nbytes} bytes")

print("\n" + "-" * 40)
print("BOOLEAN AND STRING EXAMPLES:")
print("-" * 40)

# Boolean arrays
bool_flags = np.array([True, False, True, False, True], dtype=np.bool_)
print(f"Boolean flags: {bool_flags}")
print(f"dtype: {bool_flags.dtype} - Memory: {bool_flags.nbytes} bytes")
print("Use case: Masks, flags, conditions")

# Boolean from conditions
numbers = np.array([1, 5, 10, 15, 20])
mask = numbers > 10
print(f"\nCondition mask (numbers > 10): {mask}")
print(f"Mask type: {mask.dtype}")
print(f"Filtered numbers: {numbers[mask]}")

# Fixed-length strings
names = np.array(['Alice', 'Bob', 'Charlie'], dtype='U10')
print(f"\nFixed-length strings: {names}")
print(f"dtype: {names.dtype}")
print(f"Memory per element: {names.itemsize} bytes")
print(f"Total memory: {names.nbytes} bytes")

# What happens with longer strings?
long_names = np.array(['Alice', 'Bob', 'Christopher'], dtype='U5')  # Only 5 chars allowed
print(f"\nTruncated strings (U5): {long_names}")
print("Note: 'Christopher' was truncated to 'Chris'")

# Variable-length strings (object type)
var_strings = np.array(['short', 'medium length', 'very very long string'], dtype=object)
print(f"\nVariable-length strings: {var_strings}")
print(f"dtype: {var_strings.dtype}")
print(f"Memory: {var_strings.itemsize} bytes per pointer (actual strings stored elsewhere)")

# String operations
print(f"\nString operations:")
print(f"Uppercase: {np.char.upper(names)}")
print(f"String lengths: {np.char.str_len(names)}")
print(f"Contains 'o': {np.char.find(names, 'o') >= 0}")

print("\n" + "=" * 50)
print("6. WHAT HAPPENS WITH OVERFLOW?")
print("=" * 50)

print("Option 1: Use larger data type")
large_values = np.array([100, 200, 300, 400, 500], dtype=np.int16)  # int16: -32,768 to 32,767
print(f"Array: {large_values}")
print(f"dtype: {large_values.dtype} ✅")

print("\nOption 2: Use unsigned type for positive-only values")
positive_values = np.array([100, 200, 255], dtype=np.uint8)  # uint8: 0 to 255
print(f"Array: {positive_values}")
print(f"dtype: {positive_values.dtype} ✅")

print("\nOption 3: Check if values fit before creating array")
values = [100, 200, 300, 4, 5]
max_val = max(values)
min_val = min(values)
print(f"Values range: {min_val} to {max_val}")
print(f"int8 range: {np.iinfo(np.int8).min} to {np.iinfo(np.int8).max}")
if min_val >= np.iinfo(np.int8).min and max_val <= np.iinfo(np.int8).max:
    print("✅ Values fit in int8")
else:
    print("❌ Values DON'T fit in int8 - use larger type!")
    recommended_array = np.array(values, dtype=np.int16)
    print(f"Recommended: use int16 → {recommended_array}")

print("\n" + "=" * 50)
print("DATA TYPE SELECTION GUIDE")
print("=" * 50)
print("🎯 CHOOSE DATA TYPE BASED ON:")
print("\n📊 INTEGER DATA:")
print("  • int8 (-128 to 127): Small integers, temperatures")
print("  • uint8 (0 to 255): Ages, percentages, RGB values")
print("  • int16 (-32K to 32K): Coordinates, small measurements")
print("  • int32 (-2B to 2B): IDs, large counts")
print("  • int64 (default): When unsure, very large numbers")
print("\n📈 FLOAT DATA:")
print("  • float16: Low precision, memory-critical applications")
print("  • float32: Standard precision, graphics, ML")
print("  • float64 (default): High precision, scientific computing")
print("\n🔘 BOOLEAN DATA:")
print("  • bool_: True/False values, 1 byte each")
print("  • Use for: Masks, flags, conditions, logical operations")
print("  • Memory efficient for binary data")
print("\n📝 STRING DATA:")
print("  • 'U' + number: Fixed Unicode strings (e.g., 'U10' = max 10 chars)")
print("  • object: Variable-length strings (uses more memory)")
print("  • Use 'U' for consistent-length text, object for variable text")
print("\n💡 MEMORY vs PRECISION:")
print("  • Smaller types = Less memory, Limited range")
print("  • Larger types = More memory, Greater range/precision")
print("  • Fixed strings = Predictable memory, may truncate")
print("  • Object strings = Flexible but more memory overhead")
print("\n⚠️  OVERFLOW PREVENTION:")
print("  • Always check value ranges before choosing type")
print("  • Use np.iinfo() and np.finfo() to check limits")
print("  • For strings, choose appropriate max length")
print("  • When in doubt, use default types (int64, float64, object)")

print("\n" + "=" * 50)
print("7. BOOLEAN AND STRING SPECIAL CASES")
print("=" * 50)

print("🔘 BOOLEAN MEMORY EFFICIENCY:")
regular_list = [True, False, True, False, True] * 1000  # Python list
np_bool_array = np.array(regular_list, dtype=np.bool_)  # NumPy boolean array
print(f"5000 booleans as Python list: ~{len(regular_list) * 28} bytes (approx)")
print(f"5000 booleans as NumPy array: {np_bool_array.nbytes} bytes")
print("NumPy boolean arrays are much more memory efficient!")

print("\n📝 STRING LENGTH CONSIDERATIONS:")
print("Choose string length wisely:")
short_strings = np.array(['a', 'bb', 'ccc'], dtype='U3')
long_strings = np.array(['a', 'bb', 'ccc'], dtype='U100')
print(f"U3 array memory: {short_strings.nbytes} bytes")
print(f"U100 array memory: {long_strings.nbytes} bytes")
print("Same data, but U100 uses much more memory!")

print("\n🎯 WHEN TO USE EACH TYPE:")
print("• bool_: Flags, masks, True/False data")
print("• U + number: Names, codes, fixed-format text")
print("• object: Variable text, mixed-length strings")
print("• Example: User IDs (U10), Descriptions (object), Active flags (bool_)")

print("\n" + "=" * 50)
print("8. DATA TYPE CONVERSION WITH astype()")
print("=" * 50)
print("astype() allows you to convert arrays from one data type to another")

print("\n" + "-" * 40)
print("INTEGER CONVERSIONS:")
print("-" * 40)

# Start with int64 array
original = np.array([1, 2, 3, 4, 5])
print(f"Original: {original}")
print(f"dtype: {original.dtype}")

# Convert to different integer types
int8_version = original.astype(np.int8)
print(f"\nConverted to int8: {int8_version}")
print(f"dtype: {int8_version.dtype}")
print(f"Memory: {original.nbytes} bytes → {int8_version.nbytes} bytes")

uint16_version = original.astype(np.uint16)
print(f"\nConverted to uint16: {uint16_version}")
print(f"dtype: {uint16_version.dtype}")

print("\n" + "-" * 40)
print("FLOAT CONVERSIONS:")
print("-" * 40)

# Integer to float
int_array = np.array([1, 2, 3, 4, 5])
float_array = int_array.astype(np.float32)
print(f"Integer: {int_array} (dtype: {int_array.dtype})")
print(f"To float32: {float_array} (dtype: {float_array.dtype})")

# Float to integer (truncates decimals)
float_data = np.array([3.7, 2.1, 8.9, 1.2])
int_data = float_data.astype(np.int32)
print(f"\nFloat: {float_data} (dtype: {float_data.dtype})")
print(f"To int32: {int_data} (dtype: {int_data.dtype})")
print("Note: Decimals are truncated, not rounded!")

print("\n" + "-" * 40)
print("BOOLEAN CONVERSIONS:")
print("-" * 40)

# Numbers to boolean
numbers = np.array([0, 1, 2, -1, 0, 5])
bools = numbers.astype(np.bool_)
print(f"Numbers: {numbers} (dtype: {numbers.dtype})")
print(f"To bool: {bools} (dtype: {bools.dtype})")
print("Rule: 0 = False, everything else = True")

# Boolean to numbers
bool_array = np.array([True, False, True, False])
int_from_bool = bool_array.astype(np.int32)
print(f"\nBooleans: {bool_array} (dtype: {bool_array.dtype})")
print(f"To int32: {int_from_bool} (dtype: {int_from_bool.dtype})")
print("Rule: True = 1, False = 0")

print("\n" + "-" * 40)
print("STRING CONVERSIONS:")
print("-" * 40)

# Numbers to strings
number_array = np.array([123, 456, 789])
string_array = number_array.astype('U10')
print(f"Numbers: {number_array} (dtype: {number_array.dtype})")
print(f"To strings: {string_array} (dtype: {string_array.dtype})")

# Strings to numbers (if possible)
string_numbers = np.array(['10', '20', '30'])
back_to_int = string_numbers.astype(np.int32)
print(f"\nString numbers: {string_numbers} (dtype: {string_numbers.dtype})")
print(f"To int32: {back_to_int} (dtype: {back_to_int.dtype})")

# What happens with invalid conversions?
print("\n⚠️  INVALID CONVERSIONS:")
try:
    invalid_strings = np.array(['hello', 'world'])
    invalid_conversion = invalid_strings.astype(np.int32)
except ValueError as e:
    print(f"Error converting ['hello', 'world'] to int32: {e}")
    print("Solution: Only convert strings that represent valid numbers")

print("\n" + "-" * 40)
print("PRECISION LOSS EXAMPLES:")
print("-" * 40)

# Float64 to float32 (precision loss)
high_precision = np.array([3.141592653589793, 2.718281828459045])
low_precision = high_precision.astype(np.float32)
print(f"High precision (float64): {high_precision}")
print(f"Low precision (float32):  {low_precision}")
print("Note: Some decimal places are lost")

# Large numbers to small types (overflow risk)
large_numbers = np.array([1000, 2000, 3000])
print(f"\nLarge numbers: {large_numbers} (dtype: {large_numbers.dtype})")
try:
    small_type = large_numbers.astype(np.int8)  # int8 max is 127
    print(f"Converted to int8: {small_type}")
    print("⚠️  Values wrapped around due to overflow!")
except:
    print("Conversion failed due to overflow")

print("\n" + "-" * 40)
print("SAFE CONVERSION PRACTICES:")
print("-" * 40)

# Check if conversion is safe
data = np.array([100, 150, 200])
print(f"Data: {data} (dtype: {data.dtype})")
print(f"int8 range: {np.iinfo(np.int8).min} to {np.iinfo(np.int8).max}")

if data.min() >= np.iinfo(np.int8).min and data.max() <= np.iinfo(np.int8).max:
    safe_conversion = data.astype(np.int8)
    print(f"✅ Safe conversion to int8: {safe_conversion}")
else:
    print("❌ Unsafe to convert to int8 - values outside range")
    print("Recommendation: Use int16 or larger")
    safe_conversion = data.astype(np.int16)
    print(f"✅ Safe conversion to int16: {safe_conversion}")

print("\n" + "-" * 40)
print("MEMORY OPTIMIZATION WITH astype():")
print("-" * 40)

# Example: Optimizing memory for age data
ages_default = np.array([25, 30, 45, 67, 89, 23, 56, 78, 34, 12])
ages_optimized = ages_default.astype(np.uint8)  # Ages 0-255

print(f"Ages (default int64): {ages_default}")
print(f"Memory: {ages_default.nbytes} bytes")
print(f"\nAges (optimized uint8): {ages_optimized}")
print(f"Memory: {ages_optimized.nbytes} bytes")
print(f"Memory saved: {ages_default.nbytes - ages_optimized.nbytes} bytes ({((ages_default.nbytes - ages_optimized.nbytes) / ages_default.nbytes * 100):.1f}% reduction)")

print("\n" + "=" * 50)
print("astype() SUMMARY")
print("=" * 50)
print("🔄 COMMON CONVERSIONS:")
print("  • array.astype(np.int8)     - Convert to 8-bit integer")
print("  • array.astype(np.float32)  - Convert to 32-bit float")
print("  • array.astype(np.bool_)    - Convert to boolean")
print("  • array.astype('U10')       - Convert to 10-char string")
print("  • array.astype(object)      - Convert to object type")
print("\n⚠️  CONVERSION RULES:")
print("  • Float → Int: Decimals truncated (not rounded)")
print("  • Number → Bool: 0 = False, everything else = True")
print("  • Bool → Number: True = 1, False = 0")
print("  • String → Number: Only if string represents valid number")
print("\n💡 BEST PRACTICES:")
print("  • Check value ranges before converting to smaller types")
print("  • Use astype() for memory optimization")
print("  • Handle ValueError exceptions for invalid conversions")
print("  • Test conversions with sample data first")
print("\n🎯 MEMORY OPTIMIZATION:")
print("  • int64 → int8: 8x memory reduction (if values fit)")
print("  • float64 → float32: 2x memory reduction")
print("  • Large arrays benefit most from optimization")

