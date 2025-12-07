import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path)

print("=" * 60)
print("INDEX OPERATIONS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. DEFAULT INDEX (RangeIndex)")
print("=" * 50)
print(df.head(3))
print("Index:", df.index)

print("\n" + "=" * 50)
print("2. SET COLUMN AS INDEX")
print("=" * 50)
df_indexed = df.set_index('Name')
print(df_indexed.head(3))

print("\n" + "=" * 50)
print("3. RESET INDEX (BACK TO DEFAULT)")
print("=" * 50)
df_reset = df_indexed.reset_index()
print(df_reset.head(3))

print("\n" + "=" * 50)
print("4. RESET INDEX (DROP OLD INDEX)")
print("=" * 50)
df_reset = df_indexed.reset_index(drop=True)
print(df_reset.head(3))

print("\n" + "=" * 50)
print("5. SET MULTIPLE COLUMNS AS INDEX")
print("=" * 50)
df_multi = df.set_index(['Type', 'Name'])
print(df_multi.head(5))

print("\n" + "=" * 50)
print("6. ACCESS WITH MULTI-INDEX")
print("=" * 50)
print(df_multi.loc[('Electric', 'Pikachu')])

print("\n" + "=" * 50)
print("7. RENAME INDEX")
print("=" * 50)
df_indexed = df.set_index('Name')
df_indexed.index.name = 'Pokemon'
print(df_indexed.head(3))

print("\n" + "=" * 50)
print("8. SET CUSTOM INDEX")
print("=" * 50)
df_custom = df.copy()
df_custom.index = ['P' + str(i) for i in range(1, len(df_custom) + 1)]
print(df_custom.head(3))

print("\n" + "=" * 50)
print("9. SORT BY INDEX")
print("=" * 50)
df_indexed = df.set_index('Name')
df_sorted = df_indexed.sort_index()
print(df_sorted.head(5))

print("\n" + "=" * 50)
print("10. CHECK IF INDEX IS UNIQUE")
print("=" * 50)
print("Is index unique?", df_indexed.index.is_unique)
