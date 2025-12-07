import pandas as pd
import os

print("=" * 60)
print("UNDERSTANDING df.info() OUTPUT")
print("=" * 60)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data', 'pokemon.csv')
df = pd.read_csv(csv_path)

print("\n" + "=" * 50)
print("DATAFRAME INFO")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("EXPLANATION OF df.info() OUTPUT")
print("=" * 50)

print("""
1. <class 'pandas.core.frame.DataFrame'>
   → This is a pandas DataFrame object

2. RangeIndex: 20 entries, 0 to 19
   → Index type: RangeIndex (default numeric index)
   → Total rows: 20
   → Index range: 0 to 19

3. Data columns (total 6 columns):
   → The DataFrame has 6 columns

4. Column Details:
   #   Column   Non-Null Count  Dtype
   -----------------------------------
   0   Name     20 non-null     object
   → Column 0: 'Name'
   → Has 20 values (no missing data)
   → Data type: object (string/text)

   1   Type     20 non-null     object
   → Column 1: 'Type'
   → Has 20 values (no missing data)
   → Data type: object (string/text)

   2   HP       20 non-null     int64
   → Column 2: 'HP'
   → Has 20 values (no missing data)
   → Data type: int64 (64-bit integer)

   3   Attack   20 non-null     int64
   4   Defense  20 non-null     int64
   5   Speed    20 non-null     int64
   → Similar structure for numeric columns

5. dtypes: int64(4), object(2)
   → Summary of data types:
   → int64(4) means 4 columns have int64 type:
      - HP, Attack, Defense, Speed
   → object(2) means 2 columns have object type:
      - Name, Type
   → The number in parentheses is the COUNT of columns with that type

6. memory usage: 1.1+ KB
   → Total memory used by DataFrame
   → Approximately 1.1 kilobytes
""")

print("\n" + "=" * 50)
print("KEY CONCEPTS")
print("=" * 50)

print("""
DATA TYPES (Dtype):
• object   → Text/strings/mixed types
             In our data: Name='Pikachu', Type='Electric'
             2 columns: Name, Type
• int64    → 64-bit integers (whole numbers)
             In our data: HP=35, Attack=55, Defense=40, Speed=90
             4 columns: HP, Attack, Defense, Speed
• float64  → Decimal numbers (e.g., 3.14, 2.5)
• bool     → True/False values
• datetime → Date/time values

WHY 'object' FOR TEXT?
• In pandas, text/strings are stored as 'object' dtype
• 'object' can hold any Python object (strings, mixed types)
• More flexible but uses more memory than specialized string types

NON-NULL COUNT:
• Shows how many non-missing values in each column
• If Non-Null Count < Total Rows → Missing data exists
• Example: "20 non-null" means all 20 rows have values

MEMORY USAGE:
• Shows how much RAM the DataFrame uses
• Larger DataFrames use more memory
• Important for big datasets
""")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\nChecking for missing data:")
print(df.isnull().sum())

print("\nData types of each column:")
print(df.dtypes)

print("\nMemory usage per column:")
print(df.memory_usage(deep=True))

print("\nQuick statistics:")
print(df.describe())

print("\n" + "=" * 50)
print("WHEN TO USE df.info()")
print("=" * 50)

print("""
Use df.info() when you want to:
✓ Check data types of columns
✓ Find missing values (Non-Null Count)
✓ See total rows and columns
✓ Check memory usage
✓ Get quick overview of DataFrame structure

It's usually the FIRST thing you do after loading data!
""")
