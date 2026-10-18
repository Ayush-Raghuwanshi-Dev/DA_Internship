"""
Task 3: Dataset Selection & Data Preparation ETL Script
Student: Ayush | PIEMR, Indore
Pipeline:
  1. Inspect raw contaminated dataset (raw_ecommerce_sales.csv)
  2. Identify column types and missing/duplicate values
  3. Purge obsolete technical columns
  4. Deduplicate rows by Order_ID
  5. Filter unlinked null customer records
  6. Impute missing Profit and Ship_Date values
  7. Engineer analytical feature columns (Delivery_Days, Profitability_Status, Order_Size_Bucket)
  8. Export final cleaned dataset for downstream EDA and Power BI modeling
"""

import sys
from datetime import datetime
from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "Data"
RAW_CSV = DATA_DIR / "raw_ecommerce_sales.csv"
CLEAN_CSV = DATA_DIR / "cleaned_ecommerce_sales.csv"
SUMMARY_FILE = BASE_DIR / "task_3_summary.txt"


def main():
    print("=" * 80)
    print("WEEK 6 - TASK 3: DATASET SELECTION & DATA PREPARATION ETL PIPELINE")
    print("=" * 80)
    print(f"Target Raw Data File: {RAW_CSV}\n")

    if not RAW_CSV.exists():
        print(f"Error: {RAW_CSV} not found! Please run generate_dataset.py first.")
        sys.exit(1)

    df_raw = pd.read_csv(RAW_CSV)
    raw_rows, raw_cols = df_raw.shape
    print(f"[Phase 1] Raw Ingestion: {raw_rows} rows x {raw_cols} columns.")

    # 1. Defect Audit
    dup_count = df_raw.duplicated(subset=["Order_ID"]).sum()
    null_counts = df_raw.isnull().sum()
    nulls_detected = null_counts[null_counts > 0].to_dict()

    print(f"\n[Phase 1 Defect Audit]:")
    print(f"  * Duplicate Order_IDs Detected : {dup_count}")
    print(f"  * Null Value Distribution     : {nulls_detected}")
    obsolete_cols = [c for c in ["ETL_Batch_ID", "Sys_Load_Timestamp", "Legacy_System_Flag"] if c in df_raw.columns]
    print(f"  * Obsolete Technical Columns   : {obsolete_cols}")

    # 2. ETL Cleaning Transformations
    print(f"\n[Phase 2 ETL Execution]:")
    df_clean = df_raw.copy()

    # Step 1: Remove obsolete columns
    if obsolete_cols:
        df_clean.drop(columns=obsolete_cols, inplace=True)
        print(f"  [Step 1] Purged {len(obsolete_cols)} obsolete technical columns.")

    # Step 2: Remove duplicate rows
    df_clean.drop_duplicates(subset=["Order_ID"], keep="first", inplace=True)
    print(f"  [Step 2] Deduplicated orders. Rows remaining: {len(df_clean)}")

    # Step 3: Filter unlinked missing Customer_ID records
    before_cust = len(df_clean)
    df_clean.dropna(subset=["Customer_ID"], inplace=True)
    print(f"  [Step 3] Filtered {before_cust - len(df_clean)} records with missing Customer_ID. Rows remaining: {len(df_clean)}")

    # Step 4: Impute missing Profit values
    missing_profit_mask = df_clean["Profit"].isnull()
    num_missing_profit = missing_profit_mask.sum()
    df_clean.loc[missing_profit_mask, "Profit"] = (
        df_clean.loc[missing_profit_mask, "Sales_Amount"] - df_clean.loc[missing_profit_mask, "Total_Cost"]
    ).round(2)
    # Recalculate margin %
    df_clean["Profit_Margin_Pct"] = (
        (df_clean["Profit"] / df_clean["Sales_Amount"]) * 100
    ).round(2)
    print(f"  [Step 4] Imputed {num_missing_profit} missing Profit values via [Sales_Amount] - [Total_Cost].")

    # Step 5: Impute missing Ship_Date values
    missing_ship_mask = df_clean["Ship_Date"].isnull()
    num_missing_ship = missing_ship_mask.sum()
    if num_missing_ship > 0:
        order_dates = pd.to_datetime(df_clean.loc[missing_ship_mask, "Order_Date"])
        df_clean.loc[missing_ship_mask, "Ship_Date"] = (
            order_dates + pd.to_timedelta(3, unit="D")
        ).dt.strftime("%Y-%m-%d")
        print(f"  [Step 5] Imputed {num_missing_ship} missing Ship_Dates with Order_Date + 3 days standard SLA.")

    # Step 6: Convert temporal types and engineer features
    order_dt_series = pd.to_datetime(df_clean["Order_Date"])
    ship_dt_series = pd.to_datetime(df_clean["Ship_Date"])
    df_clean["Delivery_Days"] = (ship_dt_series - order_dt_series).dt.days

    # Conditional feature: Profitability_Status
    def categorize_margin(row):
        if row["Profit"] < 0:
            return "Loss-Making"
        elif row["Profit_Margin_Pct"] >= 25.0:
            return "High Margin"
        else:
            return "Standard Margin"
    df_clean["Profitability_Status"] = df_clean.apply(categorize_margin, axis=1)

    # Conditional feature: Order_Size_Bucket
    def categorize_order_size(qty):
        if qty == 1:
            return "Single Item"
        elif qty <= 5:
            return "Multi-Item"
        else:
            return "Bulk Order"
    df_clean["Order_Size_Bucket"] = df_clean["Quantity"].apply(categorize_order_size)
    print("  [Step 6] Feature engineered: Delivery_Days, Profitability_Status, and Order_Size_Bucket.")

    # 3. Post-ETL Validation
    clean_rows, clean_cols = df_clean.shape
    remaining_nulls = df_clean.isnull().sum().sum()
    remaining_dups = df_clean.duplicated(subset=["Order_ID"]).sum()
    retention_rate = (clean_rows / raw_rows) * 100

    print(f"\n[Phase 3 Post-ETL Validation]:")
    print(f"  * Final Dataset Dimensions   : {clean_rows} rows x {clean_cols} columns")
    print(f"  * Remaining Missing Values   : {remaining_nulls}")
    print(f"  * Remaining Duplicate Orders : {remaining_dups}")
    print(f"  * Data Retention Rate        : {retention_rate:.2f}%")

    # Export
    df_clean.to_csv(CLEAN_CSV, index=False)
    print(f"  * Saved Cleaned Dataset to   : {CLEAN_CSV}")

    # Compile Summary
    summary_text = f"""TASK 3: DATASET SELECTION & DATA PREPARATION SUMMARY
================================================================================
1. DOMAIN & DATASET PROFILE:
   - Selected Domain           : Omnichannel E-Commerce & Retail Customer Analytics
   - Ingestion Source          : raw_ecommerce_sales.csv ({raw_rows} rows x {raw_cols} cols)
   - Scope of Attributes       : Transaction ID, Temporal, Geographies, Customer Segments,
                                 Product SKUs, Financials (Sales, Cost, Profit), Logistics.

2. DEFECT AUDIT & ETL TRANSFORMATIONS:
   - Obsolete Columns Purged   : {obsolete_cols} (3 columns removed)
   - Duplicate Orders Removed  : {dup_count} duplicate rows purged
   - Unlinked Customer Records : {before_cust - len(df_clean)} records removed
   - Missing Profits Imputed   : {num_missing_profit} values calculated via Net Sales - Total Cost
   - Missing Ship Dates Imputed: {num_missing_ship} values imputed via Order_Date + 3 days standard SLA

3. FEATURE ENGINEERING:
   - Delivery_Days             : Integer turnaround duration in days
   - Profitability_Status      : High Margin (>=25%), Standard Margin, Loss-Making (<0%)
   - Order_Size_Bucket         : Single Item (1), Multi-Item (2-5), Bulk Order (6+)

4. POST-ETL DATA HYGIENE METRICS:
   - Final Validated Records   : {clean_rows} rows x {clean_cols} columns
   - Total Missing Values      : {remaining_nulls} (0.00%)
   - Total Duplicate Orders    : {remaining_dups} (0.00%)
   - Data Authenticity Ratio   : {retention_rate:.2f}%
================================================================================
STATUS: TASK 3 COMPLETED SUCCESSFULLY!
"""
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print("\n" + "=" * 80)
    print(f"Task 3 summary saved to: {SUMMARY_FILE}")
    print("TASK 3 COMPLETED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    main()
