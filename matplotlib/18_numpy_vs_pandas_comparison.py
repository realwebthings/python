import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os

print("="*60)
print("NUMPY vs PANDAS - When to Use What?")
print("="*60)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '..', 'pandas', 'data', 'pokemon.csv')

print("\n" + "="*60)
print("METHOD 1: NUMPY (Numerical Operations)")
print("="*60)

# Read CSV and convert to NumPy arrays
names_list = []
data_list = []

with open(csv_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        names_list.append(row['Name'])
        data_list.append([int(row['HP']), int(row['Attack']), int(row['Defense']), int(row['Speed'])])

names_np = np.array(names_list)
data_np = np.array(data_list)  # Shape: (n_pokemon, 4)

print(f"NumPy array shape: {data_np.shape}")
print(f"First 5 rows:\n{data_np[:5]}")

# NumPy operations
hp_col = data_np[:, 0]  # First column (HP)
attack_col = data_np[:, 1]  # Second column (Attack)

# Statistics with NumPy
print(f"\nNumPy Statistics:")
print(f"Mean HP: {np.mean(hp_col):.2f}")
print(f"Median HP: {np.median(hp_col):.2f}")
print(f"Std HP: {np.std(hp_col):.2f}")

# Filtering with NumPy
high_hp_mask = hp_col > 100
high_hp_names = names_np[high_hp_mask]
high_hp_values = hp_col[high_hp_mask]
print(f"\nPokemon with HP > 100: {len(high_hp_names)}")

# Sorting with NumPy
sorted_indices = np.argsort(hp_col)[::-1][:10]  # Top 10
top_10_names_np = names_np[sorted_indices]
top_10_hp_np = hp_col[sorted_indices]

plt.figure(figsize=(12, 6))
plt.bar(top_10_names_np, top_10_hp_np, color='green', edgecolor='black')
plt.xlabel('Pokemon', fontsize=12)
plt.ylabel('HP', fontsize=12)
plt.title('Top 10 Pokemon by HP (NumPy)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
NUMPY APPROACH:
===============
✓ Fast numerical operations
✓ Array-based (all same type)
✓ Great for math/statistics
✓ Memory efficient
✓ Vectorized operations

✗ No column names (use indices)
✗ All data must be same type
✗ No built-in groupby
✗ Manual CSV reading
✗ Harder for mixed data types

Code:
-----
data_np = np.array(data_list)
hp_col = data_np[:, 0]  # Column by index

# Statistics
mean_hp = np.mean(hp_col)

# Filtering
mask = hp_col > 100
filtered = hp_col[mask]

# Sorting
sorted_indices = np.argsort(hp_col)[::-1]
""")

print("\n" + "="*60)
print("METHOD 2: PANDAS (Tabular Data)")
print("="*60)

# Read CSV with pandas
df = pd.read_csv(csv_path)

print(f"Pandas DataFrame shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())

# Pandas operations
print(f"\nPandas Statistics:")
print(f"Mean HP: {df['HP'].mean():.2f}")
print(f"Median HP: {df['HP'].median():.2f}")
print(f"Std HP: {df['HP'].std():.2f}")

# Filtering with Pandas
high_hp_df = df[df['HP'] > 100]
print(f"\nPokemon with HP > 100: {len(high_hp_df)}")

# Sorting with Pandas
top_10_df = df.nlargest(10, 'HP')

plt.figure(figsize=(12, 6))
plt.bar(top_10_df['Name'], top_10_df['HP'], color='coral', edgecolor='black')
plt.xlabel('Pokemon', fontsize=12)
plt.ylabel('HP', fontsize=12)
plt.title('Top 10 Pokemon by HP (Pandas)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
PANDAS APPROACH:
================
✓ Column names (easy access)
✓ Mixed data types (strings + numbers)
✓ Built-in groupby, merge, join
✓ One-line CSV reading
✓ Handles missing data
✓ Time series support
✓ SQL-like operations

✗ Slower than NumPy for pure math
✗ More memory usage
✗ Overkill for simple arrays

Code:
-----
df = pd.read_csv('pokemon.csv')

# Statistics
mean_hp = df['HP'].mean()

# Filtering
filtered = df[df['HP'] > 100]

# Sorting
top_10 = df.nlargest(10, 'HP')

# Grouping
type_avg = df.groupby('Type')['HP'].mean()
""")

print("\n" + "="*60)
print("SIDE-BY-SIDE COMPARISON")
print("="*60)

print("""
TASK 1: Calculate Mean
-----------------------
NUMPY:  np.mean(data[:, 0])
PANDAS: df['HP'].mean()

Winner: TIE (both easy)

TASK 2: Filter Data
--------------------
NUMPY:  mask = data[:, 0] > 100
        filtered = data[mask]
PANDAS: filtered = df[df['HP'] > 100]

Winner: PANDAS (more readable)

TASK 3: Sort by Column
-----------------------
NUMPY:  indices = np.argsort(data[:, 0])[::-1]
        sorted_data = data[indices]
PANDAS: sorted_df = df.sort_values('HP', ascending=False)

Winner: PANDAS (clearer intent)

TASK 4: Group by Category
--------------------------
NUMPY:  # Manual loop required
        unique_types = np.unique(types)
        for t in unique_types:
            mask = types == t
            avg = np.mean(data[mask, 0])

PANDAS: type_avg = df.groupby('Type')['HP'].mean()

Winner: PANDAS (much easier!)

TASK 5: Mathematical Operations
--------------------------------
NUMPY:  result = np.sqrt(data[:, 0]) * 2 + data[:, 1]
PANDAS: result = np.sqrt(df['HP']) * 2 + df['Attack']

Winner: NUMPY (designed for this)

TASK 6: Handle Mixed Data Types
--------------------------------
NUMPY:  # Difficult - needs structured arrays
        data = np.array([('Pikachu', 35, 55)], 
                       dtype=[('name', 'U10'), ('hp', 'i4'), ('atk', 'i4')])

PANDAS: df = pd.DataFrame({'Name': ['Pikachu'], 'HP': [35], 'Attack': [55]})

Winner: PANDAS (natural fit)
""")

print("\n" + "="*60)
print("WHEN TO USE WHAT?")
print("="*60)

print("""
USE NUMPY WHEN:
===============
✓ Pure numerical computations
✓ All data is same type (all numbers)
✓ Need maximum speed for math operations
✓ Working with matrices/arrays
✓ Scientific computing
✓ Image processing
✓ Signal processing
✓ Linear algebra operations

EXAMPLES:
• Matrix multiplication
• Image filters
• Mathematical simulations
• Neural network operations
• Numerical analysis

USE PANDAS WHEN:
================
✓ Working with tabular data (rows & columns)
✓ Mixed data types (strings + numbers)
✓ Need to filter, sort, group data
✓ Reading CSV, Excel, SQL, JSON
✓ Data cleaning (missing values, duplicates)
✓ Time series analysis
✓ Data exploration and analysis
✓ Merging/joining datasets

EXAMPLES:
• CSV/Excel data analysis
• Database-like operations
• Business analytics
• Data preprocessing for ML
• Statistical analysis
• Report generation

USE BOTH TOGETHER:
==================
Pandas is built on top of NumPy!
You can use both in the same project:

# Read with Pandas
df = pd.read_csv('data.csv')

# Convert to NumPy for fast math
data_np = df[['HP', 'Attack']].values
result = np.sqrt(data_np[:, 0]) * data_np[:, 1]

# Back to Pandas for analysis
df['Result'] = result
summary = df.groupby('Type')['Result'].mean()
""")

print("\n" + "="*60)
print("REAL-WORLD DECISION TREE")
print("="*60)

print("""
START: What are you working with?
│
├─ Pure numbers (matrices, arrays)
│  └─> USE NUMPY
│      Examples: Image processing, linear algebra, simulations
│
├─ Tabular data (CSV, Excel, database)
│  │
│  ├─ Simple math only (no grouping/filtering)
│  │  └─> NUMPY is fine
│  │
│  └─ Need to filter/sort/group/analyze
│     └─> USE PANDAS
│         Examples: Data analysis, business reports, ML preprocessing
│
└─ Mixed data types (strings + numbers)
   └─> USE PANDAS
       Examples: Customer data, product catalogs, survey results

MATPLOTLIB PLOTTING:
====================
Both work equally well for plotting!

NUMPY:
plt.plot(x_array, y_array)
plt.scatter(data[:, 0], data[:, 1])

PANDAS:
plt.plot(df['x'], df['y'])
plt.scatter(df['HP'], df['Attack'])

# Or use Pandas built-in plotting
df.plot(x='HP', y='Attack', kind='scatter')

FINAL ANSWER TO YOUR QUESTION:
===============================
YES, NumPy can do filtering, sorting, and math operations.

BUT:
• NumPy is better for NUMERICAL operations
• Pandas is better for TABULAR data operations

For CSV data with mixed types and column names:
→ PANDAS is the right tool

For pure numerical arrays and fast math:
→ NUMPY is the right tool

For plotting:
→ BOTH work fine with matplotlib!

RECOMMENDATION:
===============
Learn both! They complement each other:
• NumPy: Foundation for numerical computing
• Pandas: Built on NumPy, adds data analysis features

Most data science projects use BOTH:
1. Read data with Pandas
2. Do heavy math with NumPy
3. Analyze results with Pandas
4. Plot with Matplotlib
""")

# Practical example using both
print("\n" + "="*60)
print("PRACTICAL EXAMPLE: Using Both Together")
print("="*60)

# Read with Pandas
df = pd.read_csv(csv_path)

# Convert to NumPy for fast computation
stats_np = df[['HP', 'Attack', 'Defense', 'Speed']].values

# Fast NumPy computation
total_stats = np.sum(stats_np, axis=1)
normalized_stats = stats_np / np.max(stats_np, axis=0)

# Back to Pandas for analysis
df['Total'] = total_stats
df['Normalized_HP'] = normalized_stats[:, 0]

# Pandas grouping
type_summary = df.groupby('Type')['Total'].agg(['mean', 'max', 'min'])

print("Combined NumPy + Pandas:")
print(type_summary)

print("""
BEST OF BOTH WORLDS:
====================
df = pd.read_csv('data.csv')           # Pandas: Easy reading
data_np = df[['HP', 'Attack']].values  # Convert to NumPy
result = np.sqrt(data_np) * 2          # NumPy: Fast math
df['Result'] = result[:, 0]            # Back to Pandas
summary = df.groupby('Type').mean()    # Pandas: Easy grouping

This is the REAL-WORLD approach!
""")
