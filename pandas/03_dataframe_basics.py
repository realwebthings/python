import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [20, 21, 19],
    "Color": ["Red", "Orange", "Blue"]
}

df = pd.DataFrame(data)
print("\n" + "=" * 20+ " Data Frame "+"=" * 20)
print(df)
print("\n" + "=" * 20+ " Indexed Data Frame "+"=" * 20)
df = pd.DataFrame(data, index=["Person1", "Person2", "Person3"])
print(df)

print("\n" + "=" * 20+ " Locate Row "+"=" * 20)
print(df.loc["Person1"])

print("\n" + "=" * 20+ " Indexed Locate Row "+"=" * 20)
print("iloc: \n",df.iloc[0])

print("\n" + "=" * 20+ " Add a new column "+"=" * 20)

df["Weight"] = [70, 80, 90]
print(df)

print("\n" + "=" * 20+ " Add a new row "+"=" * 20)
new_row = pd.DataFrame({"Name": "Sandy", "Age": 20, "Color": "Pink", "Weight": 60}, index=["Person4"])
df = pd.concat([df, new_row])
print(df)


print("\n" + "=" * 20+ " Add rows "+"=" * 20)
new_rows = pd.DataFrame([{"Name": "Jeff", "Age": 21, "Color": "Purple", "Weight": 62},
                         {"Name": "Larry", "Age": 22, "Color": "Green", "Weight": 75}], 
                         index=["Person5", "Person6"])

df = pd.concat([df, new_rows])
print(df)

print("\n" + "=" * 20+ " Drop a column "+"=" * 20)
df_no_weight = df.drop("Weight", axis=1)
print(df_no_weight)

print("\n" + "=" * 20+ " Drop a row "+"=" * 20)
df_no_person1 = df.drop("Person1", axis=0)
print(df_no_person1)

