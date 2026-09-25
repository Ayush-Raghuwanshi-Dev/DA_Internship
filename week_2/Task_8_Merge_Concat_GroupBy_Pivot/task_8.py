from pathlib import Path

import pandas as pd

print("# ========================================")
print("TASK 8 - MERGE, CONCATENATE, GROUPBY & PIVOT")
print("# ========================================")

folder = Path(__file__).parent
sales = pd.read_csv(folder / "sales_data.csv")
products = pd.read_csv(folder / "product_data.csv")

merged = pd.merge(sales, products, on="Product_ID", suffixes=("_sale", "_product"))
print("\nMerged DataFrame:")
print(merged[["Order_ID", "Product_ID", "Product_sale", "Category_sale", "Sales"]].head())

first_part = sales.iloc[:3][["Order_ID", "Region", "Sales"]]
second_part = sales.iloc[3:6][["Order_ID", "Region", "Sales"]]
concatenated = pd.concat([first_part, second_part], ignore_index=True)
print("\nConcatenated DataFrames:")
print(concatenated)

category_summary = sales.groupby("Category")["Sales"].agg(["sum", "mean", "count", "min", "max"])
print("\nGroupBy summary by Category:")
print(category_summary)

pivot = pd.pivot_table(
    sales,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)
print("\nPivot table of sales by Region and Category:")
print(pivot)
