import matplotlib.pyplot as plt
import numpy as np
import csv
import os

print("="*60)
print("READING CSV AND PLOTTING - WITH vs WITHOUT PANDAS")
print("="*60)

# Get the path to pokemon.csv
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '..', 'pandas', 'data', 'pokemon.csv')

print("\n" + "="*60)
print("METHOD 1: WITHOUT PANDAS (Using Python's csv module)")
print("="*60)

# Read CSV without pandas
names = []
hp_values = []
attack_values = []
types = []

with open(csv_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        names.append(row['Name'])
        hp_values.append(int(row['HP']))
        attack_values.append(int(row['Attack']))
        types.append(row['Type'])

print(f"Read {len(names)} Pokemon without pandas")
print(f"First 5 names: {names[:5]}")
print(f"First 5 HP values: {hp_values[:5]}")

# Plot 1: Scatter plot (HP vs Attack)
plt.figure(figsize=(10, 6))
plt.scatter(hp_values, attack_values, s=100, alpha=0.6, c='blue', edgecolors='black')
plt.xlabel('HP', fontsize=12)
plt.ylabel('Attack', fontsize=12)
plt.title('Pokemon: HP vs Attack (Without Pandas)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot 2: Bar chart (Top 10 by HP)
top_10_indices = sorted(range(len(hp_values)), key=lambda i: hp_values[i], reverse=True)[:10]
top_10_names = [names[i] for i in top_10_indices]
top_10_hp = [hp_values[i] for i in top_10_indices]

plt.figure(figsize=(12, 6))
plt.bar(top_10_names, top_10_hp, color='steelblue', edgecolor='black')
plt.xlabel('Pokemon', fontsize=12)
plt.ylabel('HP', fontsize=12)
plt.title('Top 10 Pokemon by HP (Without Pandas)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
WITHOUT PANDAS:
===============
✓ Uses Python's built-in csv module
✓ Manual data extraction with loops
✓ Store data in lists
✓ More code required
✓ Manual filtering/sorting

Code:
-----
import csv

names = []
hp_values = []

with open('pokemon.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        names.append(row['Name'])
        hp_values.append(int(row['HP']))

plt.scatter(hp_values, attack_values)
""")

print("\n" + "="*60)
print("METHOD 2: WITH PANDAS (Recommended)")
print("="*60)

import pandas as pd

# Read CSV with pandas
df = pd.read_csv(csv_path)

print(f"Read {len(df)} Pokemon with pandas")
print(f"\nFirst 5 rows:")
print(df.head())

# Plot 1: Scatter plot (HP vs Attack)
plt.figure(figsize=(10, 6))
plt.scatter(df['HP'], df['Attack'], s=100, alpha=0.6, c='red', edgecolors='black')
plt.xlabel('HP', fontsize=12)
plt.ylabel('Attack', fontsize=12)
plt.title('Pokemon: HP vs Attack (With Pandas)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot 2: Bar chart (Top 10 by HP) - Much easier!
top_10_df = df.nlargest(10, 'HP')

plt.figure(figsize=(12, 6))
plt.bar(top_10_df['Name'], top_10_df['HP'], color='coral', edgecolor='black')
plt.xlabel('Pokemon', fontsize=12)
plt.ylabel('HP', fontsize=12)
plt.title('Top 10 Pokemon by HP (With Pandas)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# Plot 3: Grouped bar chart by Type (Easy with pandas!)
type_stats = df.groupby('Type')[['HP', 'Attack']].mean()

fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(type_stats))
width = 0.35

ax.bar(x - width/2, type_stats['HP'], width, label='HP', color='skyblue')
ax.bar(x + width/2, type_stats['Attack'], width, label='Attack', color='lightcoral')

ax.set_xlabel('Type', fontsize=12)
ax.set_ylabel('Average Value', fontsize=12)
ax.set_title('Average HP and Attack by Pokemon Type (With Pandas)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(type_stats.index, rotation=45, ha='right')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
WITH PANDAS:
============
✓ One line to read CSV: pd.read_csv()
✓ Data in DataFrame (table structure)
✓ Easy filtering, sorting, grouping
✓ Less code, more readable
✓ Built-in data analysis functions

Code:
-----
import pandas as pd

df = pd.read_csv('pokemon.csv')

# Direct column access
plt.scatter(df['HP'], df['Attack'])

# Easy sorting
top_10 = df.nlargest(10, 'HP')
plt.bar(top_10['Name'], top_10['HP'])

# Easy grouping
type_avg = df.groupby('Type')['HP'].mean()
""")

print("\n" + "="*60)
print("COMPARISON: WITH vs WITHOUT PANDAS")
print("="*60)

print("""
┌─────────────────────────────────────────────────────────────┐
│                    WITHOUT PANDAS                           │
├─────────────────────────────────────────────────────────────┤
│ ✓ No external dependencies (built-in csv module)           │
│ ✓ Good for simple CSV reading                              │
│ ✓ Lightweight                                               │
│                                                             │
│ ✗ More code required                                        │
│ ✗ Manual data manipulation                                  │
│ ✗ Harder to filter/sort/group                              │
│ ✗ No built-in data analysis                                │
│ ✗ Separate lists for each column                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     WITH PANDAS                             │
├─────────────────────────────────────────────────────────────┤
│ ✓ One line to read CSV                                      │
│ ✓ Easy data manipulation                                    │
│ ✓ Built-in filtering, sorting, grouping                    │
│ ✓ Data analysis functions (mean, median, etc.)             │
│ ✓ Clean, readable code                                      │
│ ✓ Handles missing data automatically                        │
│ ✓ Can read Excel, JSON, SQL, etc.                          │
│                                                             │
│ ✗ Requires pandas installation                              │
│ ✗ Slightly more memory usage                                │
└─────────────────────────────────────────────────────────────┘

WHEN TO USE PANDAS:
===================
✓ Working with tabular data (CSV, Excel, SQL)
✓ Need to filter, sort, or group data
✓ Data analysis and statistics
✓ Data cleaning (missing values, duplicates)
✓ Complex data transformations
✓ Multiple columns/operations
✓ Time series data
✓ Merging/joining datasets

WHEN YOU DON'T NEED PANDAS:
============================
✓ Very simple CSV reading (few columns)
✓ No data manipulation needed
✓ Minimal dependencies required
✓ Just plotting raw data
✓ Small scripts

CODE COMPARISON:
================

TASK: Get top 10 Pokemon by HP

WITHOUT PANDAS (10+ lines):
---------------------------
with open('pokemon.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    names = []
    hp_values = []
    for row in csv_reader:
        names.append(row['Name'])
        hp_values.append(int(row['HP']))

# Sort manually
indices = sorted(range(len(hp_values)), 
                key=lambda i: hp_values[i], reverse=True)[:10]
top_names = [names[i] for i in indices]
top_hp = [hp_values[i] for i in indices]

WITH PANDAS (2 lines):
----------------------
df = pd.read_csv('pokemon.csv')
top_10 = df.nlargest(10, 'HP')

RECOMMENDATION:
===============
For data analysis and plotting: USE PANDAS
For simple one-time CSV read: Either works

Pandas makes your life MUCH easier for anything beyond
basic CSV reading!
""")

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

print("""
EXAMPLE 1: Filter data
----------------------
WITHOUT PANDAS:
fire_pokemon = []
for i, ptype in enumerate(types):
    if ptype == 'Fire':
        fire_pokemon.append(names[i])

WITH PANDAS:
fire_pokemon = df[df['Type'] == 'Fire']

EXAMPLE 2: Calculate average
-----------------------------
WITHOUT PANDAS:
total_hp = sum(hp_values)
avg_hp = total_hp / len(hp_values)

WITH PANDAS:
avg_hp = df['HP'].mean()

EXAMPLE 3: Group by category
-----------------------------
WITHOUT PANDAS:
type_hp = {}
for i, ptype in enumerate(types):
    if ptype not in type_hp:
        type_hp[ptype] = []
    type_hp[ptype].append(hp_values[i])

type_avg = {t: sum(vals)/len(vals) for t, vals in type_hp.items()}

WITH PANDAS:
type_avg = df.groupby('Type')['HP'].mean()

EXAMPLE 4: Handle missing data
-------------------------------
WITHOUT PANDAS:
clean_hp = [hp for hp in hp_values if hp is not None]

WITH PANDAS:
df = df.dropna(subset=['HP'])
# or
df['HP'].fillna(df['HP'].mean())

CONCLUSION:
===========
Pandas is NOT required for simple plotting, but it makes
data manipulation SO MUCH EASIER that it's worth using
for anything beyond basic CSV reading.

For matplotlib plotting specifically:
• You can plot without pandas (using lists)
• Pandas makes data preparation easier
• Both produce the same plots
• Pandas shines in data manipulation, not plotting itself
""")
