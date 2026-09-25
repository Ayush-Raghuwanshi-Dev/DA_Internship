from pathlib import Path

import pandas as pd

sales = pd.read_csv(Path(__file__).parent / "sales_data.csv")

print("# ========================================")
print("TASK 5 - READING & INSPECTING DATA")
print("# ========================================")

print("\nFirst 5 rows:")
print(sales.head())
print("\nLast 5 rows:")
print(sales.tail())
print("\nNumber of rows and columns:", sales.shape)
print("\nColumn names:")
print(list(sales.columns))
print("\nData types:")
print(sales.dtypes)
print("\nDataFrame information:")
sales.info()
print("\nDescriptive statistics:")
print(sales.describe())
