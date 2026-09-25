from pathlib import Path

import numpy as np
import pandas as pd

print("# ========================================")
print("TASK 10 - SALES DATA ANALYSIS USING NUMPY & PANDAS")
print("# ========================================")

folder = Path(__file__).parent
sales = pd.read_csv(folder / "sales_data.csv", parse_dates=["Date"])
products = pd.read_csv(folder / "product_data.csv")

print("\nDataset inspection:")
print(sales.head())
print("Shape:", sales.shape)
print("\nMissing values:")
print(sales.isna().sum())

sales = sales.dropna().copy()
sales["Sales_Check"] = sales["Quantity"] * sales["Unit_Price"]
print("Sales calculation matches source column:", sales["Sales"].equals(sales["Sales_Check"]))
sales = sales.drop(columns=["Sales_Check"])

selected_data = sales[["Date", "Product", "Category", "Region", "Quantity", "Sales"]]
high_value_orders = selected_data[selected_data["Sales"] > 10000].sort_values("Sales", ascending=False)
print("\nHigh-value orders:")
print(high_value_orders)

category_summary = sales.groupby("Category")["Sales"].agg(["sum", "mean", "count"])
region_summary = sales.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by category:")
print(category_summary)
print("\nSales by region:")
print(region_summary)

pivot = pd.pivot_table(
    sales,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)
print("\nPivot table:")
print(pivot)

product_sales = sales.groupby("Product")["Sales"].sum()
total_sales = sales["Sales"].sum()
average_sales = sales["Sales"].mean()
maximum_sale = sales["Sales"].max()
minimum_sale = sales["Sales"].min()
total_quantity = sales["Quantity"].sum()
top_product = product_sales.idxmax()
best_region = region_summary.idxmax()
best_category = category_summary["sum"].idxmax()

print("\nCalculated insights:")
print(f"Total sales: Rs. {total_sales:,.2f}")
print(f"Average sales per order: Rs. {average_sales:,.2f}")
print(f"Maximum sale: Rs. {maximum_sale:,.2f}")
print(f"Minimum sale: Rs. {minimum_sale:,.2f}")
print(f"Total quantity sold: {total_quantity}")
print(f"Top-performing product: {top_product} (Rs. {product_sales[top_product]:,.2f})")
print(f"Highest-sales region: {best_region} (Rs. {region_summary[best_region]:,.2f})")
print(f"Highest-sales category: {best_category} (Rs. {category_summary.loc[best_category, 'sum']:,.2f})")
print("\nAverage sales by category:")
for cat, avg in category_summary["mean"].items():
    print(f"  - {cat}: Rs. {avg:,.2f}")

cleaned_path = folder / "cleaned_sales_data.csv"
sales.to_csv(cleaned_path, index=False)
summary_path = folder / "analysis_summary.txt"

avg_by_cat_lines = "\n".join([f"  - {cat}: Rs. {avg:,.2f}" for cat, avg in category_summary["mean"].items()])

summary_content = (
    "SALES DATA ANALYSIS SUMMARY\n"
    "===========================\n"
    "Educational synthetic dataset created specifically for this assignment.\n\n"
    f"The dataset contains {len(sales)} sales records.\n"
    f"Total sales across the dataset were Rs. {total_sales:,.2f}.\n"
    f"Average sales per order were Rs. {average_sales:,.2f}.\n"
    f"The maximum single-order sale was Rs. {maximum_sale:,.2f}.\n"
    f"The minimum single-order sale was Rs. {minimum_sale:,.2f}.\n"
    f"Total quantity sold across all orders was {total_quantity} units.\n"
    f"The top-performing product was {top_product}, with total sales of Rs. {product_sales[top_product]:,.2f}.\n"
    f"The region with the highest total sales was {best_region}, with Rs. {region_summary[best_region]:,.2f}.\n"
    f"The highest-selling category was {best_category}, with Rs. {category_summary.loc[best_category, 'sum']:,.2f}.\n\n"
    "Average Sales by Category:\n"
    f"{avg_by_cat_lines}\n"
)
summary_path.write_text(summary_content, encoding="utf-8")
print("\nCleaned data exported to:", cleaned_path.name)
print("Analysis summary saved to:", summary_path.name)
