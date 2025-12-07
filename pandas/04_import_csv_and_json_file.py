import pandas as pd
import os

print("=" * 60)
print("PANDAS - READING CSV AND JSON FILES")
print("=" * 60)

print("\n" + "=" * 50)
print("1. READ CSV FILE")
print("=" * 50)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data', 'pokemon.csv')
json_path = os.path.join(script_dir, 'data', 'pokemon.json')

df_csv = pd.read_csv(csv_path)
# df_json = pd.read_json(json_path)
# print(df_csv.to_string()) # it will print all data without truncating in terminal
print(df_csv.head(5)) # print first 5 rows
print("\n" + "=" * 50)
print(df_csv.tail(5)) # print last 5 rows
print("\n" + "=" * 50)
print(df_csv.sample(5)) # print random 5 rows
print("\n" + "=" * 50)
print(df_csv.info()) # print info about the dataframe
print(f"\nShape: {df_csv.shape}")
print(f"Columns: {list(df_csv.columns)}")

print("\n" + "=" * 50)
print("2. INDEXING AND SELECTING DATA")
print("=" * 50)

# Set Name as index
df_csv = pd.read_csv(csv_path, index_col='Name')
print("DataFrame with Name as index:")
print(df_csv.head(5))

print("\n" + "=" * 50)
print("3. SELECTING ROWS (using .loc)")
print("=" * 50)

print("\nSingle Row:")
print(df_csv.loc['Pikachu'])

print("\nMultiple Rows:")
print(df_csv.loc[['Pikachu', 'Charizard']])

print("\n" + "=" * 50)
print("4. SELECTING COLUMNS")
print("=" * 50)

print("\nSingle Column:")
print(df_csv['HP'])

print("\nMultiple Columns:")
print(df_csv[['HP', 'Attack']])

print("\n" + "=" * 50)
print("5. SELECTING ROWS AND COLUMNS")
print("=" * 50)

print("\nSpecific rows and columns:")
print(df_csv.loc[['Pikachu', 'Charizard'], ['HP', 'Attack']])

print("\nSingle value:")
print(df_csv.loc['Pikachu', 'HP'])

print("\n" + "=" * 50)
print("6. SELECTING ROWS USING INTEGER INDEX (.iloc)")
print("=" * 50)

print("\nFirst row (index 0):")
print(df_csv.iloc[0])

print("\nFirst 3 rows:")
print(df_csv.iloc[0:3])

print("\nSpecific rows by position:")
print(df_csv.iloc[[0, 2, 4]])

print("\nRows and columns by position:")
print(df_csv.iloc[0:3, 0:2])

print("\nSingle value by position:")
print(df_csv.iloc[0, 1])

print("\nValues with stepped index")
print(df_csv.iloc[0::2])

print("\n" + "=" * 50)
print("7. ROW SELECTION BY USER INPUT")
print("=" * 50)

pokemon = ""
try:
    pokemon = input("Enter a Pokemon name: ")
    print(df_csv.loc[pokemon])
    print(df_csv.loc[pokemon, 'HP'])
    print(df_csv.loc[[pokemon], ['HP', 'Attack']])
except EOFError as e:
    print(f"{pokemon} Pokemon not found", e)

print("\n" + "=" * 50)
print("8. SUMMARY - ROW vs COLUMN SELECTION")
print("=" * 50)

print("""
ROW SELECTION (using .loc with labels):
• df.loc['Pikachu']                    → Single row
• df.loc[['Pikachu', 'Charizard']]    → Multiple rows

ROW SELECTION (using .iloc with positions):
• df.iloc[0]                           → First row
• df.iloc[0:3]                         → First 3 rows
• df.iloc[[0, 2, 4]]                   → Rows at positions 0, 2, 4

COLUMN SELECTION:
• df['HP']                             → Single column
• df[['HP', 'Attack']]                 → Multiple columns

ROW + COLUMN SELECTION:
• df.loc['Pikachu', 'HP']              → Single value (by label)
• df.iloc[0, 1]                        → Single value (by position)
• df.loc[['Pikachu'], ['HP', 'Attack']] → Specific rows & columns

KEY DIFFERENCES:
.loc[row_labels, column_labels]  → Uses LABELS (names)
.iloc[row_positions, col_positions] → Uses INTEGER POSITIONS (0, 1, 2...)
""")




