"""
PANDAS LEARNING INDEX
Complete guide to learning pandas from basics to advanced
"""

print("=" * 70)
print(" " * 20 + "PANDAS LEARNING PATH")
print("=" * 70)

learning_path = """
📚 WEEK 1: FUNDAMENTALS (Files 01-06)
├── 01_intro_to_pandas.py              ✓ What is pandas
├── 02_series.py                       ✓ Series creation, indexing, filtering
├── 03_dataframe_basics.py             ✓ DataFrame creation, add/drop rows/columns
├── 04_reading_data.py                 ✓ CSV/JSON reading, loc/iloc selection
├── 05_dataframe_info.py               ✓ Understanding df.info() and dtypes
└── 06_understanding_object_dtype.py   ✓ Why text is 'object' dtype

📚 WEEK 2: DATA MANIPULATION (Files 07-11)
├── 07_column_operations.py            ✓ Rename, reorder, select columns
├── 08_filtering.py                    ✓ Boolean filtering, conditions
├── 09_sorting.py                      ✓ sort_values, sort_index
├── 10_index_operations.py             ✓ set_index, reset_index
└── 11_aggregate_functions.py          ✓ mean, sum, groupby

📚 WEEK 3: DATA CLEANING & TRANSFORMATION (Files 12-15)
├── 12_data_cleaning.py                ✓ fillna, dropna, duplicates
├── 13_string_operations.py            ✓ str methods (split, strip, contains)
├── 14_apply_map_lambda.py             ✓ Custom functions on data
└── 15_data_types_conversion.py        ✓ astype, to_numeric, to_datetime

📚 WEEK 4: ADVANCED OPERATIONS (Files 16-18)
├── 16_merging_joining.py              ✓ merge, join, concat
├── 17_pivot_reshape.py                ✓ pivot_table, melt, stack/unstack
└── 18_datetime_operations.py          ✓ Date parsing, time series basics

📊 DATA FILES
└── data/
    ├── pokemon.csv                    ✓ Sample CSV data
    └── pokemon.json                   ✓ Sample JSON data
"""

print(learning_path)

print("\n" + "=" * 70)
print("QUICK REFERENCE - KEY OPERATIONS")
print("=" * 70)

quick_ref = """
📖 READING DATA
• pd.read_csv('file.csv')              → Read CSV
• pd.read_json('file.json')            → Read JSON
• df.head(5), df.tail(5)               → View first/last rows

📖 SELECTION
• df['column']                         → Select column
• df[['col1', 'col2']]                 → Select multiple columns
• df.loc['row_label']                  → Select by label
• df.iloc[0]                           → Select by position
• df.loc['row', 'col']                 → Select specific cell

📖 FILTERING
• df[df['Age'] > 25]                   → Filter rows
• df[(df['Age'] > 25) & (df['City'] == 'NYC')]  → Multiple conditions

📖 SORTING
• df.sort_values('column')             → Sort by column
• df.sort_values(['col1', 'col2'])     → Sort by multiple columns
• df.sort_index()                      → Sort by index

📖 AGGREGATION
• df.mean(), df.sum(), df.max()        → Aggregate functions
• df.groupby('column').mean()          → Group and aggregate
• df.describe()                        → Statistical summary

📖 DATA CLEANING
• df.fillna(value)                     → Fill missing values
• df.dropna()                          → Drop rows with nulls
• df.drop_duplicates()                 → Remove duplicates
• df.replace(old, new)                 → Replace values

📖 COLUMN OPERATIONS
• df.rename(columns={'old': 'new'})    → Rename columns
• df.drop('column', axis=1)            → Drop column
• df['new_col'] = df['col1'] + df['col2']  → Create column

📖 STRING OPERATIONS
• df['col'].str.lower()                → Lowercase
• df['col'].str.contains('text')       → Check if contains
• df['col'].str.split(',')             → Split strings

📖 APPLY FUNCTIONS
• df['col'].apply(lambda x: x * 2)     → Apply function to column
• df.apply(func, axis=1)               → Apply to rows
• df['col'].map({'A': 1, 'B': 2})      → Map values

📖 MERGING
• pd.merge(df1, df2, on='key')         → Merge DataFrames
• pd.concat([df1, df2])                → Concatenate DataFrames
"""

print(quick_ref)

print("\n" + "=" * 70)
print("LEARNING TIPS")
print("=" * 70)

tips = """
💡 BEST PRACTICES
1. Always check df.info() after loading data
2. Use df.head() to preview data before operations
3. Check for null values with df.isnull().sum()
4. Use meaningful column names
5. Keep original data, create copies for modifications

🎯 COMMON PATTERNS
• Load → Inspect → Clean → Transform → Analyze
• Use method chaining: df.fillna(0).sort_values('col').head(10)
• Save intermediate results for debugging
• Use .copy() to avoid SettingWithCopyWarning

⚡ PERFORMANCE TIPS
• Use vectorized operations instead of loops
• Filter early to reduce data size
• Use appropriate dtypes (category for repeated strings)
• Read only needed columns: pd.read_csv('file.csv', usecols=['col1', 'col2'])
"""

print(tips)

print("\n" + "=" * 70)
print("START YOUR LEARNING JOURNEY")
print("=" * 70)
print("\n👉 Begin with: 01_intro_to_pandas.py")
print("👉 Follow the sequence for smooth learning")
print("👉 Practice with pokemon.csv dataset")
print("\n" + "=" * 70)
