import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path)

print("=" * 60)
print("APPLY, MAP, LAMBDA FUNCTIONS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. LAMBDA FUNCTION (SIMPLE)")
print("=" * 50)
df['HP_Doubled'] = df['HP'].apply(lambda x: x * 2)
print(df[['Name', 'HP', 'HP_Doubled']].head(5))

print("\n" + "=" * 50)
print("2. APPLY WITH CUSTOM FUNCTION")
print("=" * 50)
def categorize_hp(hp):
    if hp < 50:
        return 'Low'
    elif hp < 80:
        return 'Medium'
    else:
        return 'High'

df['HP_Category'] = df['HP'].apply(categorize_hp)
print(df[['Name', 'HP', 'HP_Category']].head(10))

print("\n" + "=" * 50)
print("3. APPLY TO MULTIPLE COLUMNS (axis=1)")
print("=" * 50)
df['Total_Stats'] = df.apply(lambda row: row['HP'] + row['Attack'] + row['Defense'], axis=1)
print(df[['Name', 'HP', 'Attack', 'Defense', 'Total_Stats']].head(5))

print("\n" + "=" * 50)
print("4. MAP WITH DICTIONARY")
print("=" * 50)
type_map = {
    'Electric': 'E',
    'Fire': 'F',
    'Water': 'W',
    'Grass': 'G',
    'Psychic': 'P',
    'Dragon': 'D',
    'Normal': 'N',
    'Fighting': 'Fi',
    'Flying': 'Fl',
    'Poison': 'Po'
}
df['Type_Code'] = df['Type'].map(type_map)
print(df[['Name', 'Type', 'Type_Code']].head(10))

print("\n" + "=" * 50)
print("5. MAP WITH FUNCTION")
print("=" * 50)
df['Name_Upper'] = df['Name'].map(str.upper)
print(df[['Name', 'Name_Upper']].head(5))

print("\n" + "=" * 50)
print("6. APPLYMAP (ENTIRE DATAFRAME)")
print("=" * 50)
df_numeric = df[['HP', 'Attack', 'Defense', 'Speed']].head(3)
print("Original:")
print(df_numeric)
print("\nDivided by 10:")
print(df_numeric.applymap(lambda x: x / 10))

print("\n" + "=" * 50)
print("7. CONDITIONAL APPLY")
print("=" * 50)
df['Power_Rating'] = df['Attack'].apply(lambda x: 'Strong' if x > 80 else 'Weak')
print(df[['Name', 'Attack', 'Power_Rating']].head(10))

print("\n" + "=" * 50)
print("8. APPLY WITH MULTIPLE CONDITIONS")
print("=" * 50)
def battle_score(row):
    score = row['HP'] * 0.3 + row['Attack'] * 0.4 + row['Defense'] * 0.3
    return round(score, 2)

df['Battle_Score'] = df.apply(battle_score, axis=1)
print(df[['Name', 'HP', 'Attack', 'Defense', 'Battle_Score']].head(5))

print("\n" + "=" * 50)
print("9. VECTORIZED OPERATIONS (FASTER)")
print("=" * 50)
df['HP_Plus_Attack'] = df['HP'] + df['Attack']
print(df[['Name', 'HP', 'Attack', 'HP_Plus_Attack']].head(5))

print("\n" + "=" * 50)
print("10. REPLACE WITH MAP")
print("=" * 50)
df['Type_Full'] = df['Type'].map({
    'Electric': 'Electric Type',
    'Fire': 'Fire Type',
    'Water': 'Water Type'
}).fillna(df['Type'] + ' Type')
print(df[['Name', 'Type', 'Type_Full']].head(10))
