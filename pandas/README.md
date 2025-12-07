# Pandas Learning Guide

Complete guide to learning pandas from basics to advanced concepts.

## 📁 Folder Structure

```
pandas/
├── 00_pandas_index.py                 # Learning roadmap and quick reference
├── data/
│   ├── pokemon.csv                    # Sample CSV dataset
│   └── pokemon.json                   # Sample JSON dataset
│
├── WEEK 1: FUNDAMENTALS
├── 01_intro_to_pandas.py              # What is pandas
├── 02_series.py                       # Series creation, indexing, filtering
├── 03_dataframe_basics.py             # DataFrame creation, add/drop rows/columns
├── 04_reading_data.py                 # CSV/JSON reading, loc/iloc selection
├── 05_dataframe_info.py               # Understanding df.info() and dtypes
├── 06_understanding_object_dtype.py   # Why text is 'object' dtype
│
├── WEEK 2: DATA MANIPULATION
├── 07_column_operations.py            # Rename, reorder, select columns
├── 08_filtering.py                    # Boolean filtering, conditions
├── 09_sorting.py                      # sort_values, sort_index
├── 10_index_operations.py             # set_index, reset_index
├── 11_aggregate_functions.py          # mean, sum, groupby
│
├── WEEK 3: DATA CLEANING & TRANSFORMATION
├── 12_data_cleaning.py                # fillna, dropna, duplicates
├── 13_string_operations.py            # str methods (split, strip, contains)
├── 14_apply_map_lambda.py             # Custom functions on data
├── 15_data_types_conversion.py        # astype, to_numeric, to_datetime
│
└── WEEK 4: ADVANCED OPERATIONS
    ├── 16_merging_joining.py          # merge, join, concat
    ├── 17_pivot_reshape.py            # pivot_table, melt, stack/unstack
    └── 18_datetime_operations.py      # Date parsing, time series basics
```

## 🎯 Learning Path

### Week 1: Fundamentals (Files 01-06)
Master the basics of pandas including Series, DataFrames, and data loading.

**Topics:**
- What is pandas and why use it
- Series: one-dimensional labeled arrays
- DataFrame: two-dimensional labeled data structure
- Reading CSV and JSON files
- Understanding data types and df.info()
- Selecting data with loc and iloc

**Key Concepts:**
```python
# Create Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Create DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

# Read data
df = pd.read_csv('file.csv')

# Select data
df.loc['row_label']      # By label
df.iloc[0]               # By position
```

### Week 2: Data Manipulation (Files 07-11)
Learn to manipulate and transform your data effectively.

**Topics:**
- Column operations (rename, reorder, select)
- Filtering with boolean conditions
- Sorting by values and index
- Index operations
- Aggregate functions and groupby

**Key Concepts:**
```python
# Column operations
df.rename(columns={'old': 'new'})
df[['col1', 'col2']]

# Filtering
df[df['Age'] > 25]
df[(df['Age'] > 25) & (df['City'] == 'NYC')]

# Sorting
df.sort_values('column')
df.sort_index()

# Aggregation
df.groupby('Type').mean()
```

### Week 3: Data Cleaning & Transformation (Files 12-15)
Master data cleaning and transformation techniques.

**Topics:**
- Handling missing values
- String operations
- Applying custom functions
- Data type conversions

**Key Concepts:**
```python
# Data cleaning
df.fillna(0)
df.dropna()
df.drop_duplicates()

# String operations
df['col'].str.lower()
df['col'].str.contains('text')

# Apply functions
df['col'].apply(lambda x: x * 2)
df.apply(func, axis=1)

# Type conversion
df['col'].astype(int)
pd.to_datetime(df['date'])
```

### Week 4: Advanced Operations (Files 16-18)
Explore advanced pandas features for complex data operations.

**Topics:**
- Merging and joining DataFrames
- Pivot tables and reshaping
- DateTime operations

**Key Concepts:**
```python
# Merging
pd.merge(df1, df2, on='key', how='inner')
pd.concat([df1, df2])

# Pivot
df.pivot_table(values='val', index='idx', aggfunc='mean')
df.melt(id_vars='id', var_name='var', value_name='val')

# DateTime
pd.to_datetime(df['date'])
df['date'].dt.year
df.resample('W').sum()
```

## 📊 Quick Reference

### Reading Data
```python
pd.read_csv('file.csv')              # Read CSV
pd.read_json('file.json')            # Read JSON
pd.read_excel('file.xlsx')           # Read Excel
df.head(5)                           # First 5 rows
df.tail(5)                           # Last 5 rows
df.info()                            # DataFrame info
df.describe()                        # Statistical summary
```

### Selection
```python
df['column']                         # Single column
df[['col1', 'col2']]                 # Multiple columns
df.loc['row_label']                  # Row by label
df.iloc[0]                           # Row by position
df.loc['row', 'col']                 # Specific cell
df.loc[df['Age'] > 25]               # Conditional selection
```

