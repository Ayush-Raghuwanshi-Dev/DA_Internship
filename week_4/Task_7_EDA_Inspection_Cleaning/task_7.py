"""
Task 7: Exploratory Data Analysis - Data Inspection & Cleaning
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Inspect raw dirty dataset, detect null values, duplicates, and domain anomalies,
           apply data cleaning and imputation techniques, and export cleaned dataset.
"""

import os
import numpy as np
import pandas as pd

def run_task_7():
    print("=" * 80)
    print("WEEK 4 - TASK 7: EDA - DATA INSPECTION & DATA CLEANING")
    print("=" * 80)

    # 1. Load the raw dirty dataset
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "Task_7_EDA_Inspection_Cleaning", "raw_customer_data.csv")
    if not os.path.exists(raw_path):
        raw_path = os.path.join(base_dir, "Data", "raw_customer_data.csv")

    df_raw = pd.read_csv(raw_path)
    initial_rows = len(df_raw)
    print(f"Loaded raw dataset from: {raw_path}")
    print(f"Initial Dataset Dimensions: {df_raw.shape[0]} rows x {df_raw.shape[1]} columns\n")

    # 2. Phase 1: Data Inspection
    print("-" * 80)
    print("PHASE 1: INITIAL INSPECTION & DEFECT AUDIT")
    print("-" * 80)
    
    # Missing values count
    null_counts = df_raw.isnull().sum()
    print("Missing Values Per Column:")
    for col, cnt in null_counts.items():
        if cnt > 0:
            print(f"  * {col:<22}: {cnt} missing values ({(cnt/initial_rows)*100:.1f}%)")
        else:
            print(f"    {col:<22}: 0 missing")

    # Duplicate rows
    duplicate_mask = df_raw.duplicated()
    num_duplicates = int(duplicate_mask.sum())
    print(f"\nDuplicate Rows Detected: {num_duplicates}")

    # Domain integrity check (negative or impossible values)
    invalid_age = df_raw[(df_raw["Age"] < 18) | (df_raw["Age"] > 100)]
    invalid_spend = df_raw[df_raw["Total_Spend"] < 0]
    print(f"Domain Anomalies Detected: {len(invalid_age)} invalid Age records, {len(invalid_spend)} negative Total_Spend records.")

    # 3. Phase 2: Data Cleaning & Remediation
    print("\n" + "-" * 80)
    print("PHASE 2: EXECUTING SYSTEMATIC DATA CLEANING WORKFLOW")
    print("-" * 80)

    df_clean = df_raw.copy()

    # Step 1: Remove duplicate records
    print("Step 1: Removing Duplicate Rows...")
    df_clean = df_clean.drop_duplicates()
    dupes_removed = initial_rows - len(df_clean)
    print(f"  => Removed {dupes_removed} duplicate records. Current rows: {len(df_clean)}")

    # Step 2: Handle domain invalid values (corrupted input rows)
    print("Step 2: Remedying Domain Validity Violations (Negative Spend & Impossible Age)...")
    # Identify non-null invalid ages (e.g. negative numbers) and fix or drop
    corrupt_mask = (df_clean["Age"].notna() & ((df_clean["Age"] < 18) | (df_clean["Age"] > 100))) | \
                   (df_clean["Total_Spend"].notna() & (df_clean["Total_Spend"] < 0))
    corrupt_count = int(corrupt_mask.sum())
    df_clean = df_clean[~corrupt_mask]
    print(f"  => Filtered {corrupt_count} corrupt glitch rows. Current valid rows: {len(df_clean)}")

    # Step 3: Impute missing numerical values
    print("Step 3: Imputing Missing Values using Statistically Robust Strategies...")
    
    # Age: Impute with Median Age
    age_median = float(df_clean["Age"].median())
    df_clean["Age"] = df_clean["Age"].fillna(age_median).astype(int)
    print(f"  => Age nulls filled with Median: {age_median:.1f} years")

    # Income: Right-skewed -> Use Median imputation
    income_median = float(df_clean["Annual_Income_k"].median())
    df_clean["Annual_Income_k"] = df_clean["Annual_Income_k"].fillna(income_median).round(1)
    print(f"  => Annual_Income_k nulls filled with Median: {income_median:.2f}k")

    # Spending Score: Approximately symmetric -> Use Mean imputation
    spend_mean = float(df_clean["Spending_Score"].mean())
    df_clean["Spending_Score"] = df_clean["Spending_Score"].fillna(spend_mean).round(1)
    print(f"  => Spending_Score nulls filled with Mean: {spend_mean:.2f}")

    # Total Spend: Skewed -> Recompute from purchase_freq * avg_order_value or fill with median
    spend_median = float(df_clean["Total_Spend"].median())
    df_clean["Total_Spend"] = df_clean["Total_Spend"].fillna(spend_median).round(2)
    print(f"  => Total_Spend nulls filled with Median: {spend_median:.2f}")

    # Satisfaction Score: Discrete ordinal (1-5) -> Mode imputation
    sat_mode = int(df_clean["Satisfaction_Score"].mode().iloc[0])
    df_clean["Satisfaction_Score"] = df_clean["Satisfaction_Score"].fillna(sat_mode).astype(int)
    print(f"  => Satisfaction_Score nulls filled with Mode: {sat_mode}")

    # 4. Phase 3: Verification & Summary
    print("\n" + "-" * 80)
    print("PHASE 3: POST-CLEANING INTEGRITY VERIFICATION")
    print("-" * 80)
    post_nulls = df_clean.isnull().sum().sum()
    post_dupes = df_clean.duplicated().sum()
    final_rows = len(df_clean)
    print(f"Post-Cleaning Dimensions: {final_rows} rows x {df_clean.shape[1]} columns")
    print(f"Remaining Missing Values: {post_nulls}")
    print(f"Remaining Duplicate Rows: {post_dupes}")
    print(f"Retention Rate: {(final_rows / initial_rows)*100:.1f}% of authentic data retained.")

    # 5. Export Cleaned Dataset
    cleaned_out_path = os.path.join(base_dir, "Task_7_EDA_Inspection_Cleaning", "cleaned_customer_data.csv")
    df_clean.to_csv(cleaned_out_path, index=False)
    data_clean_path = os.path.join(base_dir, "Data", "cleaned_customer_data.csv")
    df_clean.to_csv(data_clean_path, index=False)
    print(f"\nCleaned dataset exported to: {cleaned_out_path}")

    # 6. Save Analytical Documentation
    summary_path = os.path.join(base_dir, "Task_7_EDA_Inspection_Cleaning", "task_7_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 7: EDA DATA INSPECTION & CLEANING REPORT\n")
        f.write("=" * 65 + "\n\n")
        f.write(f"1. Initial Raw Records: {initial_rows}\n")
        f.write(f"2. Duplicates Removed: {dupes_removed}\n")
        f.write(f"3. Final Clean Records: {final_rows}\n")
        f.write(f"4. Missing Values Imputed: Annual_Income_k (Median={income_median:.2f}k), Spending_Score (Mean={spend_mean:.2f}), Total_Spend (Median={spend_median:.2f})\n")
        f.write("\n5. Rationale for Cleaning Choices:\n")
        f.write("   - Dropping Duplicates: Repeated customer IDs artificially double record weights and skew sample variance.\n")
        f.write("   - Median vs Mean Imputation: Annual Income and Total Spend are positively skewed; mean imputation would artificially bias unobserved records upward. Using median preserves distribution shape.\n")
        f.write("   - Domain Bounds Filtering: Negative Age (-5) or negative spend (-999) represent data pipeline errors that would compromise statistical inferences if left untreated.\n")
    print(f"Task 7 cleaning documentation saved to: {summary_path}")
    print("=" * 80)
    print("TASK 7 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_7()
