from pathlib import Path

import pandas as pd

print("# ========================================")
print("TASK 6 - SELECTING, FILTERING & SORTING")
print("# ========================================")

file_path = Path(__file__).parent / "sales_data.csv"
sales = pd.read_csv(file_path)

print("\nSelected columns:")
print(sales[["Order_ID", "Product", "Region", "Sales"]].head())
print("\nSelected rows using iloc:")
print(sales.iloc[0:3])
print("\nSales greater than 10000:")
print(sales[sales["Sales"] > 10000][["Order_ID", "Product", "Sales"]])
print("\nElectronics sales in the Central region:")
print(sales[(sales["Category"] == "Electronics") & (sales["Region"] == "Central")][["Product", "Region", "Sales"]])
print("\nSales sorted in ascending order:")
print(sales[["Product", "Sales"]].sort_values("Sales").head())
print("\nSales sorted in descending order:")
print(sales[["Product", "Sales"]].sort_values("Sales", ascending=False).head())
