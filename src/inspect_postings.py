import pandas as pd

file_path = "data/raw/postings.csv"

df = pd.read_csv(file_path, nrows=1000)

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())
