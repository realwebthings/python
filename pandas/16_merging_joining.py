import pandas as pd

print("=" * 60)
print("MERGING AND JOINING DATAFRAMES")
print("=" * 60)

print("\n" + "=" * 50)
print("1. CONCAT - VERTICAL (STACK ROWS)")
print("=" * 50)
df1 = pd.DataFrame({'Name': ['Pikachu', 'Charizard'], 'HP': [35, 78]})
df2 = pd.DataFrame({'Name': ['Blastoise', 'Venusaur'], 'HP': [79, 80]})
df_concat = pd.concat([df1, df2])
print(df_concat)

print("\n" + "=" * 50)
print("2. CONCAT - RESET INDEX")
print("=" * 50)
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)

print("\n" + "=" * 50)
print("3. CONCAT - HORIZONTAL (SIDE BY SIDE)")
print("=" * 50)
df3 = pd.DataFrame({'Attack': [55, 84]})
df4 = pd.DataFrame({'Defense': [40, 78]})
df_concat = pd.concat([df3, df4], axis=1)
print(df_concat)

print("\n" + "=" * 50)
print("4. MERGE - INNER JOIN (COMMON ROWS)")
print("=" * 50)
df_pokemon = pd.DataFrame({
    'Name': ['Pikachu', 'Charizard', 'Blastoise'],
    'Type': ['Electric', 'Fire', 'Water']
})
df_stats = pd.DataFrame({
    'Name': ['Pikachu', 'Charizard', 'Mewtwo'],
    'HP': [35, 78, 106]
})
df_merged = pd.merge(df_pokemon, df_stats, on='Name', how='inner')
print(df_merged)
print("Note: Only Pikachu and Charizard appear (common in both)")

print("\n" + "=" * 50)
print("5. MERGE - LEFT JOIN (KEEP ALL FROM LEFT)")
print("=" * 50)
df_merged = pd.merge(df_pokemon, df_stats, on='Name', how='left')
print(df_merged)
print("Note: Blastoise kept with NaN HP")

print("\n" + "=" * 50)
print("6. MERGE - RIGHT JOIN (KEEP ALL FROM RIGHT)")
print("=" * 50)
df_merged = pd.merge(df_pokemon, df_stats, on='Name', how='right')
print(df_merged)
print("Note: Mewtwo kept with NaN Type")

print("\n" + "=" * 50)
print("7. MERGE - OUTER JOIN (KEEP ALL)")
print("=" * 50)
df_merged = pd.merge(df_pokemon, df_stats, on='Name', how='outer')
print(df_merged)
print("Note: All rows kept, NaN where no match")

print("\n" + "=" * 50)
print("8. MERGE ON MULTIPLE COLUMNS")
print("=" * 50)
df_a = pd.DataFrame({
    'Name': ['Pikachu', 'Charizard'],
    'Type': ['Electric', 'Fire'],
    'HP': [35, 78]
})
df_b = pd.DataFrame({
    'Name': ['Pikachu', 'Charizard'],
    'Type': ['Electric', 'Fire'],
    'Attack': [55, 84]
})
df_merged = pd.merge(df_a, df_b, on=['Name', 'Type'])
print(df_merged)

print("\n" + "=" * 50)
print("9. MERGE WITH DIFFERENT COLUMN NAMES")
print("=" * 50)
df_x = pd.DataFrame({'Pokemon': ['Pikachu', 'Charizard'], 'HP': [35, 78]})
df_y = pd.DataFrame({'Name': ['Pikachu', 'Charizard'], 'Attack': [55, 84]})
df_merged = pd.merge(df_x, df_y, left_on='Pokemon', right_on='Name')
print(df_merged)

print("\n" + "=" * 50)
print("10. JOIN (INDEX-BASED)")
print("=" * 50)
df_left = pd.DataFrame({'HP': [35, 78]}, index=['Pikachu', 'Charizard'])
df_right = pd.DataFrame({'Attack': [55, 84]}, index=['Pikachu', 'Charizard'])
df_joined = df_left.join(df_right)
print(df_joined)

print("\n" + "=" * 50)
print("SUMMARY - MERGE TYPES")
print("=" * 50)
print("""
CONCAT:
• pd.concat([df1, df2])           → Stack vertically (rows)
• pd.concat([df1, df2], axis=1)   → Stack horizontally (columns)

MERGE (SQL-like joins):
• how='inner'  → Only matching rows (intersection)
• how='left'   → All from left, matching from right
• how='right'  → All from right, matching from left
• how='outer'  → All rows from both (union)

JOIN:
• df1.join(df2)  → Merge on index (faster for index-based)
""")
