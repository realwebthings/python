import pandas as pd
import os 
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path, index_col='Name')
print(df.head(5))
print("\n" + "=" * 50)
# Filtering = Keeping the rows that match the condition
print(f"{"SPEED > 100":^50}")
print("=" * 50)

tall_pokemon = df[df['Speed'] > 100]
print(tall_pokemon)
print("\n" + "=" * 50)
print(f"{"Type == Electric AND Speed >= 100":^50}")
print("=" * 50)
type_pokemon = df[(df['Type'] == 'Electric') & (df['Speed'] >= 100)]
print(type_pokemon)
print("=" * 50)
# df = df.dropna() # drop rows with missing values
# df = df.fillna(130) # fill missing values with 130
# df = df.fillna(df["Calories"].mean()) # fill missing values with mean