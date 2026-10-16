"""
Task 4: DAX Measures & Calculated Columns Verification Engine
Internship: Data Analytics - Week 5
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Compute, verify, and document exact mathematical outputs for 16+ production
           DAX measures and calculated columns against the Star Schema dataset.
"""

import os
from pathlib import Path
import pandas as pd
import numpy as np

def run_task_4():
    print("=" * 85)
    print("WEEK 5 - TASK 4: DAX CALCULATED COLUMNS & MEASURES VERIFICATION")
    print("=" * 85)

    base_dir = Path(__file__).resolve().parent.parent / "Data"
    df_sales = pd.read_csv(base_dir / "Fact_Sales.csv")
    df_date = pd.read_csv(base_dir / "Dim_Date.csv")
    df_prod = pd.read_csv(base_dir / "Dim_Product.csv")
    df_cust = pd.read_csv(base_dir / "Dim_Customer.csv")
    df_reg = pd.read_csv(base_dir / "Dim_Region.csv")

    # Merge date details for temporal calculations
    df_merged = df_sales.merge(df_date, on="Date_Key", how="left")
    df_merged = df_merged.merge(df_prod, on="Product_Key", how="left")
    df_merged = df_merged.merge(df_reg, on="Region_Key", how="left")

    print(f"Loaded {len(df_sales)} sales transactions for DAX calculation verification.\n")

    # -------------------------------------------------------------
    # 1. CORE AGGREGATION & RATIO DAX MEASURES
    # -------------------------------------------------------------
    total_sales = float(df_sales["Sales_Amount"].sum())
    total_cost = float(df_sales["Total_Cost"].sum())
    total_profit = float(df_sales["Profit"].sum())
    profit_margin_pct = (total_profit / total_sales) * 100 if total_sales > 0 else 0.0
    total_quantity = int(df_sales["Quantity"].sum())
    total_orders = int(df_sales["Order_ID"].nunique())
    aov = total_sales / total_orders if total_orders > 0 else 0.0
    avg_units_per_order = total_quantity / total_orders if total_orders > 0 else 0.0
    max_order_val = float(df_sales["Sales_Amount"].max())
    min_order_val = float(df_sales["Sales_Amount"].min())

    measures_core = [
        ("Total Sales", f"INR {total_sales:,.2f}", "SUM(Fact_Sales[Sales_Amount])", "Gross merchandise revenue"),
        ("Total Cost", f"INR {total_cost:,.2f}", "SUM(Fact_Sales[Total_Cost])", "Manufacturing + logistics cost"),
        ("Total Profit", f"INR {total_profit:,.2f}", "[Total Sales] - [Total Cost]", "Net commercial gross profit"),
        ("Profit Margin %", f"{profit_margin_pct:.2f}%", "DIVIDE([Total Profit], [Total Sales], 0)", "Overall margin health ratio"),
        ("Total Quantity Sold", f"{total_quantity:,} units", "SUM(Fact_Sales[Quantity])", "Physical volume throughput"),
        ("Total Distinct Orders", f"{total_orders:,} orders", "DISTINCTCOUNT(Fact_Sales[Order_ID])", "Unique customer transactions"),
        ("Average Order Value (AOV)", f"INR {aov:,.2f}", "DIVIDE([Total Sales], [Total Orders], 0)", "Mean revenue per transaction"),
        ("Average Units / Order", f"{avg_units_per_order:.2f} units", "DIVIDE([Total Quantity], [Total Orders], 0)", "Mean basket quantity"),
        ("Max Single Order Value", f"INR {max_order_val:,.2f}", "MAXX(Fact_Sales, Fact_Sales[Sales_Amount])", "Highest individual basket"),
        ("Min Single Order Value", f"INR {min_order_val:,.2f}", "MINX(Fact_Sales, Fact_Sales[Sales_Amount])", "Lowest individual basket")
    ]

    print("-" * 85)
    print("SECTION 1: CORE REVENUE, COST & TRANSACTIONAL DAX MEASURES")
    print("-" * 85)
    print(f"{'Measure Name':<26} | {'Computed Output':>18} | {'DAX Expression':<36}")
    print("-" * 85)
    for m_name, m_val, m_dax, m_desc in measures_core:
        print(f"{m_name:<26} | {m_val:>18} | {m_dax:<36}")
    print()

    # -------------------------------------------------------------
    # 2. TIME INTELLIGENCE DAX (2024, 2025, 2026 YoY ANALYSIS)
    # -------------------------------------------------------------
    yearly_sales = df_merged.groupby("Year")["Sales_Amount"].sum().to_dict()
    yearly_profit = df_merged.groupby("Year")["Profit"].sum().to_dict()

    sales_2024 = yearly_sales.get(2024, 0.0)
    sales_2025 = yearly_sales.get(2025, 0.0)
    sales_2026 = yearly_sales.get(2026, 0.0)

    profit_2024 = yearly_profit.get(2024, 0.0)
    profit_2025 = yearly_profit.get(2025, 0.0)
    profit_2026 = yearly_profit.get(2026, 0.0)

    yoy_sales_2025 = ((sales_2025 - sales_2024) / sales_2024) * 100 if sales_2024 > 0 else 0.0
    yoy_sales_2026 = ((sales_2026 - sales_2025) / sales_2025) * 100 if sales_2025 > 0 else 0.0

    yoy_profit_2025 = ((profit_2025 - profit_2024) / profit_2024) * 100 if profit_2024 > 0 else 0.0
    yoy_profit_2026 = ((profit_2026 - profit_2025) / profit_2025) * 100 if profit_2025 > 0 else 0.0

    print("-" * 85)
    print("SECTION 2: TIME INTELLIGENCE & YEAR-OVER-YEAR (YOY) DAX MEASURES")
    print("-" * 85)
    print(f"Calendar Year 2024 Sales (Base Year) : INR {sales_2024:,.2f} | Profit: INR {profit_2024:,.2f}")
    print(f"Calendar Year 2025 Sales (Growth)    : INR {sales_2025:,.2f} | Profit: INR {profit_2025:,.2f}")
    print(f"Calendar Year 2026 Sales (YTD Run)   : INR {sales_2026:,.2f} | Profit: INR {profit_2026:,.2f}")
    print(f"  * YoY Sales Growth (2025 vs 2024)  : {yoy_sales_2025:+.2f}%")
    print(f"  * YoY Sales Growth (2026 vs 2025)  : {yoy_sales_2026:+.2f}%")
    print(f"  * YoY Profit Growth (2025 vs 2024) : {yoy_profit_2025:+.2f}%")
    print(f"  * YoY Profit Growth (2026 vs 2025) : {yoy_profit_2026:+.2f}%\n")

    # -------------------------------------------------------------
    # 3. CATEGORY & REGIONAL DRILL-DOWN EVALUATION
    # -------------------------------------------------------------
    cat_summary = df_merged.groupby("Category").agg(
        Total_Sales=("Sales_Amount", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    ).reset_index()
    cat_summary["Margin_Pct"] = (cat_summary["Total_Profit"] / cat_summary["Total_Sales"]) * 100

    print("-" * 85)
    print("SECTION 3: CATEGORICAL DAX AGGREGATIONS (DRILL-DOWN MATRIX EVALUATION)")
    print("-" * 85)
    print(f"{'Product Category':<18} | {'Total Sales (INR)':>18} | {'Total Profit (INR)':>18} | {'Margin %':>10}")
    print("-" * 85)
    for _, row in cat_summary.iterrows():
        print(f"{row['Category']:<18} | {row['Total_Sales']:>18,.2f} | {row['Total_Profit']:>18,.2f} | {row['Margin_Pct']:>9.2f}%")
    print("-" * 85)

    # -------------------------------------------------------------
    # 4. EXPORT SUMMARY REPORT
    # -------------------------------------------------------------
    out_dir = Path(__file__).resolve().parent
    summary_path = out_dir / "task_4_summary.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 4: DAX CALCULATED COLUMNS & MEASURES SUMMARY REPORT\n")
        f.write("=" * 75 + "\n\n")
        f.write("1. CORE REVENUE & TRANSACTION MEASURES:\n")
        for m_name, m_val, m_dax, m_desc in measures_core:
            f.write(f"- {m_name:<26}: {m_val}\n")
            f.write(f"  Formula : {m_dax}\n")
            f.write(f"  Purpose : {m_desc}\n\n")
        f.write("2. TIME INTELLIGENCE & YOY GROWTH:\n")
        f.write(f"- 2024 Sales (Base Year) : INR {sales_2024:,.2f}\n")
        f.write(f"- 2025 Sales (Prior SPLY): INR {sales_2025:,.2f} (YoY Growth: {yoy_sales_2025:+.2f}%)\n")
        f.write(f"- 2026 Sales (Current)   : INR {sales_2026:,.2f} (YoY Growth: {yoy_sales_2026:+.2f}%)\n")
        f.write(f"- 2025 vs 2024 Profit YoY: {yoy_profit_2025:+.2f}%\n")
        f.write(f"- 2026 vs 2025 Profit YoY: {yoy_profit_2026:+.2f}%\n\n")
        f.write("3. CATEGORY MARGIN BREAKDOWN:\n")
        for _, row in cat_summary.iterrows():
            f.write(f"- {row['Category']:<16}: Sales = INR {row['Total_Sales']:,.2f} | Profit = INR {row['Total_Profit']:,.2f} | Margin = {row['Margin_Pct']:.2f}%\n")

    print(f"\nTask 4 DAX summary saved to: {summary_path}")
    print("=" * 85)
    print("TASK 4 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_4()
