import pandas as pd
import os 

# Data Cleaning =  the process of fixing/removing incorrect, incomplete or irrelevant data.
#                  ~75% of work done with pandas is data cleaning
#                  It is a crucial step in data preprocessing and ensures that the data is accurate and reliable for analysis.

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path, index_col='Name')
print(df.head(5))


print("\n" + "=" * 50)
print(f"{'1. ADD NEW COLUMN':^50}")
print("=" * 50)

# Method 1: Add column with single value
df['Level'] = 50
print("\nAdded 'Level' column with value 50:")
print(df.head(3))

# Method 2: Add column with calculation
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
print("\nAdded 'Total' column (sum of stats):")
print(df[['HP', 'Attack', 'Defense', 'Speed', 'Total']].head(3))

# Method 3: Add column with list
df['Generation'] = 1
print("\nAdded 'Generation' column:")
print(df.head(3))

print("\n" + "=" * 50)
print(f"{'2. ADD ROWS WITH NULL VALUES':^50}")
print("=" * 50)

# Add rows with missing values
new_rows = pd.DataFrame({
    'Type': [None, 'Fire', None],
    'HP': [50, None, 70],
    'Attack': [60, 80, None],
    'Defense': [55, 75, 65],
    'Speed': [None, 90, 85],
    'Level': [50, 50, 50],
    'Total': [None, None, None],
    'Generation': [1, 1, 1]
}, index=['MissingMon1', 'MissingMon2', 'MissingMon3'])

df = pd.concat([df, new_rows])
print("\nDataFrame with rows containing null values:")
print(df.tail(5))

print("\nChecking for null values:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print(f"{'3. DROP ROWS WITH MISSING VALUES':^50}")
print("=" * 50)

print("\nBefore dropping (last 5 rows):")
print(df.tail(5))

print(f"\nShape before: {df.shape}")
df_cleaned = df.dropna()
print(f"Shape after dropna(): {df_cleaned.shape}")
print("\nAfter dropping all rows with ANY null values:")
print(df_cleaned.tail(5))

# Drop rows with null in specific column
df_cleaned_type = df.dropna(subset=['Type'])

print(f"\nShape after dropna(subset=['Type']): {df_cleaned_type.shape}")
print("Dropped only rows with null in 'Type' column")
print(df_cleaned_type, "\n")


print("\n" + "=" * 50)
print(f"{'4. FILL MISSING VALUES (fillna)':^50}")
print("=" * 50)

print("\nNull values before filling:")
print(df.isnull().sum())

# Fill with specific value
df_filled = df.fillna(0)
print("\nAfter fillna(0):")
print(df_filled.tail(3))

# Fill with mean
df['HP'] = df['HP'].fillna(df['HP'].mean())
print(f"\nFilled HP nulls with mean: {df['HP'].mean():.2f}")

# Fill with forward fill (use previous value)
df['Type'] = df['Type'].ffill()
print("\nFilled Type nulls with forward fill (ffill)")
print(df.tail(3))

print("\n" + "=" * 50)
print(f"{'5. FIX INCONSISTENT VALUES (replace)':^50}")
print("=" * 50)

# Add inconsistent data
df.loc['Pikachu', 'Type'] = 'ELECTRIC'
df.loc['Charizard', 'Type'] = 'fire'
df.loc['Blastoise', 'Type'] = 'WATER'

print("\nInconsistent Type values:")
print(df[['Type']].head(5))

# Replace inconsistent values
df['Type'] = df['Type'].replace({'ELECTRIC': 'Electric', 'fire': 'Fire', 'WATER': 'Water'})
print("\nAfter replace():")
print(df[['Type']].head(5))

print("\n" + "=" * 50)
print(f"{'6. STANDARDIZE TEXT (lowercase)':^50}")
print("=" * 50)

print("\nBefore standardization:")
print(df['Type'].head(5))

df['Type'] = df['Type'].str.lower()
print("\nAfter str.lower():")
print(df['Type'].head(5))

# Also available: str.upper(), str.title(), str.capitalize()
df['Type'] = df['Type'].str.capitalize()
print("\nAfter str.capitalize():")
print(df['Type'].head(5))

print("\n" + "=" * 50)
print(f"{'7. FIX DATA TYPES':^50}")
print("=" * 50)

print("\nData types before:")
print(df.dtypes)

# Convert to specific type
df['Level'] = df['Level'].astype(int)
df['HP'] = df['HP'].astype(int)
print("\nData types after conversion:")
print(df.dtypes)

print("\n" + "=" * 50)
print(f"{'8. REMOVE DUPLICATE VALUES':^50}")
print("=" * 50)

# Add duplicate rows
dup_row = df.loc[['Pikachu']].copy()
dup_row.index = ['Pikachu_Duplicate']
df = pd.concat([df, dup_row])

print(f"\nShape before removing duplicates: {df.shape}")
print("\nDuplicate rows:")
print(df[df.duplicated(keep=False)].sort_index())

# Remove duplicates
df_no_dups = df.drop_duplicates()
print(f"\nShape after drop_duplicates(): {df_no_dups.shape}")

# Remove duplicates based on specific columns
df_no_dups_subset = df.drop_duplicates(subset=['Type', 'HP', 'Attack'])
print(f"Shape after drop_duplicates(subset=['Type', 'HP', 'Attack']): {df_no_dups_subset.shape}")

print("\n" + "=" * 50)
print(f"{'9. DROP COLUMNS':^50}")
print("=" * 50)

print("\nColumns before:")
print(df.columns.tolist())

df_no_level = df.drop('Level', axis=1)
print("\nAfter dropping 'Level' column:")
print(df_no_level.columns.tolist())

df_no_multiple = df.drop(['Level', 'Generation'], axis=1)
print("\nAfter dropping 'Level' and 'Generation':")
print(df_no_multiple.columns.tolist())

print("\n" + "=" * 50)
print("DATA CLEANING SUMMARY")
print("=" * 50)
print("""
KEY DATA CLEANING OPERATIONS:
1. fillna() - Fill missing values
2. dropna() - Remove rows/columns with missing values
3. replace() - Fix inconsistent values
4. str.lower()/str.upper() - Standardize text
5. astype() - Fix data types
6. drop_duplicates() - Remove duplicate rows
7. drop() - Remove columns
""")