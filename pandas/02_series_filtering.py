import pandas as pd

#Series = A pandas series is like a column in a table
#It is a one-dimensional array holding data of any type
# Think of it like a single column in a spreadsheet

a = [1, 7, 2]

series = pd.Series(a)

series.sort_values(ascending=True, inplace=True)

print(series)

b = ["A", 1, 2]

series = pd.Series(b)

print(series)

c = [1.2, 3.4, 2.1]

series = pd.Series(c)

print(series)

d = [True, False, True]

series = pd.Series(d)

print(series)


e = [100, 101, 102]

series = pd.Series(e, index = ["a", "b", "c"])


print(series)
print(series["a"])

try:
    print(series["d"])
except:
    print("Index not found")

print("try: ",series[0]) 
# Output: 
# /Users/mukeshkumar/MyRepo/python/pandas/02_series.py:45: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
# print("try: ",series[0])
# try:  100

print("iloc: ", series.iloc[0])

print("filtering: ",series[series < 101])

print("\n" + "=" * 60)
print("CREATE SERIES FROM DICTIONARY")
calories = {"day1": 420, "day2": 380, "day3": 390}
series = pd.Series(calories)

print(series)
print("direct access: day1: ", series["day1"])
print("iloc: ", series.iloc[0])
print("loc: ", series.loc["day1"])
print("filtering:\n", series[series < 400])

series.loc['day3'] = series.loc['day3'] + 10
print("updated: ", series)
print("\n" + "=" * 60)