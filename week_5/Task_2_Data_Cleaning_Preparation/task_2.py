"""
Task 2: Power Query Data Cleaning, Preparation & Transformation Pipeline
Internship: Data Analytics - Week 5
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Execute and verify the complete ETL cleaning pipeline on contaminated raw sales data,
           remedy nulls and duplicates, add custom conditional business features, and export cleaned dataset.
"""

import os
from pathlib import Path
import pandas as pd
import numpy as np

def run_task_2():
    print("=" * 80)
    print("WEEK 5 - TASK 2: DATA CLEANING & PREPARATION (POWER QUERY ETL PIPELINE)")
    print("=" * 80)

    base_dir = Path(__file__).resolve().parent
    raw_path = base_dir / "raw_fact_sales.csv"
    if not raw_path.exists():
        raw_path = base_dir.parent / "Data" / "raw_fact_sales.csv"

    df_raw = pd.read_csv(raw_path)
    initial_rows = len(df_raw)
    initial_cols = len(df_raw.columns)

    print(f"Loaded Contaminated Raw Sales Data: {raw_path}")
    print(f"Initial Dimensions: {initial_rows} rows x {initial_cols} columns\n")

    # 1. Defect Audit
    print("-" * 80)
    print("PHASE 1: DEFECT & CONTAMINATION AUDIT (PRE-CLEANING)")
    print("-" * 80)
    dupes_count = df_raw.duplicated(subset=["Order_ID"]).sum()
    print(f"Duplicate Orders Detected (subset=Order_ID): {dupes_count}")

    null_counts = df_raw.isnull().sum()
    print("Missing Values Detected:")
    for col, cnt in null_counts.items():
        if cnt > 0:
            print(f"  * {col:<22}: {cnt} missing values ({(cnt/initial_rows)*100:.1f}%)")

    junk_cols = [c for c in ["ETL_Batch_ID", "Sys_Load_Timestamp", "Legacy_System_Flag"] if c in df_raw.columns]
    print(f"Obsolete Technical Columns Identified: {junk_cols}")

    # 2. Execute ETL Cleaning Steps
    print("\n" + "-" * 80)
    print("PHASE 2: EXECUTING REPRODUCIBLE ETL TRANSFORMATIONS")
    print("-" * 80)

    df_clean = df_raw.copy()

    # Step 1: Remove obsolete columns
    print(f"Step 1: Removing Obsolete Technical Columns {junk_cols}...")
    df_clean = df_clean.drop(columns=junk_cols, errors="ignore")
    print(f"  => Columns reduced from {initial_cols} to {len(df_clean.columns)}")

    # Step 2: Deduplication on primary key
    print("Step 2: Removing Duplicate Transaction Records (Order_ID)...")
    df_clean = df_clean.drop_duplicates(subset=["Order_ID"])
    rows_after_dupes = len(df_clean)
    print(f"  => Purged {initial_rows - rows_after_dupes} duplicate rows. Remaining: {rows_after_dupes}")

    # Step 3: Remove records with missing Customer_Key (Orphan Foreign Keys)
    print("Step 3: Filtering Unlinked Records with Missing Customer_Key...")
    df_clean = df_clean[df_clean["Customer_Key"].notnull()]
    df_clean["Customer_Key"] = df_clean["Customer_Key"].astype(int)
    print(f"  => Current Valid Transactions: {len(df_clean)}")

    # Step 4: Recalculate Missing Profit & Profit Margin %
    print("Step 4: Imputing Missing Profit Values via Net Sales - Total Cost...")
    missing_profit_before = df_clean["Profit"].isnull().sum()
    df_clean["Profit"] = df_clean["Profit"].fillna(df_clean["Sales_Amount"] - df_clean["Total_Cost"]).round(2)
    df_clean["Profit_Margin_Pct"] = df_clean["Profit_Margin_Pct"].fillna(
        ((df_clean["Profit"] / df_clean["Sales_Amount"]) * 100).round(2)
    )
    print(f"  => Imputed {missing_profit_before} missing profit records. Remaining null profits: {df_clean['Profit'].isnull().sum()}")

    # Step 5: Convert Date Types and Calculate Delivery Duration
    print("Step 5: Converting Temporal Types & Computing Delivery Days...")
    df_clean["Order_Date"] = pd.to_datetime(df_clean["Order_Date"])
    df_clean["Ship_Date"] = pd.to_datetime(df_clean["Ship_Date"])
    # If Ship_Date is null, impute as Order_Date + 3 days
    missing_ship = df_clean["Ship_Date"].isnull().sum()
    df_clean["Ship_Date"] = df_clean["Ship_Date"].fillna(df_clean["Order_Date"] + pd.to_timedelta(3, unit='d'))
    df_clean["Delivery_Days"] = (df_clean["Ship_Date"] - df_clean["Order_Date"]).dt.days.astype(int)
    print(f"  => Imputed {missing_ship} missing Ship_Dates with Order_Date + 3 days standard delivery.")

    # Step 6: Custom Conditional Columns
    print("Step 6: Engineering Analytical Conditional Columns (Profitability Status & Order Size Bucket)...")
    def get_profit_status(margin):
        if margin >= 25.0:
            return "High Margin (>=25%)"
        elif margin >= 10.0:
            return "Standard Margin (10-25%)"
        elif margin >= 0.0:
            return "Low Margin (0-10%)"
        else:
            return "Loss-Making (<0%)"

    df_clean["Profitability_Status"] = df_clean["Profit_Margin_Pct"].apply(get_profit_status)

    def get_order_bucket(qty):
        if qty >= 6:
            return "Bulk Order (6+ units)"
        elif qty >= 2:
            return "Multi-Item Order (2-5 units)"
        else:
            return "Single Item Order (1 unit)"

    df_clean["Order_Size_Category"] = df_clean["Quantity"].apply(get_order_bucket)

    # Convert dates back to string format YYYY-MM-DD for CSV persistence
    df_clean["Order_Date"] = df_clean["Order_Date"].dt.strftime("%Y-%m-%d")
    df_clean["Ship_Date"] = df_clean["Ship_Date"].dt.strftime("%Y-%m-%d")

    # 3. Verification & Summary Audit
    print("\n" + "-" * 80)
    print("PHASE 3: POST-ETL DATA INTEGRITY AUDIT")
    print("-" * 80)
    final_rows = len(df_clean)
    final_cols = len(df_clean.columns)
    final_nulls = df_clean.isnull().sum().sum()
    final_dupes = df_clean.duplicated(subset=["Order_ID"]).sum()

    print(f"Final Cleaned Dataset Dimensions: {final_rows} rows x {final_cols} columns")
    print(f"Remaining Missing Values: {final_nulls}")
    print(f"Remaining Duplicate Orders: {final_dupes}")
    print(f"Data Authenticity Retention: {(final_rows / initial_rows)*100:.2f}%")

    # Export Cleaned Datasets
    out_clean_path = base_dir / "cleaned_fact_sales.csv"
    df_clean.to_csv(out_clean_path, index=False)
    data_clean_path = base_dir.parent / "Data" / "cleaned_fact_sales.csv"
    df_clean.to_csv(data_clean_path, index=False)
    print(f"\nSaved Cleaned Fact Sales to: {out_clean_path}")

    # Export Summary File
    summary_path = base_dir / "task_2_summary.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 2: POWER QUERY ETL DATA CLEANING & PREPARATION SUMMARY\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"1. Raw Ingestion Rows: {initial_rows}\n")
        f.write(f"2. Duplicate Orders Removed: {dupes_count}\n")
        f.write(f"3. Unlinked Null Customer Records Filtered: {rows_after_dupes - final_rows}\n")
        f.write(f"4. Missing Profits Imputed: {missing_profit_before} (via Net Sales - Total Cost)\n")
        f.write(f"5. Obsolete Columns Purged: {', '.join(junk_cols)}\n")
        f.write(f"6. Final Validated Records: {final_rows} (0 missing, 0 duplicates)\n")
        f.write(f"7. Retention Rate: {(final_rows / initial_rows)*100:.2f}%\n")
        f.write("\n8. Feature Engineering:\n")
        f.write("   - Delivery_Days: Date difference between Ship_Date and Order_Date\n")
        f.write("   - Profitability_Status: High Margin (>=25%), Standard Margin, Low Margin, Loss-Making (<0%)\n")
        f.write("   - Order_Size_Category: Bulk Order (6+), Multi-Item (2-5), Single Item (1)\n")
    print(f"Task 2 cleaning documentation saved to: {summary_path}")
    print("=" * 80)
    print("TASK 2 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_2()
