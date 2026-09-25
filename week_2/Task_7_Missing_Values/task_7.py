from pathlib import Path

import pandas as pd

print("# ========================================")
print("TASK 7 - HANDLING MISSING VALUES")
print("# ========================================")

file_path = Path(__file__).parent / "missing_values_data.csv"
sales = pd.read_csv(file_path)
print("\nOriginal dataset:")
print(sales)
print("\nMissing-value mask:")
print(sales.isnull())
print("\nMissing values by column:")
print(sales.isna().sum())

without_missing_rows = sales.dropna()
filled_sales = sales.copy()
filled_sales["Quantity"] = filled_sales["Quantity"].fillna(filled_sales["Quantity"].median())
filled_sales["Unit_Price"] = filled_sales["Unit_Price"].fillna(filled_sales["Unit_Price"].median())
filled_sales["Category"] = filled_sales["Category"].fillna(filled_sales["Category"].mode()[0])

print("\nAfter removing rows with missing values:")
print(without_missing_rows)
print("\nAfter filling missing values:")
print(filled_sales)
print("\nMissing data should be handled because incomplete values can affect calculations and lead to unreliable analysis.")
