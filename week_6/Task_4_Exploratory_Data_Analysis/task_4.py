"""
Task 4: Exploratory Data Analysis (EDA) Script
Student: Ayush | PIEMR, Indore
Comprehensive Statistical Analysis:
  1. Descriptive statistics (Mean, Median, Std, Skewness, Kurtosis)
  2. Outlier detection using Interquartile Range (IQR) method
  3. Correlation analysis across numerical variables
  4. Categorical and regional breakdown
  5. Statistical trend identification and summary generation
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "Data"
CLEAN_CSV = DATA_DIR / "cleaned_ecommerce_sales.csv"
SUMMARY_FILE = BASE_DIR / "task_4_summary.txt"


def detect_iqr_outliers(series):
    """Compute Tukey's IQR bounds and count outliers."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    return {
        "Q1": round(q1, 2),
        "Q3": round(q3, 2),
        "IQR": round(iqr, 2),
        "Lower_Bound": round(lower_bound, 2),
        "Upper_Bound": round(upper_bound, 2),
        "Outlier_Count": len(outliers),
        "Outlier_Pct": round((len(outliers) / len(series)) * 100, 2)
    }


def main():
    print("=" * 80)
    print("WEEK 6 - TASK 4: EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 80)
    print(f"Dataset: {CLEAN_CSV}\n")

    if not CLEAN_CSV.exists():
        print(f"Error: {CLEAN_CSV} does not exist! Please run Task 3 first.")
        sys.exit(1)

    df = pd.read_csv(CLEAN_CSV)
    num_cols = ["Sales_Amount", "Profit", "Quantity", "Discount_Rate", "Unit_Price", "Delivery_Days"]

    # 1. Descriptive Statistics
    print("--------------------------------------------------------------------------------")
    print("SECTION 1: PARAMETRIC & NON-PARAMETRIC DESCRIPTIVE STATISTICS")
    print("--------------------------------------------------------------------------------")
    stats_rows = []
    for col in num_cols:
        s = df[col]
        mean_val = s.mean()
        median_val = s.median()
        mode_val = s.mode()[0]
        std_val = s.std()
        var_val = s.var()
        skew_val = s.skew()
        kurt_val = s.kurtosis()
        min_val = s.min()
        max_val = s.max()

        stats_rows.append({
            "Metric": col,
            "Mean": round(mean_val, 2),
            "Median": round(median_val, 2),
            "Mode": round(mode_val, 2),
            "Std_Dev": round(std_val, 2),
            "Variance": round(var_val, 2),
            "Skewness": round(skew_val, 2),
            "Kurtosis": round(kurt_val, 2),
            "Min": round(min_val, 2),
            "Max": round(max_val, 2)
        })

    df_stats = pd.DataFrame(stats_rows)
    print(df_stats.to_string(index=False))

    # 2. Outlier Analysis via IQR Method
    print("\n--------------------------------------------------------------------------------")
    print("SECTION 2: OUTLIER DETECTION VIA INTERQUARTILE RANGE (IQR) METHOD")
    print("--------------------------------------------------------------------------------")
    outlier_dict = {}
    for col in ["Sales_Amount", "Profit", "Quantity", "Unit_Price"]:
        outlier_res = detect_iqr_outliers(df[col])
        outlier_dict[col] = outlier_res
        print(f"Attribute: {col}")
        print(f"  * Q1: {outlier_res['Q1']} | Q3: {outlier_res['Q3']} | IQR: {outlier_res['IQR']}")
        print(f"  * Valid Range : [{outlier_res['Lower_Bound']}, {outlier_res['Upper_Bound']}]")
        print(f"  * Outliers    : {outlier_res['Outlier_Count']} rows ({outlier_res['Outlier_Pct']}%)")

    # 3. Correlation Matrix Analysis
    print("\n--------------------------------------------------------------------------------")
    print("SECTION 3: PAIRWISE CORRELATION MATRIX (PEARSON)")
    print("--------------------------------------------------------------------------------")
    corr_matrix = df[num_cols].corr().round(3)
    print(corr_matrix.to_string())

    # 4. Categorical Breakdown
    print("\n--------------------------------------------------------------------------------")
    print("SECTION 4: PRODUCT CATEGORY & SEGMENT PERFORMANCE BREAKDOWN")
    print("--------------------------------------------------------------------------------")
    cat_summary = df.groupby("Category").agg(
        Total_Sales=("Sales_Amount", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    ).reset_index()
    cat_summary["Margin_Pct"] = ((cat_summary["Total_Profit"] / cat_summary["Total_Sales"]) * 100).round(2)
    print("CATEGORY BREAKDOWN:")
    print(cat_summary.to_string(index=False))

    seg_summary = df.groupby("Customer_Segment").agg(
        Total_Sales=("Sales_Amount", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count"),
        Avg_Order_Value=("Sales_Amount", "mean")
    ).reset_index()
    seg_summary["Margin_Pct"] = ((seg_summary["Total_Profit"] / seg_summary["Total_Sales"]) * 100).round(2)
    seg_summary["Avg_Order_Value"] = seg_summary["Avg_Order_Value"].round(2)
    print("\nCUSTOMER SEGMENT BREAKDOWN:")
    print(seg_summary.to_string(index=False))

    reg_summary = df.groupby("Region").agg(
        Total_Sales=("Sales_Amount", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    ).reset_index()
    reg_summary["Margin_Pct"] = ((reg_summary["Total_Profit"] / reg_summary["Total_Sales"]) * 100).round(2)
    print("\nREGIONAL BREAKDOWN:")
    print(reg_summary.to_string(index=False))

    # Compile Summary File
    summary_text = f"""TASK 4: EXPLORATORY DATA ANALYSIS (EDA) COMPREHENSIVE REPORT
================================================================================
1. DESCRIPTIVE STATISTICS OVERVIEW (N = {len(df)} transactions):
{df_stats.to_string(index=False)}

2. IQR OUTLIER DETECTION RESULTS:
- Sales_Amount : {outlier_dict['Sales_Amount']['Outlier_Count']} outliers ({outlier_dict['Sales_Amount']['Outlier_Pct']}%) | Bounds: [{outlier_dict['Sales_Amount']['Lower_Bound']}, {outlier_dict['Sales_Amount']['Upper_Bound']}]
- Profit       : {outlier_dict['Profit']['Outlier_Count']} outliers ({outlier_dict['Profit']['Outlier_Pct']}%) | Bounds: [{outlier_dict['Profit']['Lower_Bound']}, {outlier_dict['Profit']['Upper_Bound']}]
- Quantity     : {outlier_dict['Quantity']['Outlier_Count']} outliers ({outlier_dict['Quantity']['Outlier_Pct']}%) | Bounds: [{outlier_dict['Quantity']['Lower_Bound']}, {outlier_dict['Quantity']['Upper_Bound']}]

3. CORRELATION ANALYSIS (PEARSON):
{corr_matrix.to_string()}

Key Correlation Insights:
- Sales_Amount & Profit       : r = {corr_matrix.loc['Sales_Amount', 'Profit']:.3f} (Strong positive correlation)
- Discount_Rate & Profit      : r = {corr_matrix.loc['Discount_Rate', 'Profit']:.3f} (Negative impact on net margin)
- Quantity & Sales_Amount     : r = {corr_matrix.loc['Quantity', 'Sales_Amount']:.3f} (Moderate positive correlation)

4. CATEGORY PERFORMANCE BREAKDOWN:
{cat_summary.to_string(index=False)}

5. CUSTOMER SEGMENT PERFORMANCE BREAKDOWN:
{seg_summary.to_string(index=False)}

6. REGIONAL PERFORMANCE BREAKDOWN:
{reg_summary.to_string(index=False)}
================================================================================
STATUS: TASK 4 COMPLETED SUCCESSFULLY!
"""
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print("\n" + "=" * 80)
    print(f"Task 4 EDA summary saved to: {SUMMARY_FILE}")
    print("TASK 4 COMPLETED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    main()
