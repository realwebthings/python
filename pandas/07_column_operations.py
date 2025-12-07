import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path)

print("=" * 60)
print("COLUMN OPERATIONS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. SELECT SINGLE COLUMN")
print("=" * 50)
print(df['Name'].head(3))

print("\n" + "=" * 50)
print("2. SELECT MULTIPLE COLUMNS")
print("=" * 50)
print(df[['Name', 'Type', 'HP']].head(3))

print("\n" + "=" * 50)
print("3. REORDER COLUMNS")
print("=" * 50)
df_reordered = df[['Name', 'HP', 'Attack', 'Defense', 'Speed', 'Type']]
print(df_reordered.head(3))

print("\n" + "=" * 50)
print("4. RENAME COLUMNS")
print("=" * 50)
df_renamed = df.rename(columns={'HP': 'Health', 'Attack': 'Atk', 'Defense': 'Def'})
print(df_renamed.head(3))

print("\n" + "=" * 50)
print("5. RENAME ALL COLUMNS (LOWERCASE)")
print("=" * 50)
df_lower = df.copy()
df_lower.columns = df_lower.columns.str.lower()
print(df_lower.head(3))

print("\n" + "=" * 50)
print("6. ADD NEW COLUMN (CALCULATION)")
print("=" * 50)
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
print(df[['Name', 'HP', 'Attack', 'Defense', 'Speed', 'Total']].head(3))

print("\n" + "=" * 50)
print("7. ADD NEW COLUMN (CONDITIONAL)")
print("=" * 50)
df['Power_Level'] = df['Total'].apply(lambda x: 'High' if x > 250 else 'Low')
print(df[['Name', 'Total', 'Power_Level']].head(5))

print("\n" + "=" * 50)
print("8. DROP COLUMNS")
print("=" * 50)
df_dropped = df.drop(['Total', 'Power_Level'], axis=1)
print(df_dropped.head(3))

print("\n" + "=" * 50)
print("9. INSERT COLUMN AT SPECIFIC POSITION")
print("=" * 50)
df_insert = df.copy()
df_insert.insert(1, 'ID', range(1, len(df_insert) + 1))
print(df_insert.head(3))

print("\n" + "=" * 50)
print("10. GET COLUMN NAMES")
print("=" * 50)
print("Columns:", df.columns.tolist())
print("Number of columns:", len(df.columns))