### Filtering
```python
df[df['Age'] > 25]                   # Single condition
df[(df['Age'] > 25) & (df['City'] == 'NYC')]  # Multiple conditions
df[df['Name'].str.contains('John')]  # String filtering
df.query('Age > 25 and City == "NYC"')  # Query syntax
```

### Sorting
```python
df.sort_values('column')             # Sort by column
df.sort_values(['col1', 'col2'])     # Sort by multiple
df.sort_index()                      # Sort by index
df.sort_values('col', ascending=False)  # Descending
```

### Aggregation
```python
df.mean()                            # Mean of all columns
df['col'].sum()                      # Sum of column
df.groupby('Type').mean()            # Group and aggregate
df.groupby(['Type', 'Category']).agg({'HP': 'mean', 'Attack': 'max'})
```

### Data Cleaning
```python
df.fillna(0)                         # Fill missing with 0
df.fillna(df.mean())                 # Fill with mean
df.dropna()                          # Drop rows with NaN
df.drop_duplicates()                 # Remove duplicates
df.replace(old, new)                 # Replace values
```

### Column Operations
```python
df.rename(columns={'old': 'new'})    # Rename columns
df.drop('column', axis=1)            # Drop column
df['new'] = df['col1'] + df['col2']  # Create column
df.insert(1, 'new_col', values)      # Insert at position
```

### String Operations
```python
df['col'].str.lower()                # Lowercase
df['col'].str.upper()                # Uppercase
df['col'].str.contains('text')       # Check contains
df['col'].str.split(',')             # Split string
df['col'].str.strip()                # Remove whitespace
df['col'].str.replace('old', 'new')  # Replace in string
```

### Apply Functions
```python
df['col'].apply(lambda x: x * 2)     # Apply to column
df.apply(func, axis=1)               # Apply to rows
df['col'].map({'A': 1, 'B': 2})      # Map values
df.applymap(func)                    # Apply to all cells
```

### Merging
```python
pd.merge(df1, df2, on='key')         # Inner join
pd.merge(df1, df2, how='left')       # Left join
pd.merge(df1, df2, how='outer')      # Outer join
pd.concat([df1, df2])                # Concatenate
df1.join(df2)                        # Join on index
```

### Reshaping
```python
df.pivot_table(values='val', index='idx')  # Pivot table
df.melt(id_vars='id')                # Wide to long
df.stack()                           # Columns to rows
df.unstack()                         # Rows to columns
df.T                                 # Transpose
```

### DateTime
```python
pd.to_datetime(df['date'])           # Parse to datetime
df['date'].dt.year                   # Extract year
df['date'].dt.month                  # Extract month
df['date'].dt.day_name()             # Day name
df.resample('W').sum()               # Resample by week
```

## 💡 Best Practices

1. **Always check data first**
   ```python
   df.info()
   df.head()
   df.isnull().sum()
   ```

2. **Use method chaining**
   ```python
   df.fillna(0).sort_values('col').head(10)
   ```

3. **Avoid loops, use vectorization**
   ```python
   # Bad: for loop
   for i in range(len(df)):
       df.loc[i, 'new'] = df.loc[i, 'col'] * 2
   
   # Good: vectorized
   df['new'] = df['col'] * 2
   ```

4. **Use .copy() to avoid warnings**
   ```python
   df_new = df[df['Age'] > 25].copy()
   ```

5. **Read only needed columns**
   ```python
   df = pd.read_csv('file.csv', usecols=['col1', 'col2'])
   ```

## 🎓 Learning Tips

- Start with `00_pandas_index.py` for overview
- Follow files in sequence (01 → 18)
- Practice with `pokemon.csv` dataset
- Run each file and observe outputs
- Modify code to experiment
- Use `df.head()` frequently to check results

## 📈 Progress Tracker

- [ ] Week 1: Fundamentals (01-06)
  - [ ] 01_intro_to_pandas.py
  - [ ] 02_series.py
  - [ ] 03_dataframe_basics.py
  - [ ] 04_reading_data.py
  - [ ] 05_dataframe_info.py
  - [ ] 06_understanding_object_dtype.py

- [ ] Week 2: Data Manipulation (07-11)
  - [ ] 07_column_operations.py
  - [ ] 08_filtering.py
  - [ ] 09_sorting.py
  - [ ] 10_index_operations.py
  - [ ] 11_aggregate_functions.py

- [ ] Week 3: Data Cleaning (12-15)
  - [ ] 12_data_cleaning.py
  - [ ] 13_string_operations.py
  - [ ] 14_apply_map_lambda.py
  - [ ] 15_data_types_conversion.py

- [ ] Week 4: Advanced (16-18)
  - [ ] 16_merging_joining.py
  - [ ] 17_pivot_reshape.py
  - [ ] 18_datetime_operations.py

## 🚀 Getting Started

```bash
# Navigate to pandas folder
cd /Users/mukeshkumar/MyRepo/python/pandas

# Start with the index
python 00_pandas_index.py

# Follow the learning path
python 01_intro_to_pandas.py
python 02_series.py
# ... and so on
```

## 📚 Additional Resources

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

**Happy Learning! 🐼**
