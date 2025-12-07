import pandas as pd

print("=" * 60)
print("WHY ARE NAME AND TYPE 'object' DTYPE?")
print("=" * 60)

# Create sample DataFrame
df = pd.DataFrame({
    'Name': ['Pikachu', 'Charizard', 'Blastoise'],
    'Type': ['Electric', 'Fire', 'Water'],
    'HP': [35, 78, 79],
    'Attack': [55, 84, 83]
})

print("\n" + "=" * 50)
print("DATAFRAME INFO")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("CHECKING DATA TYPES")
print("=" * 50)
print(df.dtypes)

print("\n" + "=" * 50)
print("EXPLANATION: dtypes: int64(4), object(2)")
print("=" * 50)

print("""
The notation 'object(2)' means:
→ 2 columns have the 'object' data type
→ These are: Name and Type

The notation 'int64(4)' means:
→ 4 columns have the 'int64' data type
→ These are: HP, Attack, Defense, Speed

The number in parentheses = COUNT of columns with that type
""")

print("\n" + "=" * 50)
print("YES! 'object' = STRING/TEXT DATA")
print("=" * 50)

print("""
✅ SIMPLE ANSWER:
Yes! 'object' dtype means STRING/TEXT data in pandas.

Name column: 'Pikachu', 'Charizard', 'Blastoise' → STRINGS
Type column: 'Electric', 'Fire', 'Water' → STRINGS

So when you see:
  dtypes: object(2)
  
It means: 2 columns contain STRING/TEXT data
""")

print("\n" + "=" * 50)
print("WHY CALLED 'object' INSTEAD OF 'string'?")
print("=" * 50)

print("""
Pandas calls it 'object' (not 'string') because:

1. HISTORICAL REASON
   • Pandas uses Python's str objects
   • In Python, strings are objects
   • So pandas calls them 'object' dtype

2. FLEXIBILITY
   • 'object' can hold ANY Python object
   • Usually strings, but could be mixed types
   • More flexible than pure string type

3. MODERN PANDAS
   • Pandas now has 'string' dtype (newer)
   • But 'object' is still default for text
   • Both work for string data

4. COMPARISON WITH NUMPY
   • NumPy has fixed-length strings (e.g., 'U10' = max 10 chars)
   • Pandas uses flexible Python strings (any length)
   • NumPy: 'Mew' and 'Charizard' both take 10 chars space
   • Pandas: 'Mew' takes 3 chars, 'Charizard' takes 9 chars
   • Pandas 'object' is more flexible but uses more memory

BOTTOM LINE:
object dtype = strings/text (99% of the time)
""")

print("\n" + "=" * 50)
print("VISUAL BREAKDOWN")
print("=" * 50)

print("\nColumn by column:")
for col in df.columns:
    dtype_str = str(df[col].dtype)
    value = df[col].iloc[0]
    value_type = type(value).__name__
    print(f"{col:10} → dtype: {dtype_str:10} → Python type: {value_type:10} → Example: {value}")

print("\nNotice:")
print("  'object' dtype → Python type is 'str' (string)")
print("  'int64' dtype → Python type is 'int' or 'numpy.int64'")

print("\n" + "=" * 50)
print("COUNTING DTYPES")
print("=" * 50)

dtype_counts = df.dtypes.value_counts()
print(dtype_counts)
print(f"\nobject: {dtype_counts.get('object', 0)} columns (Name, Type)")
print(f"int64:  {dtype_counts.get('int64', 0)} columns (HP, Attack)")

print("\n" + "=" * 50)
print("MEMORY IMPLICATIONS")
print("=" * 50)

print("\nMemory usage by column:")
print(df.memory_usage(deep=True))

print("""
Notice:
• 'object' columns (Name, Type) use MORE memory
• 'int64' columns use fixed 8 bytes per value
• Text is variable length, so uses more space
""")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print("""
dtypes: int64(4), object(2) means:

✓ object(2) → 2 columns contain STRINGS/TEXT
  - Name column: 'Pikachu', 'Charizard', 'Blastoise'
  - Type column: 'Electric', 'Fire', 'Water'
  - These are Python str objects
  
✓ int64(4) → 4 columns contain INTEGERS/NUMBERS
  - HP, Attack, Defense, Speed
  - These are numeric values

KEY POINT:
'object' dtype = STRING/TEXT data (in most cases)
The (2) means there are 2 columns with strings!
""")

print("\n" + "=" * 50)
print("PROOF: CHECKING ACTUAL PYTHON TYPES")
print("=" * 50)

print(f"\nName column first value: '{df['Name'].iloc[0]}'")
print(f"Python type: {type(df['Name'].iloc[0])}")
print(f"Is it a string? {isinstance(df['Name'].iloc[0], str)}")

print(f"\nHP column first value: {df['HP'].iloc[0]}")
print(f"Python type: {type(df['HP'].iloc[0])}")
print(f"Is it a string? {isinstance(df['HP'].iloc[0], str)}")

print("\n✅ Confirmed: 'object' dtype contains str (string) values!")
