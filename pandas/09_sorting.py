import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path)

print("=" * 60)
print("SORTING OPERATIONS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. SORT BY SINGLE COLUMN (ASCENDING)")
print("=" * 50)
df_sorted = df.sort_values('HP')
print(df_sorted[['Name', 'HP']].head(5))

print("\n" + "=" * 50)
print("2. SORT BY SINGLE COLUMN (DESCENDING)")
print("=" * 50)
df_sorted = df.sort_values('HP', ascending=False)
print(df_sorted[['Name', 'HP']].head(5))

print("\n" + "=" * 50)
print("3. SORT BY MULTIPLE COLUMNS")
print("=" * 50)
df_sorted = df.sort_values(['Type', 'HP'], ascending=[True, False])
print(df_sorted[['Name', 'Type', 'HP']].head(10))

print("\n" + "=" * 50)
print("4. SORT BY INDEX")
print("=" * 50)
df_indexed = df.set_index('Name')
df_sorted = df_indexed.sort_index()
print(df_sorted.head(5))

print("\n" + "=" * 50)
print("5. SORT BY INDEX (DESCENDING)")
print("=" * 50)
df_sorted = df_indexed.sort_index(ascending=False)
print(df_sorted.head(5))

print("\n" + "=" * 50)
print("6. SORT INPLACE (MODIFY ORIGINAL)")
print("=" * 50)
df_copy = df.copy()
print("Before:", df_copy['HP'].head(3).tolist())
df_copy.sort_values('HP', inplace=True)
print("After:", df_copy['HP'].head(3).tolist())

print("\n" + "=" * 50)
print("7. SORT WITH NULL VALUES")
print("=" * 50)
df_with_null = df.copy()
df_with_null.loc[0, 'HP'] = None
df_with_null.loc[1, 'HP'] = None
df_sorted = df_with_null.sort_values('HP', na_position='first')
print(df_sorted[['Name', 'HP']].head(5))
