import pandas as pd
from datetime import datetime, timedelta

print("=" * 60)
print("DATETIME OPERATIONS")
print("=" * 60)

print("\n" + "=" * 50)
print("1. CREATE DATETIME SERIES")
print("=" * 50)
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=5, freq='D'),
    'Value': [10, 20, 15, 25, 30]
})
print(df)

print("\n" + "=" * 50)
print("2. PARSE STRING TO DATETIME")
print("=" * 50)
df_str = pd.DataFrame({'Date': ['2024-01-01', '2024-01-02', '2024-01-03']})
df_str['Date'] = pd.to_datetime(df_str['Date'])
print(df_str)
print(df_str.dtypes)

print("\n" + "=" * 50)
print("3. EXTRACT DATE COMPONENTS")
print("=" * 50)
date_col = df['Date']
df['Year'] = date_col.dt.year  # type: ignore
df['Month'] = date_col.dt.month  # type: ignore
df['Day'] = date_col.dt.day  # type: ignore
df['DayOfWeek'] = date_col.dt.day_name()  # type: ignore
print(df)

print("\n" + "=" * 50)
print("4. DATE ARITHMETIC")
print("=" * 50)
df['Next_Week'] = df['Date'] + pd.Timedelta(days=7)
df['Last_Week'] = df['Date'] - pd.Timedelta(days=7)
print(df[['Date', 'Next_Week', 'Last_Week']])

print("\n" + "=" * 50)
print("5. FILTER BY DATE RANGE")
print("=" * 50)
df_filtered = df[df['Date'] >= '2024-01-03']
print(df_filtered)

print("\n" + "=" * 50)
print("6. SET DATE AS INDEX")
print("=" * 50)
df_indexed = df.set_index('Date')
print(df_indexed)

print("\n" + "=" * 50)
print("7. RESAMPLE (TIME-BASED GROUPING)")
print("=" * 50)
df_ts = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'Sales': [100, 150, 120, 180, 200, 160, 140, 190, 210, 170]
})
df_ts = df_ts.set_index('Date')
weekly = df_ts.resample('W').sum()
print("Daily sales:")
print(df_ts.head())
print("\nWeekly sales (resampled):")
print(weekly)

print("\n" + "=" * 50)
print("8. DATE DIFFERENCE")
print("=" * 50)
df_diff = pd.DataFrame({
    'Start': pd.to_datetime(['2024-01-01', '2024-01-05']),
    'End': pd.to_datetime(['2024-01-10', '2024-01-15'])
})
df_diff['Days_Diff'] = (df_diff['End'] - df_diff['Start']).dt.days
print(df_diff)

print("\n" + "=" * 50)
print("9. FORMAT DATETIME")
print("=" * 50)
date_series = pd.date_range('2024-01-01', periods=5, freq='D')
df_format = pd.DataFrame({'Date': date_series})
df_format['Date_Formatted'] = date_series.strftime('%Y-%m-%d')
df_format['Date_Custom'] = date_series.strftime('%B %d, %Y')
print(df_format)

print("\n" + "=" * 50)
print("10. CURRENT DATE/TIME")
print("=" * 50)
now = pd.Timestamp.now()
today = pd.Timestamp.today()
print(f"Now: {now}")
print(f"Today: {today}")
print(f"Current year: {now.year}")
print(f"Current month: {now.month}")
