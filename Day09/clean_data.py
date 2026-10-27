import pandas as pd

# 1. Load the messy CSV
df=pd.read_csv('Day09/messy_data.csv')

print("\n---Original DataFrame---\n")
print(df)

# .isna() checks every cell for NaN. .sum() adds up the Trues for each column.
print("\n---Where is the missing data?---\n")
print(df.isna().sum())

df_dropped = df.dropna()  # Drop rows with any NaN values

print("\n---DataFrame after dropping missing values---\n")
print(df_dropped)

df_filled = df.fillna({"salary":0, "role": "Unknown"})
print("\n--- AFTER FILLING MISSING VALUES ---")
print(df_filled)

print("\n---Fixing the data types---\n")
df_filled['salary'] = df_filled['salary'].astype(int)
print(df_filled.dtypes)

df_filled.to_csv('Day09/cleaned_data.csv', index=False)
print("\n---Cleaned data saved to CSV---")