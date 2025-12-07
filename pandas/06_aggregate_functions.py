import pandas as pd
import os 
# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

# mean, median, mode, min, max, sum, count, std, var, describe
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path, index_col='Name')
print(df.head(5))

print("\n" + "=" * 50)
print(f"{"1. MEAN (WHOLE DATAFRAME)":^50}")
print("=" * 50)
print(df.mean(numeric_only=True))

print("\n" + "=" * 50)
print(f"{"2. SUM (WHOLE DATAFRAME)":^50}")
print("=" * 50)
print(df.sum(numeric_only=True))

print("\n" + "=" * 50)
print(f"{"3. MIN (WHOLE DATAFRAME)":^50}")
print("=" * 50)
print(df.min(numeric_only=True))


print("\n" + "=" * 50)
print(f"{"4. MAX (WHOLE DATAFRAME)":^50}")
print("=" * 50)
print(df.max(numeric_only=True))

print("\n" + "=" * 50)
print(f"{"5. COUNT (WHOLE DATAFRAME)":^50}")
print("=" * 50)
# print(df.count(numeric_only=True))
print(df.count())



print("\n" + "=" * 50)
print(f"{"1. MEAN (SINGLE COLUMN: HP)":^50}")
print("=" * 50)
print(df[["HP"]].mean(numeric_only=True))

print("\n" + "=" * 50)
print(f"{"2. SUM (SINGLE COLUMN: HP)":^50}")
print("=" * 50)
print(df["HP"].sum(numeric_only=True))

print("\n" + "=" * 50)
print(f"{"3. MIN (SINGLE COLUMN: HP)":^50}")
print("=" * 50)
print(df["HP"].min(numeric_only=True))


print("\n" + "=" * 50)
print(f"{"4. MAX (SINGLE COLUMN: HP)":^50}")
print("=" * 50)
print(df["HP"].max(numeric_only=True))

print("\n" + "=" * 50)
print(f"{"5. COUNT (SINGLE COLUMN: HP)":^50}")
print("=" * 50)
# print(df.count(numeric_only=True))
print(df["HP"].count())


print("\n" + "=" * 50)
print(f"{"GROUP BY":^50}")
group = df.groupby("Type")
print(group.mean(numeric_only=True))
print("=" * 50)

