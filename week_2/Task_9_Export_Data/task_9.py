from pathlib import Path

import pandas as pd

print("# ========================================")
print("TASK 9 - EXPORTING DATA")
print("# ========================================")

folder = Path(__file__).parent
sales = pd.read_csv(folder / "sales_data.csv")
processed_sales = sales[sales["Sales"] >= 5000][
    ["Order_ID", "Product", "Category", "Region", "Quantity", "Sales"]
].sort_values("Sales", ascending=False)

output_path = folder / "processed_sales_data.csv"
processed_sales.to_csv(output_path, index=False)
verified_data = pd.read_csv(output_path)

print("Processed rows:", len(processed_sales))
print("Exported file:", output_path.name)
print("\nVerified exported data:")
print(verified_data)
